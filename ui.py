"""Renders layout views, sidebar controls, top bar, and chat bubbles."""

from datetime import datetime
import streamlit as st
from config import PLATFORM_NAME
from prompt import SUGGESTED_PROMPTS
from utils import (
    save_current_conversation, load_conversation,
    start_new_conversation, get_conversation_groups, search_conversations,
    rename_conversation,
    Conversation
)


def _divider() -> None:
    st.markdown("<hr>", unsafe_allow_html=True)


FOOD_EMOJIS: list = [
    "&#127828;", "&#127839;", "&#127829;", "&#127789;", "&#127831;",
    "&#127849;", "&#127830;", "&#127820;", "&#127838;", "&#127864;",
]


def render_background() -> None:
    """Reusable floating animated food-emoji background, rendered once globally."""
    food_html = '<div class="zb-food-bg">'
    for emoji in FOOD_EMOJIS:
        food_html += f'<div class="zb-food-item">{emoji}</div>'
    food_html += '</div>'
    st.markdown(food_html, unsafe_allow_html=True)


def _is_mobile() -> bool:
    return bool(st.session_state.get("is_mobile", False))


def render_sidebar_controls() -> None:
    if "ui_font_size" not in st.session_state:
        st.session_state.ui_font_size = 15

    with st.sidebar:
        # ── Sidebar header with close ──
        st.markdown(
            '<div class="zb-sidebar-header">'
            '<span class="zb-header-icon">&#127828;</span>'
            f'<span class="zb-header-name">{PLATFORM_NAME} AI</span>'
            '<button class="zb-sidebar-close" data-zb-action="close" aria-label="Close sidebar">&#10005;</button>'
            '</div>',
            unsafe_allow_html=True,
        )

        # ── Conversations ──
        st.markdown(
            "<p class='zb-section-label'>&#128195; Conversations</p>",
            unsafe_allow_html=True,
        )

        search_query = st.text_input(
            "Search conversations",
            value=st.session_state.get("search_query", ""),
            placeholder="Find a chat...",
            label_visibility="collapsed",
            key="conv_search_input",
        )
        if search_query != st.session_state.get("search_query", ""):
            st.session_state.search_query = search_query
            st.rerun()

        if search_query:
            results = search_conversations(search_query)
            if results:
                for conv_id, conv in results:
                    _render_conversation_item(conv_id, conv)
            else:
                st.markdown("<div class='zb-no-convs'>No chats found</div>", unsafe_allow_html=True)
        else:
            fav_only = st.session_state.get("sidebar_favs", False)
            favs: set = st.session_state.setdefault("favorites", set())
            if st.button(("🗂️ Showing favorites" if fav_only else "❤️ Favorites"),
                         key="fav_filter", use_container_width=True):
                st.session_state.sidebar_favs = not fav_only
                st.rerun()
            if fav_only and not favs:
                st.markdown(
                    "<div class='zb-no-convs'>No favorites yet — open the ☰ menu and tap ❤️ Favorites.</div>",
                    unsafe_allow_html=True,
                )
            groups = get_conversation_groups()
            has_any = False
            for group_name in ["Today", "Yesterday", "Previous 7 Days", "Older"]:
                items = groups[group_name]
                if fav_only:
                    items = [it for it in items if it[0] in favs]
                if items:
                    has_any = True
                    st.markdown(f"<span class='zb-conv-group-label'>{group_name}</span>", unsafe_allow_html=True)
                    for conv_id, conv in items:
                        _render_conversation_item(conv_id, conv)
            if not has_any:
                st.markdown("<div class='zb-no-convs'>No chats yet — ask me something!</div>", unsafe_allow_html=True)

        _divider()

        # ── Actions ──
        st.markdown(
            "<p class='zb-section-label'>&#9881;&#65039; Actions</p>",
            unsafe_allow_html=True,
        )
        if st.button("\U0001F4C4 New Chat", use_container_width=True, help="Save current chat and start fresh"):
            start_new_conversation()
            st.rerun()

        _divider()

        # ── Quick Tips ──
        st.markdown(
            "<p class='zb-section-label'>&#128161; Tips</p>",
            unsafe_allow_html=True,
        )
        tips = [
            ("&#127831;", "Ask about any dish — price & rating!"),
            ("&#128661;", "Share a <b>ZB-XXXX</b> code to track an order"),
            ("&#10024;", "Ask for <b>combo deals</b> to save more"),
            ("&#128172;", "Curious about <b>delivery fees</b>?"),
        ]
        tip_html = '<div class="zb-tips" style="display:flex;flex-direction:column;gap:2px;">'
        for icon, text in tips:
            tip_html += (
                f'<div class="zb-tip-item">'
                f'<span class="zb-tip-icon">{icon}</span>'
                f'<span>{text}</span>'
                f'</div>'
            )
        tip_html += '</div>'
        st.markdown(tip_html, unsafe_allow_html=True)

        _divider()

        # ── Text Scale ──
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
            help="Adjust global text size.",
            label_visibility="collapsed",
        )

        # Keyboard shortcut hint
        st.markdown(
            '<div class="zb-kbd-hint">'
            '<kbd>Ctrl</kbd>+<kbd>K</kbd> Jump to chat &middot; '
            '<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> Search &middot; '
            '<kbd>Esc</kbd> Close menu'
            '</div>',
            unsafe_allow_html=True
        )


def _render_conversation_item(conv_id: str, conv: Conversation) -> None:
    is_active = conv_id == st.session_state.current_conv_id
    active_cls = " active" if is_active else ""

    delta = datetime.now() - conv.updated_at
    if delta.total_seconds() < 60:
        time_ago = "just now"
    elif delta.total_seconds() < 3600:
        time_ago = f"{int(delta.total_seconds() // 60)}m ago"
    elif delta.total_seconds() < 86400:
        time_ago = f"{int(delta.total_seconds() // 3600)}h ago"
    else:
        time_ago = f"{int(delta.total_seconds() // 86400)}d ago"

    is_renaming = st.session_state.get("renaming_conv") == conv_id

    st.markdown(
        f"""
        <div class="zb-conv-item{active_cls}">
            <span class="zb-conv-title-text">{conv.title}</span>
            <div class="zb-conv-meta">
                <span>{time_ago}</span>
                <span>{conv.message_count} msgs</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns([1, 1, 1, 2])
    with cols[0]:
        if st.button("\u25B6", key=f"load_{conv_id}", help="Load conversation"):
            save_current_conversation()
            load_conversation(conv_id)
            st.rerun()
    with cols[1]:
        if st.button("\u270E", key=f"rename_{conv_id}", help="Rename"):
            st.session_state.renaming_conv = conv_id
            st.rerun()
    with cols[2]:
        if st.button("\u2715", key=f"delete_{conv_id}", help="Delete"):
            if conv_id in st.session_state.conversations:
                del st.session_state.conversations[conv_id]
                if conv_id == st.session_state.current_conv_id:
                    start_new_conversation()
                st.rerun()

    if is_renaming:
        new_title = st.text_input(
            "Rename",
            value=conv.title,
            key=f"rename_input_{conv_id}",
            label_visibility="collapsed",
        )
        save_col, cancel_col = st.columns([1, 1])
        with save_col:
            if st.button("Save", key=f"rename_save_{conv_id}"):
                rename_conversation(conv_id, new_title)
                st.session_state.renaming_conv = None
                st.rerun()
        with cancel_col:
            if st.button("Cancel", key=f"rename_cancel_{conv_id}"):
                st.session_state.renaming_conv = None
                st.rerun()


# ──────────────────────────────────────────────────────────
# PREMIUM HEADER — native nav buttons + drawers
# ──────────────────────────────────────────────────────────

MENU_ITEMS: list = [
    ("🏠", "Home", "menu_home", "home"),
    ("💬", "New Chat", "menu_new", "new"),
    ("📝", "Conversation Summary", "menu_summary", "summary"),
    ("❤️", "Favorites", "menu_fav", "favorites"),
    ("🍕", "Browse Menu", "menu_browse", "browse"),
    ("🛵", "Track Orders", "menu_orders", "orders"),
    ("🎁", "Offers", "menu_offers", "offers"),
    ("⭐", "Recommended Meals", "menu_reco", "recommended"),
    ("🎨", "Theme", "menu_dark", "dark"),
    ("❓", "Help", "menu_help", "help"),
    ("ℹ️", "About", "menu_about", "about"),
]

QUICK_ITEMS: list[tuple[str, str, str]] = [
    ("🍔", "Burgers", "Show me all burgers with prices, ratings and customisation options"),
    ("🍕", "Pizza", "List all pizzas available today with prices, ratings and customisation choices"),
    ("🍗", "Chicken", "Which broasted chicken choices have a perfect 5-star rating, and what do they cost?"),
    ("🌯", "Shawarma", "Show me the shawarma options with prices and ratings"),
    ("🍚", "Biryani", "What biryani options are available with prices and ratings?"),
    ("🥤", "Drinks", "What drinks, mojitos and sodas do you have?"),
    ("🍰", "Desserts", "Do you have any desserts or sweet options?"),
    ("⭐", "Today's Specials", "What are today's specials and top rated meals?"),
    ("🛵", "Track Order", "How do I track my live order? Walk me through it."),
    ("💳", "Payment", "What payment methods do you accept?"),
    ("🧾", "Order History", "Can you show my order history?"),
    ("📍", "Nearest Branch", "Where is the nearest ZingyByte branch?"),
    ("🎁", "Coupons", "Are there any coupons or promo codes available?"),
    ("💬", "Support", "I need help placing my order"),
]

_MENU_QUERIES: dict = {
    "browse": "Show me the full menu with prices and ratings",
    "orders": "How can I track my orders? Walk me through it with an example ZB-XXXX code",
    "offers": "Are there any current offers or combo deals?",
    "recommended": "What are the most recommended meals today?",
    "help": "What can you help me with?",
}


def _init_nav_state() -> None:
    for key, default in (
        ("show_menu", False), ("show_panel", False), ("open_sidebar", False),
        ("theme", "dark"), ("favorites", set()),
    ):
        if key not in st.session_state:
            st.session_state[key] = default
    # Desktop keeps the sidebar open at load (one-shot); mobile starts closed
    if not st.session_state.get("is_mobile") and not st.session_state.get("_sidebar_initialized"):
        st.session_state.open_sidebar = True
        st.session_state._sidebar_initialized = True


def _close_overlays() -> None:
    st.session_state.show_menu = False
    st.session_state.show_panel = False


def _inject_theme_flash() -> None:
    """Flip the body class instantly on tap — before the rerun's body-state sync."""
    orange = st.session_state.get("theme", "dark") == "orange"
    st.markdown(
        f"""
        <script>
        (function() {{
            document.body.classList.toggle('theme-orange', {"true" if orange else "false"});
            document.body.classList.toggle('theme-light', false);
        }})();
        </script>
        """,
        unsafe_allow_html=True,
    )


def _handle_menu_action(action: str) -> None:
    _close_overlays()
    if action in ("home", "new"):
        start_new_conversation()
        st.rerun()
        return
    if action == "summary":
        if st.session_state.get("messages"):
            st.session_state.input_injection = "Can you give me a quick summary of our conversation so far?"
        else:
            st.toast("No active conversation to summarize yet! 🍔")
        st.rerun()
        return
    if action == "favorites":
        st.session_state.input_injection = "Show my favorite dishes"
        st.rerun()
        return
    if action == "dark":
        current = st.session_state.get("theme", "dark")
        st.session_state.theme = "orange" if current == "dark" else "dark"
        st.toast("🍊 Orange theme on" if st.session_state.theme == "orange" else "🌙 Dark theme on")
        _inject_theme_flash()
        st.rerun()
        return
    if action == "about":
        st.session_state.show_about_dialog = True
        st.rerun()
        return
    query = _MENU_QUERIES.get(action)
    if query:
        st.session_state.input_injection = query
        st.rerun()


def _render_drawer(side: str) -> None:
    """Premium slide-in drawer. Items are REAL Streamlit buttons."""
    if side == "menu":
        anchor, backdrop_key, title, sub = "zb-menu-anchor", "zb_backdrop_menu", "Menu", "Home · menu · help"
        items = MENU_ITEMS
        cols = st.columns([2, 3])
        panel_col = cols[0]
    else:
        anchor, backdrop_key, title, sub = "zb-panel-anchor", "zb_backdrop_panel", "Quick Actions", "Order your craving"
        items = QUICK_ITEMS
        cols = st.columns([3, 2])
        panel_col = cols[1]

    # Full-screen native backdrop — tap closes the drawer via a real rerun
    if st.button(" ", key=backdrop_key, help="Close"):
        _close_overlays()
        st.rerun()

    with panel_col:
        st.markdown(f'<div class="{anchor}"></div>', unsafe_allow_html=True)
        head_cols = st.columns([5, 1])
        with head_cols[0]:
            st.markdown(
                f'<div class="zb-drawer-head"><span class="zb-drawer-title">{title}</span>'
                f'<span class="zb-drawer-sub">{sub}</span></div>',
                unsafe_allow_html=True,
            )
        with head_cols[1]:
            if st.button("✕", key=f"{side}_close", help="Close"):
                _close_overlays()
                st.rerun()

        if side == "menu":
            dark = st.session_state.get("theme", "dark") == "dark"
            for icon, label, key, action in MENU_ITEMS:
                label_text = f"{icon} {label}"
                if key == "menu_dark":
                    label_text = ("🌙 Dark Mode" if not dark else "🍊 Orange Theme")
                if st.button(label_text, key=key, use_container_width=True):
                    _handle_menu_action(action)
        else:
            for icon, label, query in QUICK_ITEMS:
                chip_key = f"qa_{label.lower().replace(' ', '_').replace(chr(39), '').replace(chr(46), '_')}"
                if st.button(f"{icon} {label}", key=chip_key, use_container_width=True):
                    _close_overlays()
                    st.session_state.input_injection = query
                    st.rerun()

        st.markdown('<div class="zb-drawer-foot">Esc or tap outside to close</div>', unsafe_allow_html=True)


def _inject_body_state(dialog_open: bool = False) -> None:
    """Keep the DOM <body> classes in sync with Python session state (rerun-safe)."""
    has_chat = "true" if st.session_state.get("messages") else "false"
    drawer = ("true" if (st.session_state.get("show_menu") or st.session_state.get("show_panel"))
              else "false")
    sidebar_open = "true" if st.session_state.get("open_sidebar") else "false"
    orange = "true" if st.session_state.get("theme", "dark") == "orange" else "false"
    st.session_state.open_sidebar = False  # one-shot — closing remains class driven
    st.markdown(
        f"""
        <script>
        (function() {{
            document.body.classList.toggle('has-chat', {has_chat});
            document.body.classList.toggle('drawer-open', {drawer});
            document.body.classList.toggle('dialog-open', {dialog_open});
            document.body.classList.toggle('theme-light', false);
            document.body.classList.toggle('theme-orange', {orange});
            /* Sidebar class: honor Python's explicit open, otherwise mirror the
               sidebar's REAL geometry so reruns never fight the JS close/open */
            if ({sidebar_open}) {{
                document.body.classList.add('sidebar-open');
                if (window.__zbSidebarFreeze) window.__zbSidebarFreeze(500);
            }} else {{
                var __zbSB = document.querySelector('[data-testid="stSidebar"]');
                if (__zbSB) {{
                    var __zbR = __zbSB.getBoundingClientRect();
                    if (!(__zbR.right > __zbR.width * 0.2)) {{
                        document.body.classList.remove('sidebar-open');
                    }}
                }}
            }}
        }})();
        </script>
        """,
        unsafe_allow_html=True,
    )


def render_top_bar() -> None:
    """Premium sticky header: native ☰ menu, brand, native ✦ quick actions."""
    _init_nav_state()
    cols = st.columns([1, 4, 1])
    with cols[0]:
        if st.button("☰", key="zb_btn_menu", help="Open menu"):
            st.session_state.show_menu = not st.session_state.get("show_menu", False)
            st.session_state.show_panel = False
            st.rerun()
    with cols[1]:
        st.markdown(
            '<div class="zb-header-brand zb-header-anchor">'
            '<span class="zb-header-icon">&#127828;</span>'
            '<span class="zb-header-name">ZingyByte AI</span>'
            '<span class="zb-header-sep"></span>'
            '<span class="zb-header-status">Online</span>'
            '</div>',
            unsafe_allow_html=True,
        )
    with cols[2]:
        if st.button("✦", key="zb_btn_panel", help="Quick actions"):
            st.session_state.show_panel = not st.session_state.get("show_panel", False)
            st.session_state.show_menu = False
            st.rerun()

    # Sidebar reopen tab — fixed top-left, visible only while the sidebar is closed
    st.markdown(
        '<button class="zb-sidebar-reopen" data-zb-action="open-sidebar" aria-label="Open sidebar" title="Open sidebar">&#9776;</button>',
        unsafe_allow_html=True,
    )

    if st.session_state.get("show_menu"):
        _render_drawer("menu")
    if st.session_state.get("show_panel"):
        _render_drawer("panel")

    dialog_open = st.session_state.get("show_about_dialog", False)
    if dialog_open:
        render_about_modal()
        st.session_state.show_about_dialog = False

    _inject_body_state(dialog_open=dialog_open)


@st.dialog("About ZingyByte AI")
def render_about_modal() -> None:
    """Glassmorphic About dialog — explains the app in plain, friendly English."""
    st.markdown(
        """
        ### 🍔 ZingyByte AI v2.0 — Virtual Food Concierge

        #### 🚀 Smart Technology Under the Hood
        * **Lightning-Fast AI:** Powered by advanced tech to give you instant, smart responses without the wait.
        * **Accurate Menu Search:** Our system reads the actual menu, ensuring you get 100% real prices, ingredients, and dietary info—no guesswork.
        * **Natural Conversations:** The AI remembers your chat and replies in real-time, just like texting a friend.

        #### ✨ App Features You'll Love
        * **🛵 Live Order Tracking:** Keep an eye on your food's journey in real-time using your unique order code (like ZB-9874).
        * **❤️ Smart Favorites:** Just tell the AI what you loved, and it will remember your favorite dishes for next time.
        * **🎨 Sleek & Modern Design:** Enjoy a beautiful, easy-on-the-eyes dark interface with frosted glass effects.

        ---
        *Crafted for effortless food discovery. Tap anywhere outside or press Esc to return to chat.*
        """,
        unsafe_allow_html=True,
    )
    if st.button("⬅️ Back to Chat", use_container_width=True):
        st.session_state.show_about_dialog = False
        st.rerun()


# ──────────────────────────────────────────────────────────
# EMPTY STATE / HERO + CHIPS
# ──────────────────────────────────────────────────────────

def render_empty_state_screen() -> None:
    st.markdown(
        """
        <div class="zb-hero">
            <span class="zb-hero-icon">&#127828;</span>
            <h1 class="zb-hero-title">Welcome to ZingyByte AI <span class="zb-native-emoji">&#127828;&#10024;</span></h1>
            <p class="zb-hero-sub">Your personal food concierge. Ask about menus, prices, ratings, or track your live orders!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Adaptive chip grid — full-width pills on narrow containers, auto-flow row on
    # Adaptive chip grid — 2 columns of pills on mobile, one row on desktop
    n_cols = 2 if _is_mobile() else len(SUGGESTED_PROMPTS)
    cols = st.columns(n_cols)
    for idx, card in enumerate(SUGGESTED_PROMPTS):
        parts = card["label"].split(" ", 1)
        emoji = parts[0] if parts else "🍔"
        label = parts[1] if len(parts) > 1 else card["label"]
        with cols[idx % n_cols]:
            if idx == 0:
                st.markdown('<div class="zb-chips-anchor"></div>', unsafe_allow_html=True)
            if st.button(f"{emoji} {label}", key=f"chip_{idx}"):
                st.session_state.input_injection = card["query"]
                st.rerun()


# ──────────────────────────────────────────────────────────
# CHAT BUBBLE RENDERER
# ──────────────────────────────────────────────────────────

def render_chat_bubble(role: str, content: str) -> None:
    stamp = datetime.now().strftime("%I:%M %p")
    with st.chat_message(role):
        st.markdown(content)
        st.markdown(f'<div class="zb-ts">{stamp}</div>', unsafe_allow_html=True)


def render_typing_indicator() -> str:
    """HTML for the ChatGPT-style 'thinking' pill shown while streaming."""
    return (
        '<div class="zb-typing" aria-label="ZingyByte is typing">'
        '<span class="zb-typing-dot"></span>'
        '<span class="zb-typing-dot"></span>'
        '<span class="zb-typing-dot"></span>'
        '</div>'
    )


def _render_bubble_actions(idx: int, content: str) -> None:
    """Feedback row: like / dislike with an instant status indicator.

    Button labels stay static because Streamlit 1.48's frontend does not
    re-render `st.button` labels after a rerun; the selection state is shown
    by a markdown indicator computed AFTER the click handlers run, so it
    reflects the click in the very same frame as the toast.
    """
    feedback = st.session_state.setdefault("msg_feedback", {})
    current = feedback.get(idx, 0)

    cols = st.columns([1, 1, 3])
    with cols[0]:
        liked = st.button("👍", key=f"like_{idx}")
    with cols[1]:
        disliked = st.button("👎", key=f"dislike_{idx}")

    if liked:
        feedback[idx] = 0 if current == 1 else 1
        st.toast("Thanks for the feedback! ❤️" if current != 1 else "Feedback removed")
    elif disliked:
        feedback[idx] = 0 if current == -1 else -1
        st.toast("Feedback noted — we'll improve! 👍" if current != -1 else "Feedback removed")

    with cols[2]:
        now = feedback.get(idx, 0)
        status = "❤️ Liked" if now == 1 else ("💔 Disliked" if now == -1 else "")
        st.markdown(
            f'<span class="zb-fb-status">{status}</span>',
            unsafe_allow_html=True,
        )


def render_followup_questions(suggestions: list) -> None:
    if not suggestions:
        return
    st.markdown(
        '<div class="zb-followup"><span class="zb-followup-label">&#128161; Try asking</span></div>',
        unsafe_allow_html=True,
    )
    n_cols = 1 if _is_mobile() else 2
    cols = st.columns(n_cols)
    for i, suggestion in enumerate(suggestions):
        with cols[i % n_cols]:
            if i == 0:
                st.markdown('<div class="zb-fu-anchor"></div>', unsafe_allow_html=True)
            if st.button(suggestion, key=f"fu_{i}", use_container_width=True):
                st.session_state.input_injection = suggestion
                st.rerun()


def render_active_chat_bubbles() -> None:
    for i, message in enumerate(st.session_state.messages):
        render_chat_bubble(message["role"], message["content"])
        if message["role"] == "assistant":
            _render_bubble_actions(i, message["content"])

    if st.session_state.messages:
        last_msg = st.session_state.messages[-1]
        if last_msg["role"] == "assistant":
            last_content = last_msg["content"]
            last_user = ""
            for msg in reversed(st.session_state.messages):
                if msg["role"] == "user":
                    last_user = msg["content"]
                    break
            from prompt import generate_followup_suggestions
            suggestions = generate_followup_suggestions(last_user, last_content)
            render_followup_questions(suggestions)

    # ── Precision auto-scroll to the last chat bubble ──
    st.markdown(
        """
        <script>
            (function() {
                function scrollToLatestMessage() {
                    const messages = document.querySelectorAll('.stChatMessage');
                    if (messages.length > 0) {
                        const lastMessage = messages[messages.length - 1];
                        lastMessage.scrollIntoView({ behavior: 'smooth', block: 'end' });
                    }
                    const mainContainer = document.querySelector('section.main') || document.querySelector('.main');
                    if (mainContainer) {
                        mainContainer.scrollTop = mainContainer.scrollHeight;
                    }
                }

                scrollToLatestMessage();
                setTimeout(scrollToLatestMessage, 100);
                setTimeout(scrollToLatestMessage, 350);

                if (window.__zbScrollObserver) {
                    window.__zbScrollObserver.disconnect();
                }
                const targetContainer = document.querySelector('section.main') || document.body;
                if (targetContainer && 'MutationObserver' in window) {
                    let isUserScrollingUp = false;
                    targetContainer.addEventListener('scroll', function() {
                        isUserScrollingUp = targetContainer.scrollHeight - targetContainer.scrollTop - targetContainer.clientHeight > 200;
                    }, { passive: true });

                    const observer = new MutationObserver(function() {
                        if (!isUserScrollingUp) {
                            scrollToLatestMessage();
                        }
                    });
                    observer.observe(targetContainer, { childList: true, subtree: true, characterData: true });
                    window.__zbScrollObserver = observer;
                }
            })();
        </script>
        """,
        unsafe_allow_html=True,
    )
