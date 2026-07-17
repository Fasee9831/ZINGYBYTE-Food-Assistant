"""Main entry orchestrator organizing execution lifecycles and application layouts."""

import streamlit as st
from config import PAGE_CONFIG

# Lock default workspace page profiles instantly before other dependencies process layouts
st.set_page_config(**PAGE_CONFIG)

from styles import inject_premium_styles
from utils import init_app_state, compile_message_history
from ui import (
    render_sidebar_controls,
    render_top_bar,
    render_empty_state_screen,
    render_active_chat_bubbles,
)
from chat import execute_grounded_stream, update_running_summary


def main() -> None:
    """Coordinates view generation loops, user inputs, and streaming engine cycles."""

    # 1. Inject the full design-system CSS
    inject_premium_styles()

    # 2. Initialise session state defaults
    init_app_state()

    # 3. Render sidebar panel
    render_sidebar_controls()

    # 4. Render top navigation bar
    render_top_bar()

    # 5. Render hero screen or live chat bubbles
    if not st.session_state.messages:
        render_empty_state_screen()
    else:
        render_active_chat_bubbles()

    # 6. Capture suggestion-card injected queries
    active_query = None
    if st.session_state.get("input_injection"):
        active_query = st.session_state.input_injection
        st.session_state.input_injection = None

    # 7. Capture manual text input
    user_text_input = st.chat_input(
        "Ask about any dish, customizations, delivery, or track your order…"
    )
    if user_text_input:
        active_query = user_text_input

    # 8. Execute query through the grounded streaming pipeline
    if active_query:
        st.session_state.messages.append({"role": "user", "content": active_query})
        with st.chat_message("user"):
            st.markdown(active_query)

        history_payload = compile_message_history()

        with st.chat_message("assistant"):
            text_placeholder  = st.empty()
            badge_placeholder = st.empty()

            accumulated_response = ""
            metrics_payload      = {}

            with st.spinner("🍔 Searching ZingyByte knowledge base…"):
                stream_node = execute_grounded_stream(
                    user_input=active_query,
                    history_payload=history_payload,
                    model_name=st.session_state.selected_model,
                )

                for block in stream_node:
                    if block["type"] == "token":
                        accumulated_response += block["content"]
                        metrics_payload       = block["metrics"]
                        elapsed = metrics_payload["elapsed"]
                        tokens  = metrics_payload["tokens"]
                        tps     = round(tokens / elapsed) if elapsed > 0 else 0

                        # Render text with animated cursor
                        text_placeholder.markdown(
                            accumulated_response + "<span class='zb-cursor'></span>",
                            unsafe_allow_html=True,
                        )

                        # Live streaming metrics
                        badge_placeholder.markdown(
                            f"<div class='zb-badge-row'>"
                            f"<span class='zb-badge streaming'>⏱️ {elapsed:.2f}s</span>"
                            f"<span class='zb-badge streaming'>🚀 {tps} t/s</span>"
                            f"<span class='zb-badge streaming'>✨ Generating…</span>"
                            f"</div>",
                            unsafe_allow_html=True,
                        )

                    elif block["type"] == "error":
                        text_placeholder.error(block["content"])
                        return

            # Final clean render — remove cursor
            text_placeholder.markdown(accumulated_response)

            # Clear streaming badges (will be shown in chat history on rerun)
            badge_placeholder.empty()

            # Persist message to session history
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": accumulated_response,
                    "metrics": metrics_payload,
                }
            )

            # Update rolling conversation summary if conversation is long
            update_running_summary(st.session_state.selected_model)

            # Store last latency for sidebar display
            if metrics_payload:
                st.session_state.metrics_history["execution_time"] = metrics_payload.get(
                    "elapsed", 0.0
                )

            st.rerun()


if __name__ == "__main__":
    main()
