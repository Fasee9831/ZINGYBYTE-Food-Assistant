"""LangChain engine with cached model, prompt, and optimized streaming."""

import time
from typing import Generator, Dict, Any, List
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from config import DEFAULT_MODEL, logger
from prompt import get_zingybyte_prompt, generate_followup_suggestions
from knowledge import query_knowledge_context

@st.cache_resource(show_spinner=False)
def get_cached_model(model_name: str) -> ChatGroq:
    logger.info(f"Loading Groq LLM: {model_name}")
    return ChatGroq(
        model_name=model_name,
        temperature=0.1,
        api_key=st.secrets["GROQ_API_KEY"]
    )

@st.cache_resource(show_spinner=False)
def get_cached_prompt() -> Any:
    return get_zingybyte_prompt()

def execute_grounded_stream(
    user_input: str,
    history_payload: list,
    model_name: str
) -> Generator[Dict[str, Any], None, None]:
    try:
        grounding_data = query_knowledge_context(user_input)
        model = get_cached_model(model_name)
        prompt_template = get_cached_prompt()
        parser = StrOutputParser()
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
                "metrics": {"elapsed": elapsed_duration, "tokens": token_counter}
            }

    except Exception as e:
        logger.error(f"Streaming error: {str(e)}")
        yield {"type": "error", "content": f"System error: {str(e)}"}

def generate_followup_questions(last_user_msg: str, last_ai_response: str) -> List[str]:
    return generate_followup_suggestions(last_user_msg, last_ai_response)

def update_running_summary(model_name: str) -> None:
    messages = st.session_state.messages
    if len(messages) > 6:
        slice_to_summarize = messages[:-4]
        transcript = ""
        for msg in slice_to_summarize:
            role = "Customer" if msg["role"] == "user" else "ZingyByte AI"
            transcript += f"{role}: {msg['content']}\n"
        try:
            model = get_cached_model(model_name)
            summary_prompt = (
                "You are an internal system utility. Summarize the following restaurant "
                "customer support conversation history in 2 extremely concise sentences. "
                f"Transcript:\n{transcript}\n\nSummary:"
            )
            summary_response = model.invoke(summary_prompt)
            st.session_state.chat_summary = summary_response.content.strip()
            logger.info(f"Summary updated: {st.session_state.chat_summary}")
        except Exception as e:
            logger.error(f"Summary failed: {str(e)}")
