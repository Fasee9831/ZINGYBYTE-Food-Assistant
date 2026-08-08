"""Main entry orchestrator with performance optimizations and enhanced UX."""

import re
import streamlit as st
from config import PAGE_CONFIG, DEFAULT_MODEL

st.set_page_config(**PAGE_CONFIG)

from styles import inject_premium_styles
from utils import init_app_state, compile_message_history, save_current_conversation
from ui import (
    render_sidebar_controls,
    render_top_bar,
    render_empty_state_screen,
    render_active_chat_bubbles,
    render_chat_bubble,
    render_background,
    _divider,
)
from chat import execute_grounded_stream, update_running_summary
from favorites import handle_add_favorite_request, format_favorites_display

try:
    from streamlit_js_eval import streamlit_js_eval
except ImportError:  # pragma: no cover — fallback if dependency is missing
    streamlit_js_eval = None

_IMAGE_EXT = re.compile(r'\.(jpg|jpeg|png|gif|webp|bmp|svg|ico|heic|heif|tiff?)\b', re.IGNORECASE)

_IMAGE_ERROR_RESPONSE = (
    "I'm your text-based food concierge! 🍔 Ask me about menu items, prices, "
    "ratings, live order tracking, or delivery info!"
)


def _inject_keyboard_shortcuts() -> None:
    """Inject JavaScript for keyboard shortcuts."""
    st.markdown(
        """
        <script>
        document.addEventListener('keydown', function(e) {
            // Ctrl/Cmd + K: Focus chat input
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                var input = document.querySelector('[data-testid="stChatInput"] textarea');
                if (input) { input.focus(); input.scrollIntoView({ behavior: 'smooth' }); }
            }
            // Ctrl/Cmd + Shift + K: Focus search
            if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'K') {
                e.preventDefault();
                var search = document.querySelector('[data-testid="stSidebar"] [data-testid="stTextInput"] input');
                if (search) { search.focus(); }
            }
        });
        </script>
        """,
        unsafe_allow_html=True,
    )


def _is_image_input(text: str) -> bool:
    if "data:image" in text or text.strip().startswith("data:"):
        return True
    if _IMAGE_EXT.search(text):
        return True
    return False


def _get_last_user_query() -> str:
    for msg in reversed(st.session_state.messages):
        if msg["role"] == "user":
            return msg["content"]
    return ""


def _detect_viewport() -> None:
    """Detect mobile via window.innerWidth once, defaulting to desktop."""
    if not st.session_state.get("_width_probe_pending", True):
        return
    if streamlit_js_eval is None:
        st.session_state.is_mobile = False
        st.session_state._width_probe_pending = False
        return
    try:
        width = streamlit_js_eval(js_expr="window.innerWidth", key="zb_width_probe")
    except Exception:
        width = None
    if width is None or int(width) <= 0:
        return  # probe again on the next rerun
    st.session_state.is_mobile = int(width) < 768
    st.session_state._width_probe_pending = False


def main() -> None:
    inject_premium_styles()
    _inject_keyboard_shortcuts()
    init_app_state()
    _detect_viewport()

    # Global floating background — persists across empty and chat states
    render_background()

    # Handle regenerate
    if st.session_state.get("regenerate"):
        st.session_state.regenerate = False
        last_query = _get_last_user_query()
        if last_query:
            st.session_state.input_injection = last_query
            for _ in range(2):
                if st.session_state.messages and st.session_state.messages[-1]["role"] in ("user", "assistant"):
                    st.session_state.messages.pop()
        st.rerun()
        return

    render_sidebar_controls()

    # Regenerate button below sidebar content
    with st.sidebar:
        msgs = st.session_state.messages
        if msgs and msgs[-1]["role"] == "assistant":
            _divider()
            if st.button("\U0001f504 Try again", use_container_width=True, key="regenerate_btn"):
                st.session_state.regenerate = True
                st.rerun()
    render_top_bar()

    # FETCH_FAVORITES — triggered by the "My Favorite Dishes" button in the menu drawer
    if st.session_state.pop("fetch_favorites", False):
        fav_reply = format_favorites_display()
        st.session_state.messages.append({"role": "assistant", "content": fav_reply})
        render_chat_bubble("assistant", fav_reply)
        save_current_conversation()
        st.rerun()
        return

    if not st.session_state.messages:
        render_empty_state_screen()
    else:
        render_active_chat_bubbles()

    # Handle input injection (from suggestion cards or follow-up questions)
    active_query = None
    if st.session_state.get("input_injection"):
        active_query = st.session_state.input_injection
        st.session_state.input_injection = None

    user_text_input = st.chat_input(
        "Ask me about the menu, your order, or anything food…"
    )
    if user_text_input:
        active_query = user_text_input

    if active_query:
        is_image = _is_image_input(active_query)
        user_display = "[Image / File pasted]" if is_image else active_query

        st.session_state.messages.append({"role": "user", "content": user_display})
        render_chat_bubble("user", user_display)

        if is_image:
            st.session_state.messages.append({
                "role": "assistant",
                "content": _IMAGE_ERROR_RESPONSE,
            })
            render_chat_bubble("assistant", _IMAGE_ERROR_RESPONSE)
            save_current_conversation()
            st.rerun()
            return

        # Natural-language add-to-favorites intent ("Make X my favorite" / "Add X to favorites")
        fav_result = handle_add_favorite_request(active_query)
        if fav_result is not None:
            fav_reply, _saved = fav_result
            st.session_state.messages.append({"role": "assistant", "content": fav_reply})
            render_chat_bubble("assistant", fav_reply)
            save_current_conversation()
            st.rerun()
            return

        history_payload = compile_message_history()
        response_text = ""
        had_error = False

        with st.chat_message("assistant"):
            text_placeholder = st.empty()

            with st.spinner("🍔 Let me check that for you…"):
                stream_node = execute_grounded_stream(
                    user_input=active_query,
                    history_payload=history_payload,
                    model_name=DEFAULT_MODEL,
                )

                for block in stream_node:
                    if block["type"] == "token":
                        response_text += block["content"]
                        text_placeholder.markdown(
                            response_text + '<span class="zb-cursor"></span>',
                            unsafe_allow_html=True,
                        )

                    elif block["type"] == "error":
                        had_error = True
                        raw = block["content"]
                        if "image" in raw.lower() or "not support" in raw.lower():
                            response_text = _IMAGE_ERROR_RESPONSE
                        else:
                            response_text = f"⚠️ {raw}"
                        text_placeholder.error(response_text)
                        break

            if not had_error:
                text_placeholder.markdown(response_text)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response_text,
        })

        if not had_error:
            update_running_summary(DEFAULT_MODEL)

        save_current_conversation()
        st.rerun()


if __name__ == "__main__":
    main()
