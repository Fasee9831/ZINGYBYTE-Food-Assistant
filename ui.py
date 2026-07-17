"""Renders layout views, sidebar controls, top bar, and chat bubbles."""

import streamlit as st
from config import AVAILABLE_MODELS, PLATFORM_NAME, VERSION
from prompt import SUGGESTED_PROMPTS
from utils import export_session_logs


# ──────────────────────────────────────────────────────────
# INTERNAL HELPERS
# ──────────────────────────────────────────────────────────

def _divider() -> None:
    st.markdown("<hr>", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────────────────

def render_sidebar_controls() -> None:
    """Renders the premium sidebar panel."""
    if "ui_font_size" not in st.session_state:
        st.session_state.ui_font_size = 15

    with st.sidebar:

        # ── Brand Block ──────────────────────────────────
        st.markdown(
            f"""
            <div class="zb-sidebar-brand">
                <div class="zb-logo-row">
                    <div class="zb-logo-icon">&#127828;</div>
                    <div class="zb-logo-text">
                        <strong>{PLATFORM_NAME} AI</strong>
                        <span>Smart Serve &middot; v{VERSION}</span>
                    </div>
                </div>
                <span class="zb-status-pill">AI Core Online</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        _divider()

        # ── Conversation Context Summary ─────────────────
        summary = st.session_state.get("chat_summary", "")
        if summary:
            st.markdown(
                f"""
                <div class="zb-context-card">
                    <span class="zb-context-label">&#129504; Conversation Context</span>
                    <span class="zb-context-text">{summary}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            _divider()

        # ── Intelligence Core ────────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#129302; Intelligence Core</p>",
            unsafe_allow_html=True,
        )
        st.session_state.selected_model = st.selectbox(
            "Active Model",
            options=AVAILABLE_MODELS,
            index=(
                AVAILABLE_MODELS.index(st.session_state.selected_model)
                if st.session_state.selected_model in AVAILABLE_MODELS
                else 0
            ),
            help="Choose the local Ollama model powering responses.",
            label_visibility="collapsed",
        )

        _divider()

        # ── Session Analytics ────────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#128202; Session Stats</p>",
            unsafe_allow_html=True,
        )
        msgs        = st.session_state.messages
        user_turns  = sum(1 for m in msgs if m["role"] == "user")
        total_words = sum(len(m["content"].split()) for m in msgs if m["role"] == "assistant")
        latency     = st.session_state.metrics_history.get("execution_time", 0.0)

        st.markdown(
            f"""
            <div class="zb-stat-grid">
                <div class="zb-stat-tile">
                    <span class="zb-stat-value">{user_turns}</span>
                    <span class="zb-stat-label">Turns</span>
                </div>
                <div class="zb-stat-tile">
                    <span class="zb-stat-value">{latency:.1f}s</span>
                    <span class="zb-stat-label">Latency</span>
                </div>
                <div class="zb-stat-tile">
                    <span class="zb-stat-value">{total_words}</span>
                    <span class="zb-stat-label">AI Words</span>
                </div>
                <div class="zb-stat-tile">
                    <span class="zb-stat-value">{len(msgs)}</span>
                    <span class="zb-stat-label">Messages</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        _divider()

        # ── Interface Scale ──────────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#127912; Text Scale</p>",
            unsafe_allow_html=True,
        )
        st.session_state.ui_font_size = st.slider(
            "Text size (px)",
            min_value=12,
            max_value=20,
            value=st.session_state.ui_font_size,
            step=1,
            help="Adjust global text size for readability.",
            label_visibility="collapsed",
        )

        _divider()

        # ── Actions ──────────────────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#9881;&#65039; Actions</p>",
            unsafe_allow_html=True,
        )
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("&#x1F9F9; Clear", use_container_width=True, help="Clear all messages"):
                st.session_state.messages = []
                st.session_state.chat_summary = ""
                st.session_state.metrics_history = {"total_tokens": 0, "execution_time": 0.0}
                st.rerun()
        with col_b:
            st.download_button(
                label="&#x1F4E5; Export",
                data=export_session_logs(),
                file_name="zingybyte_chat.json",
                mime="application/json",
                use_container_width=True,
                help="Download full chat history as JSON",
            )

        _divider()

        # ── Quick Tips ───────────────────────────────────
        st.markdown(
            "<p class='zb-section-label'>&#128161; Quick Tips</p>",
            unsafe_allow_html=True,
        )
        tips = [
            ("&#127831;", "Ask about <b>any menu item</b> by name for prices &amp; ratings"),
            ("&#128661;", "Track orders with your <b>ZB-XXXX</b> token"),
            ("&#10024;", "Try <b>combo suggestions</b> for best meal deals"),
            ("&#128172;", "Ask about <b>delivery fees</b> or cancellation policy"),
        ]
        tip_html = '<div class="zb-tips">'
        for icon, text in tips:
            tip_html += (
                f'<div class="zb-tip-row">'
                f'<span class="zb-tip-icon">{icon}</span>'
                f'<span>{text}</span>'
                f'</div>'
            )
        tip_html += '</div>'
        st.markdown(tip_html, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# TOP NAVIGATION BAR
# ──────────────────────────────────────────────────────────

def render_top_bar() -> None:
    """Renders a slim context bar at the top of the chat area."""
    model   = st.session_state.get("selected_model", "llama3")
    msgs    = st.session_state.get("messages", [])
    turns   = sum(1 for m in msgs if m["role"] == "user")

    # Pre-compute all conditional HTML outside the f-string to avoid parser bugs
    turn_label = f"{turns} turn" if turns == 1 else f"{turns} turns"

    if turns > 0:
        live_chip = (
            '<span class="zb-chip-live">&#9679; Live</span>'
        )
    else:
        live_chip = ""

    html_str = f"""
<div class="zb-topbar">
    <div class="zb-topbar-left">
        <span class="zb-topbar-icon">&#127828;</span>
        <span class="zb-topbar-name">ZingyByte AI</span>
        <span class="zb-topbar-sep">/</span>
        <span class="zb-topbar-sub">Smart Serve Console</span>
    </div>
    <div class="zb-topbar-right">
        <span class="zb-chip">&#128172; {turn_label}</span>
        <span class="zb-chip-model">&#129302; {model.upper()}</span>{live_chip}
    </div>
</div>
"""
    st.markdown(html_str, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────
# EMPTY STATE / HERO
# ──────────────────────────────────────────────────────────

def render_empty_state_screen() -> None:
    """Renders the animated hero section and suggestion cards."""

    # Floating food background
    food_emojis = ["🍔", "🍟", "🍕", "🌭", "🍿", "🍩", "🍗", "🌮", "🥪", "🥤", "🍦", "🥓"]
    food_html = '<div class="zb-food-bg">'
    for emoji in food_emojis:
        food_html += f'<div class="zb-food-item">{emoji}</div>'
    food_html += '</div>'
    st.markdown(food_html, unsafe_allow_html=True)

    # Hero
    st.markdown(
        """
        <div class="zb-hero">
            <span class="zb-hero-icon">&#127828;</span>
            <h1 class="zb-hero-title">ZingyByte AI</h1>
            <p class="zb-hero-sub">Your smart food concierge &mdash; menus, orders &amp; deals in seconds.</p>
            <div class="zb-hero-badge-wrap">
                <span class="zb-hero-badge">Grounded Menu Knowledge &middot; Always On</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Grid label
    st.markdown(
        "<p class='zb-grid-label'>Try a suggested query</p>",
        unsafe_allow_html=True,
    )

    # 2-column suggestion grid
    cols = st.columns(2, gap="medium")
    for idx, card in enumerate(SUGGESTED_PROMPTS):
        parts = card["label"].split(" ", 1)
        emoji = parts[0] if parts else "&#127374;"
        title = parts[1] if len(parts) > 1 else card["label"]

        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="zb-card">
                    <span class="zb-card-emoji">{emoji}</span>
                    <span class="zb-card-title">{title}</span>
                    <span class="zb-card-desc">{card['query']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Ask this", key=f"preset_{idx}", use_container_width=True):
                st.session_state.input_injection = card["query"]
                st.rerun()


# ──────────────────────────────────────────────────────────
# ACTIVE CHAT BUBBLES
# ──────────────────────────────────────────────────────────

def render_active_chat_bubbles() -> None:
    """Renders all conversation messages with metric badges on AI turns."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if "metrics" in message and message["role"] == "assistant":
                m          = message["metrics"]
                word_count = len(message["content"].split())
                read_time  = max(1, round(word_count / 200))
                tokens     = m.get("tokens", 0)
                elapsed    = m.get("elapsed", 1)
                tps        = round(tokens / elapsed) if elapsed > 0 else 0

                badges = (
                    f'<div class="zb-badge-row">'
                    f'<span class="zb-badge">&#9201; {elapsed:.2f}s</span>'
                    f'<span class="zb-badge">&#128640; {tps} t/s</span>'
                    f'<span class="zb-badge">&#9889; {tokens} chunks</span>'
                    f'<span class="zb-badge">&#128221; {word_count} words</span>'
                    f'<span class="zb-badge">&#128214; ~{read_time} min read</span>'
                    f'</div>'
                )
                st.markdown(badges, unsafe_allow_html=True)
