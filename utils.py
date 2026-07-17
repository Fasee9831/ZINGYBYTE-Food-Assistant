"""Runtime session state configuration methods and file generation handlers."""

import json
from datetime import datetime
from typing import List
import streamlit as st
# Added SystemMessage to feed compiled summary to the LangChain engine
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from config import DEFAULT_MODEL

def init_app_state() -> None:
    """Safely locks standard reactive dictionary keys inside the current state context."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = DEFAULT_MODEL
    if "metrics_history" not in st.session_state:
        st.session_state.metrics_history = {"total_tokens": 0, "execution_time": 0.0}
    # [NEW] Initialize chat summary session memory
    if "chat_summary" not in st.session_state:
        st.session_state.chat_summary = ""

def compile_message_history() -> List:
    """Converts local state log indexes into structural message components for LangChain context mapping."""
    history = []
    
    # 1. Prepend dynamic system summary if one exists
    if st.session_state.get("chat_summary"):
        history.append(
            SystemMessage(content=f"[SUMMARY OF PRIOR CONVERSATION]: {st.session_state.chat_summary}")
        )
    
    # 2. Keep the sliding history window tiny (last 4 messages) to prevent slow inference
    active_window = st.session_state.messages[-4:]
    for msg in active_window:
        if msg["role"] == "user":
            history.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            history.append(AIMessage(content=msg["content"]))
            
    return history

def export_session_logs() -> str:
    """Serializes the active session logs into a standard printable JSON layout structure."""
    return json.dumps({
        "agent": "ZingyByte AI — Smart Serve Platform",
        "timestamp": datetime.utcnow().isoformat(),
        "summary": st.session_state.get("chat_summary", ""),
        "logs": st.session_state.messages
    }, indent=2)