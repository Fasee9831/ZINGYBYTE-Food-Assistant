"""Runtime session state configuration, conversation management, and file generation."""

import re
import os
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
from dataclasses import dataclass, field
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from config import DEFAULT_MODEL, PLATFORM_NAME, VERSION

_IMAGE_EXT_RE = re.compile(r'\.(jpg|jpeg|png|gif|webp|bmp|svg|ico|heic|heif|tiff?)\b', re.IGNORECASE)

def _redact_image_content(text: str) -> str:
    if "data:image" in text or text.strip().startswith("data:"):
        return "[Image content removed]"
    if _IMAGE_EXT_RE.search(text):
        return "[Image content removed]"
    return text


@dataclass
class Conversation:
    id: str
    title: str
    messages: List[Dict]
    created_at: datetime
    updated_at: datetime
    message_count: int
    summary: str = ""
    metrics: Dict = field(default_factory=lambda: {"total_tokens": 0, "execution_time": 0.0})
    last_user_query: str = ""

_MENU_KEYWORDS = {
    "biryani": "🍚 Biryani Chat",
    "pizza": "🍕 Pizza Chat",
    "burger": "🍔 Burger Chat",
    "shawarma": "🌯 Shawarma Chat",
    "sandwich": "🥪 Sandwiches",
    "chicken": "🍗 Chicken",
    "drink": "🥤 Drinks",
    "milkshake": "🥤 Drinks",
    "mojito": "🥤 Drinks",
    "lemonade": "🥤 Drinks",
    "soda": "🥤 Drinks",
    "broasted": "🍗 Broasted Chicken",
    "garlic": "🍗 Broasted Chicken",
    "honey": "🍗 Broasted Chicken",
    "paneer": "🥪 Paneer",
    "cheese": "🧀 Cheese",
    "beef": "🍔 Beef",
    "bbq": "🍔 BBQ",
    "mexican": "🌮 Mexican",
    "tandoori": "🍗 Tandoori",
    "pepperoni": "🍕 Pepperoni Pizza",
    "primavera": "🍕 Primavera Pizza",
    "chicago": "🍕 Chicago Deep Dish",
    "malabar": "🍚 Malabar Biryani",
    "afghani": "🍚 Afghani Biryani",
    "peri": "🌯 Peri Peri Shawarma",
    "mixed": "🌯 Mixed Shawarma",
    "classic": "🍗 Classic Chicken",
    "cloud": "🥪 Cloud Egg Toast",
}

_GENERIC_TITLES = [
    (["order", "track", "where", "status", "eta", "delivery"], "🛵 Order Tracking"),
    (["delivery", "fee", "free", "cost", "price", "payment", "pay", "card", "cash", "cod", "upi"], "💳 Payment & Delivery"),
    (["menu", "food", "eat", "hungry", "suggest", "recommend", "option", "list", "have", "what"], "🍕 Exploring the Menu"),
    (["hello", "hi", "hey", "help", "start"], "👋 General Chat"),
]


def _generate_conversation_id() -> str:
    return uuid.uuid4().hex[:12]


def _auto_generate_title(messages: List[Dict]) -> str:
    for msg in messages:
        if msg["role"] == "user":
            text = msg["content"].lower()
            for keyword, title in _MENU_KEYWORDS.items():
                if keyword in text:
                    return title
            for keywords, title in _GENERIC_TITLES:
                if any(kw in text for kw in keywords):
                    return title
            return "💬 General Chat"
    return "💬 New Conversation"


def init_app_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    else:
        for msg in st.session_state.messages:
            msg["content"] = _redact_image_content(msg["content"])
    if "favorite_dishes" not in st.session_state:
        st.session_state.favorite_dishes = {}
    if "favorites" not in st.session_state:
        st.session_state.favorites = set()
    if "metrics_history" not in st.session_state:
        st.session_state.metrics_history = {"total_tokens": 0, "execution_time": 0.0}
    if "chat_summary" not in st.session_state:
        st.session_state.chat_summary = ""
    if "conversations" not in st.session_state:
        st.session_state.conversations = {}
    if "current_conv_id" not in st.session_state:
        st.session_state.current_conv_id = _generate_conversation_id()
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""
    if "renaming_conv" not in st.session_state:
        st.session_state.renaming_conv = None
    if "switch_to_conv" not in st.session_state:
        st.session_state.switch_to_conv = None
    if "regenerate" not in st.session_state:
        st.session_state.regenerate = False
    if "total_tokens_used" not in st.session_state:
        st.session_state.total_tokens_used = 0
    if "session_start_time" not in st.session_state:
        st.session_state.session_start_time = datetime.now()


def save_current_conversation() -> str:
    conv_id = st.session_state.current_conv_id
    messages = st.session_state.messages
    if not messages:
        return conv_id
    title = _auto_generate_title(messages)
    existing = st.session_state.conversations.get(conv_id)
    st.session_state.conversations[conv_id] = Conversation(
        id=conv_id,
        title=title,
        messages=messages.copy(),
        created_at=existing.created_at if existing else datetime.now(),
        updated_at=datetime.now(),
        message_count=len([m for m in messages if m["role"] == "user"]),
        summary=st.session_state.chat_summary,
        metrics=st.session_state.metrics_history.copy(),
        last_user_query=_get_last_user_query(messages),
    )
    return conv_id


def _get_last_user_query(messages):
    for msg in reversed(messages):
        if msg["role"] == "user":
            return msg["content"]
    return ""


def load_conversation(conv_id: str) -> None:
    if conv_id in st.session_state.conversations:
        conv = st.session_state.conversations[conv_id]
        st.session_state.messages = conv.messages.copy()
        st.session_state.chat_summary = conv.summary
        st.session_state.metrics_history = conv.metrics.copy()
        st.session_state.current_conv_id = conv_id
        st.session_state.search_query = ""


def start_new_conversation() -> None:
    save_current_conversation()
    st.session_state.messages = []
    st.session_state.chat_summary = ""
    st.session_state.metrics_history = {"total_tokens": 0, "execution_time": 0.0}
    st.session_state.current_conv_id = _generate_conversation_id()
    st.session_state.search_query = ""


def rename_conversation(conv_id: str, new_title: str) -> None:
    if conv_id in st.session_state.conversations:
        st.session_state.conversations[conv_id].title = new_title


def get_conversation_groups() -> Dict[str, List[Tuple[str, Conversation]]]:
    now = datetime.now()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday_start = today_start - timedelta(days=1)
    week_start = today_start - timedelta(days=7)
    groups = {"Today": [], "Yesterday": [], "Previous 7 Days": [], "Older": []}
    for conv_id, conv in st.session_state.conversations.items():
        updated = conv.updated_at
        if updated >= today_start:
            groups["Today"].append((conv_id, conv))
        elif updated >= yesterday_start:
            groups["Yesterday"].append((conv_id, conv))
        elif updated >= week_start:
            groups["Previous 7 Days"].append((conv_id, conv))
        else:
            groups["Older"].append((conv_id, conv))
    for key in groups:
        groups[key].sort(key=lambda x: x[1].updated_at, reverse=True)
    return groups


def search_conversations(query: str) -> List[Tuple[str, Conversation]]:
    if not query:
        return []
    query = query.lower()
    results = []
    for conv_id, conv in st.session_state.conversations.items():
        if query in conv.title.lower():
            results.append((conv_id, conv))
            continue
        for msg in conv.messages:
            if query in msg["content"].lower():
                results.append((conv_id, conv))
                break
    return results


def get_chat_statistics() -> Dict:
    msgs = st.session_state.messages
    user_turns = sum(1 for m in msgs if m["role"] == "user")
    ai_turns = sum(1 for m in msgs if m["role"] == "assistant")
    total_words = sum(len(m["content"].split()) for m in msgs if m["role"] == "assistant")
    latency = st.session_state.metrics_history.get("execution_time", 0.0)
    duration = datetime.now() - st.session_state.session_start_time
    duration_mins = int(duration.total_seconds() // 60)
    return {
        "messages": len(msgs),
        "user_turns": user_turns,
        "ai_turns": ai_turns,
        "total_words": total_words,
        "latency": latency,
        "duration_mins": duration_mins,
        "tokens": st.session_state.total_tokens_used,
    }


def compile_message_history() -> List:
    history = []
    if st.session_state.get("chat_summary"):
        history.append(SystemMessage(content=f"[SUMMARY OF PRIOR CONVERSATION]: {st.session_state.chat_summary}"))
    active_window = st.session_state.messages[-4:]
    for msg in active_window:
        safe = _redact_image_content(msg["content"])
        if msg["role"] == "user":
            history.append(HumanMessage(content=safe))
        elif msg["role"] == "assistant":
            history.append(AIMessage(content=safe))
    return history
