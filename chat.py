"""LangChain engine with multi-model failover, cached models, and rate-limit immune streaming."""

import time
from typing import Generator, Dict, Any, List
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from config import DEFAULT_MODEL, FALLBACK_MODELS, logger
from prompt import get_zingybyte_prompt, generate_followup_suggestions
from knowledge import query_knowledge_context, generate_local_fallback_response


def _get_api_keys() -> List[str]:
    """Retrieve all available Groq API keys (supports single key or multi-key rotation)."""
    keys = []
    if "GROQ_API_KEYS" in st.secrets:
        raw = st.secrets["GROQ_API_KEYS"]
        if isinstance(raw, list):
            keys.extend(raw)
        elif isinstance(raw, str):
            keys.extend([k.strip() for k in raw.split(",") if k.strip()])
    if "GROQ_API_KEY" in st.secrets and st.secrets["GROQ_API_KEY"] not in keys:
        keys.append(st.secrets["GROQ_API_KEY"])
    return [k for k in keys if k] if keys else [""]


@st.cache_resource(show_spinner=False)
def get_cached_model(model_name: str, api_key: str = "") -> ChatGroq:
    logger.info(f"Loading Groq LLM: {model_name}")
    key = api_key or _get_api_keys()[0]
    return ChatGroq(
        model_name=model_name,
        temperature=0.1,
        api_key=key,
        max_retries=2,
        max_tokens=500
    )


@st.cache_resource(show_spinner=False)
def get_cached_prompt() -> Any:
    return get_zingybyte_prompt()


def _is_rate_limit_error(err_str: str) -> bool:
    err_lower = err_str.lower()
    return any(term in err_lower for term in [
        "rate limit", "429", "tpm", "quota", "too many requests", "resource_exhausted", "tokens per minute"
    ])


def execute_grounded_stream(
    user_input: str,
    history_payload: list,
    model_name: str = DEFAULT_MODEL
) -> Generator[Dict[str, Any], None, None]:
    grounding_data = query_knowledge_context(user_input)
    prompt_template = get_cached_prompt()
    parser = StrOutputParser()

    # Determine priority list of models to try
    if model_name in ("auto", None, ""):
        candidates = FALLBACK_MODELS.copy()
    else:
        candidates = [model_name] + [m for m in FALLBACK_MODELS if m != model_name]

    api_keys = _get_api_keys()
    streamed_any = False

    # Attempt 1: Try across available models and API keys
    for key in api_keys:
        for attempt, candidate_model in enumerate(candidates):
            try:
                logger.info(f"Streaming attempt {attempt + 1}/{len(candidates)} using {candidate_model}")
                model = get_cached_model(candidate_model, api_key=key)
                chain = prompt_template | model | parser
                start_time = time.perf_counter()
                token_counter = 0

                for chunk in chain.stream({
                    "input": user_input,
                    "history": history_payload,
                    "grounding_context": grounding_data
                }):
                    token_counter += 1
                    streamed_any = True
                    elapsed_duration = time.perf_counter() - start_time
                    yield {
                        "type": "token",
                        "content": chunk,
                        "metrics": {
                            "elapsed": elapsed_duration,
                            "tokens": token_counter,
                            "model": candidate_model
                        }
                    }
                # Successfully completed streaming
                return

            except Exception as e:
                err_str = str(e)
                logger.warning(f"Error on candidate {candidate_model}: {err_str}")

                # If tokens were already yielded to UI, do not switch mid-stream
                if streamed_any:
                    logger.error(f"Stream interrupted midway on {candidate_model}: {err_str}")
                    yield {"type": "error", "content": "Network hiccup mid-response. Please try asking again!"}
                    return

                if _is_rate_limit_error(err_str):
                    logger.info(f"Model {candidate_model} reached rate limit. Failing over to next model...")
                    time.sleep(0.4)
                    continue
                else:
                    # Transient error — try next candidate model
                    continue

    # Attempt 2: Replenishment wait (2.5s) on primary model
    logger.info("All pool models reached limit. Waiting 2.5s for token replenishment...")
    time.sleep(2.5)
    try:
        fallback_target = candidates[0]
        model = get_cached_model(fallback_target, api_key=api_keys[0])
        chain = prompt_template | model | parser
        start_time = time.perf_counter()
        token_counter = 0

        for chunk in chain.stream({
            "input": user_input,
            "history": history_payload,
            "grounding_context": grounding_data
        }):
            token_counter += 1
            elapsed_duration = time.perf_counter() - start_time
            yield {
                "type": "token",
                "content": chunk,
                "metrics": {
                    "elapsed": elapsed_duration,
                    "tokens": token_counter,
                    "model": fallback_target
                }
            }
        return

    except Exception as final_e:
        # Attempt 3: Zero-Token Local Knowledge Engine
        # Guarantees the chatbot NEVER stops working even if daily API quota is completely spent
        logger.warning(f"Cloud API limits completely reached ({final_e}). Seamlessly switching to Zero-Token Local Engine!")
        fallback_text = generate_local_fallback_response(user_input)
        start_time = time.perf_counter()
        words = fallback_text.split(" ")
        for i, word in enumerate(words):
            chunk = word if i == len(words) - 1 else word + " "
            time.sleep(0.012)  # Natural typing feel
            yield {
                "type": "token",
                "content": chunk,
                "metrics": {
                    "elapsed": time.perf_counter() - start_time,
                    "tokens": i + 1,
                    "model": "Zero-Token Offline Shield"
                }
            }
        return


def generate_followup_questions(last_user_msg: str, last_ai_response: str) -> List[str]:
    return generate_followup_suggestions(last_user_msg, last_ai_response)


def update_running_summary(model_name: str) -> None:
    """Lightweight summary update every 6 messages using separate model pool."""
    messages = st.session_state.messages
    # Only run every 6 turns to conserve token budget
    if len(messages) >= 6 and len(messages) % 6 == 0:
        slice_to_summarize = messages[:-2]
        transcript = ""
        for msg in slice_to_summarize[-6:]:
            role = "Customer" if msg["role"] == "user" else "ZingyByte AI"
            transcript += f"{role}: {msg['content'][:100]}\n"
        try:
            summary_model = get_cached_model("qwen/qwen3.8-27b")
            summary_prompt = (
                "You are an internal system utility. Summarize the following restaurant "
                "customer support conversation history in 2 extremely concise sentences. "
                f"Transcript:\n{transcript}\n\nSummary:"
            )
            summary_response = summary_model.invoke(summary_prompt)
            st.session_state.chat_summary = summary_response.content.strip()
            logger.info(f"Summary updated: {st.session_state.chat_summary}")
        except Exception as e:
            logger.warning(f"Summary skipped gracefully: {str(e)}")
