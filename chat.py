"""LangChain engine implementation managing cached model instances and context injections."""

import time
from typing import Generator, Dict, Any
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from config import OLLAMA_BASE_URL, DEFAULT_MODEL, logger
from prompt import get_zingybyte_prompt
from knowledge import query_knowledge_context

@st.cache_resource(show_spinner=False)
def get_cached_model(model_name: str) -> ChatOllama:
    """Initializes and caches a thread-safe ChatOllama instance."""
    logger.info(f"Loading local LLM client runtime profile: {model_name}")
    return ChatOllama(
        base_url=OLLAMA_BASE_URL,
        model=model_name,
        temperature=0.1,  # Low temperature to prioritize accurate information retrieval
        num_ctx=4096
    )

def execute_grounded_stream(
    user_input: str,
    history_payload: list,
    model_name: str
) -> Generator[Dict[str, Any], None, None]:
    """Retrieves menu/FAQ details and pumps grounded variables into the streaming inference chain."""
    try:
        # 1. Fetch relevant menu details or FAQ matches from the user query
        grounding_data = query_knowledge_context(user_input)
        
        # 2. Setup the model client instance and prompt layout templates
        model = get_cached_model(model_name)
        prompt_template = get_zingybyte_prompt()
        parser = StrOutputParser()
        
        # 3. Assemble the runtime execution chain
        chain = prompt_template | model | parser
        
        start_time = time.perf_counter()
        token_counter = 0
        
        # 4. Stream response tokens back to the main UI container
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
        logger.error(f"Execution pipeline failure encountered during model streaming: {str(e)}")
        yield {"type": "error", "content": f"System error encountered during generation: {str(e)}"}

def update_running_summary(model_name: str) -> None:
    """Summarizes older conversation history on the fly, storing it in session state."""
    messages = st.session_state.messages
    
    # Trigger summarization only when the log gets relatively long (more than 6 messages)
    if len(messages) > 6:
        # Summarize everything except the last 4 hot messages
        slice_to_summarize = messages[:-4]
        
        # Translate conversational history into a plain transcript
        transcript = ""
        for msg in slice_to_summarize:
            role = "Customer" if msg["role"] == "user" else "ZingyByte AI"
            transcript += f"{role}: {msg['content']}\n"
            
        try:
            model = get_cached_model(model_name)
            
            # Prompt the model directly to compile a concise summary
            summary_prompt = (
                "You are an internal system utility. Summarize the following restaurant "
                "customer support conversation history in 2 extremely concise sentences. Focus solely "
                "on what the customer asked, ordered, or decided. Do not include greetings, introductions, or system logs.\n\n"
                f"Transcript:\n{transcript}\n\n"
                "Summary:"
            )
            
            # Generate the summary synchronously (avoiding stream overhead for background task)
            summary_response = model.invoke(summary_prompt)
            st.session_state.chat_summary = summary_response.content.strip()
            logger.info(f"Updated dynamic conversation summary successfully: {st.session_state.chat_summary}")
            
        except Exception as e:
            logger.error(f"Failed to compile dynamic conversation summary: {str(e)}")