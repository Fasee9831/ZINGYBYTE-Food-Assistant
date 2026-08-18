"""Premium dark-glassmorphic UI system for ZingyByte AI — styles, animations, layout."""

import streamlit as st


def inject_premium_styles() -> None:
    """Injects the full ZingyByte design-system CSS into the Streamlit page."""
    font_size = st.session_state.get("ui_font_size", 15)

    st.markdown(
        f"""
        <style>
        /* ==========================================================================
           PREMIUM DESIGN SYSTEM — Variables, Reset, Typography
           ========================================================================== */

        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        :root {{
            /* ── Colors ─────────────────────────────── */
            --bg-deep          : #0A0A0A;
            --bg-surface       : rgba(255,255,255,0.02);
            --bg-card          : rgba(255,255,255,0.03);
            --bg-elevated      : rgba(255,255,255,0.05);
            --bg-hover         : rgba(255,255,255,0.08);
            --border-subtle    : rgba(255,255,255,0.05);
            --border-light     : rgba(255,255,255,0.08);
            --border-medium    : rgba(255,255,255,0.12);
            --text-primary     : #F0F0F0;
            --text-secondary   : rgba(240,240,240,0.55);
            --text-tertiary    : rgba(240,240,240,0.32);
            --brand            : #FF8533;
            --brand-glow       : rgba(255,133,51,0.25);
            --green            : #10A37F;
            --green-glow       : rgba(16,163,127,0.5);

            /* ── Typography ──────────────────────────── */
            --font-sans        : 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono        : 'SFMono-Regular', 'Cascadia Code', 'Consolas', monospace;

            --fs-hero          : clamp(1.85rem, 0.85rem + 4vw, 3.25rem);
            --fs-heading       : clamp(1rem, 0.8rem + 1.25vw, 1.2rem);
            --fs-body          : clamp(0.8125rem, 0.78rem + 0.6vw, 0.9375rem);
            --fs-small         : clamp(0.6875rem, 0.6875rem + 0.3vw, 0.75rem);
            --fs-xs            : clamp(0.5625rem, 0.5625rem + 0.2vw, 0.625rem);
            --fs-caption       : 0.625rem;

            --lh-none          : 1;
            --lh-tight         : 1.2;
            --lh-normal        : 1.5;
            --lh-relaxed       : 1.6;

            --fw-normal        : 400;
            --fw-medium        : 500;
            --fw-semibold      : 600;
            --fw-bold          : 700;
            --fw-extrabold     : 800;

            /* ── Spacing (8px grid) ──────────────────── */
            --space-1          : 4px;
            --space-2          : 8px;
            --space-3          : 12px;
            --space-4          : 16px;
            --space-5          : 20px;
            --space-6          : 24px;
            --space-8          : 32px;
            --space-10         : 40px;
            --space-12         : 48px;

            /* ── Radii ───────────────────────────────── */
            --radius-sm        : 6px;
            --radius-md        : 10px;
            --radius-lg        : 16px;
            --radius-xl        : 20px;
            --radius-full      : 9999px;

            /* ── Shadows ─────────────────────────────── */
            --shadow-sm        : 0 1px 2px rgba(0,0,0,0.3);
            --shadow-md        : 0 4px 12px rgba(0,0,0,0.2);
            --shadow-lg        : 0 8px 24px rgba(0,0,0,0.25);
            --shadow-xl        : 0 16px 48px rgba(0,0,0,0.35);

            /* ── Layout ──────────────────────────────── */
            --sidebar-width    : 300px;
            --header-height    : 60px;
            --header-total     : calc(var(--safe-top) + var(--header-height));
            --content-max      : 900px;
            --radius           : 20px;
            --safe-bottom      : env(safe-area-inset-bottom, 0px);
            --safe-top         : env(safe-area-inset-top, 0px);

            /* ── Responsive padding tokens ───────────── */
            --pad-xs           : 6px;
            --pad-sm           : 10px;
            --pad-md           : 18px;
            --pad-lg           : 28px;

            /* ── Transitions ─────────────────────────── */
            --ease-out         : cubic-bezier(0.16, 1, 0.3, 1);
            --ease-smooth      : cubic-bezier(0.65, 0, 0.35, 1);
            --transition-fast  : 0.15s var(--ease-out);
            --transition-base  : 0.25s var(--ease-out);
            --transition-slow  : 0.4s var(--ease-out);
        }}

        /* ── Base Reset ── */
        html, body {{
            background: var(--bg-deep) !important;
            color: var(--text-primary) !important;
            font-family: var(--font-sans) !important;
            font-size: {font_size}px !important;
            line-height: var(--lh-relaxed);
            margin: 0; padding: 0;
            overflow-x: hidden !important;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-rendering: optimizeLegibility;
        }}

        html, body, .main, [data-testid="stAppViewContainer"] {{
            width: 100% !important;
            max-width: 100vw !important;
            overflow-x: hidden !important;
            scroll-behavior: smooth !important;
        }}

        *, *::before, *::after {{
            box-sizing: border-box;
        }}

        ::selection {{
            background: var(--brand-glow);
            color: var(--text-primary);
        }}

        button, input, textarea {{
            font-family: var(--font-sans);
        }}

        /* ── Perfect icon & label centering across every button ── */
        .stButton > button,
        [data-testid="stButton"] > button {{
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            vertical-align: middle !important;
            gap: 6px !important;
        }}
        .stButton > button svg,
        [data-testid="stButton"] > button svg {{
            flex-shrink: 0 !important;
            vertical-align: middle !important;
        }}
        [data-testid="stButton"] > button > span {{
            display: inline-flex !important;
            align-items: center !important;
            min-height: 0 !important;
        }}

        /* ── Hide Streamlit chrome — top accent line, header, toolbar, footer, menu ── */
        [data-testid="stDecoration"],
        #MainMenu, footer, header[data-testid="stHeader"], [data-testid="stToolbar"] {{
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            pointer-events: none !important;
        }}

        /* ── Hide native top progress & status line ── */
        div[data-baseweb="progress-bar"],
        [data-testid="stProgress"],
        .stProgress,
        div[class*="stAppProgress"],
        [data-testid="stStatusWidget"] {{
            display: none !important;
            visibility: hidden !important;
        }}

        /* ── Hide Streamlit's hover action toolbar ── */
        [data-testid="stElementToolbar"],
        [data-testid="stElementToolbarButton"] {{
            display: none !important;
            opacity: 0 !important;
            visibility: hidden !important;
            pointer-events: none !important;
        }}

        /* ── Absolute blanket ban on text selection ── */
        * {{
            -webkit-user-select: none !important;
            -moz-user-select: none !important;
            -ms-user-select: none !important;
            user-select: none !important;
        }}
        *::selection {{
            background: transparent !important;
            color: inherit !important;
        }}
        *::-moz-selection {{
            background: transparent !important;
            color: inherit !important;
        }}
        /* Keep the chat input editable — text entry must stay selectable */
        input, textarea, [contenteditable="true"] {{
            -webkit-user-select: text !important;
            -moz-user-select: text !important;
            -ms-user-select: text !important;
            user-select: text !important;
        }}
        input::selection, textarea::selection {{
            background: rgba(255,133,51,0.35) !important;
            color: inherit !important;
        }}

        /* ── Hide native close buttons and ghost tooltips ── */
        button[title="Close"],
        button[aria-label="Close"],
        [data-testid="stSidebarCloseButton"],
        button[kind="headerNoPadding"] {{
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            pointer-events: none !important;
            width: 0 !important;
            height: 0 !important;
        }}

        .stApp {{
            background: var(--bg-deep) !important;
        }}

            /* ── Main container (offset for header + sidebar) ── */
            .main .block-container, [data-testid="stMainBlockContainer"] {{
                max-width: var(--content-max) !important;
                padding: calc(var(--header-height) + 20px) var(--pad-lg) 170px var(--pad-lg) !important;
                margin: 0 auto !important;
                position: relative;
                z-index: 1;
                width: 100%;
            }}

        /* ── Seamless responsive gutters: desktop sidebar offset → tablet → mobile drawer ── */
        @media (min-width: 768px) {{
            body.sidebar-open .main .block-container,
            body.sidebar-open [data-testid="stMainBlockContainer"] {{
                padding-left: calc(var(--sidebar-width) + var(--pad-lg)) !important;
                padding-right: var(--pad-lg) !important;
                padding-bottom: 168px !important;
                max-width: var(--content-max) !important;
            }}
        }}

        @media (max-width: 1024px) {{
            .main .block-container, [data-testid="stMainBlockContainer"] {{
                padding-top: calc(var(--header-height) + 20px) !important;
                padding-left: var(--pad-md) !important;
                padding-right: var(--pad-md) !important;
                padding-bottom: 162px !important;
            }}
        }}

        @media (max-width: 768px) {{
            .main .block-container, [data-testid="stMainBlockContainer"] {{
                padding-left: var(--pad-md) !important;
                padding-right: var(--pad-md) !important;
                padding-bottom: max(165px, 18vh) !important;
            }}
        }}

        @media (max-width: 480px) {{
            .main .block-container, [data-testid="stMainBlockContainer"] {{
                padding: calc(var(--header-total) + var(--pad-md)) var(--pad-md) 165px var(--pad-md) !important;
            }}
        }}

        .stApp > div:first-child > div:first-child > div:first-child > div:first-child {{
            background: transparent !important;
        }}

        /* ── Prevent text highlighting and tap flashing on interactive elements ── */
        button,
        .stButton > button,
        .zb-chat-action-btn,
        .zb-conv-item,
        .zb-food-item {{
            user-select: none !important;
            -webkit-user-select: none !important;
            -moz-user-select: none !important;
            -webkit-tap-highlight-color: transparent !important;
        }}

        /* ==========================================================================
           FROZEN: Untouched Background & Floating Logic
           ========================================================================== */
        @keyframes drift1 {{
            0%,100% {{ transform: translate(0px, 0px) rotate(0deg) scale(1); }}
            25% {{ transform: translate(12px,-18px) rotate(8deg) scale(1.04); }}
            50% {{ transform: translate(6px, -32px) rotate(-4deg) scale(0.97); }}
            75% {{ transform: translate(-8px,-14px) rotate(10deg) scale(1.02); }}
        }}
        @keyframes drift2 {{
            0%,100% {{ transform: translate(0px, 0px) rotate(0deg) scale(1); }}
            30% {{ transform: translate(-14px,-20px) rotate(-9deg) scale(1.05); }}
            60% {{ transform: translate(8px, -28px) rotate(5deg) scale(0.96); }}
            80% {{ transform: translate(-5px,-10px) rotate(-3deg) scale(1.03); }}
        }}
        @keyframes drift3 {{
            0%,100% {{ transform: translate(0px, 0px) rotate(0deg) scale(1); }}
            20% {{ transform: translate(16px,-10px) rotate(12deg) scale(1.04); }}
            55% {{ transform: translate(-10px,-25px) rotate(-6deg) scale(0.98); }}
            80% {{ transform: translate(5px, -8px) rotate(8deg) scale(1.02); }}
        }}
        @keyframes drift4 {{
            0%,100% {{ transform: translate(0px, 0px) rotate(0deg) scale(1); }}
            35% {{ transform: translate(-18px,-15px) rotate(-10deg) scale(1.06); }}
            65% {{ transform: translate(10px,-22px) rotate(7deg) scale(0.95); }}
        }}
        @keyframes drift5 {{
            0%,100% {{ transform: translate(0px, 0px) rotate(0deg) scale(1); }}
            40% {{ transform: translate(20px,-18px) rotate(-14deg) scale(1.05); }}
            70% {{ transform: translate(-6px,-30px) rotate(6deg) scale(0.97); }}
        }}
        @keyframes hoverGlow {{
            0%,100% {{ filter: drop-shadow(0 0 8px rgba(255,133,51,0.4)); }}
            50% {{ filter: drop-shadow(0 0 20px rgba(255,75,75,0.7)); }}
        }}

        .zb-food-bg {{
            position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden;
        }}
        .zb-food-item {{
            position: absolute; font-size: 3.4rem; opacity: 0.045;
            transition: opacity 0.6s ease, filter 0.6s ease, transform 0.4s ease;
            user-select: none; will-change: transform;
        }}
        .zb-food-item:nth-child(1)  {{ top: 6%; left: 4%; animation: drift1 9s ease-in-out infinite; }}
        .zb-food-item:nth-child(2)  {{ top: 12%; right: 6%; animation: drift2 11s ease-in-out infinite 1.2s; }}
        .zb-food-item:nth-child(3)  {{ top: 35%; left: 2%; animation: drift3 13s ease-in-out infinite 2.5s; }}
        .zb-food-item:nth-child(4)  {{ top: 55%; right: 3%; animation: drift4 10s ease-in-out infinite 0.8s; }}
        .zb-food-item:nth-child(5)  {{ top: 72%; left: 5%; animation: drift5 12s ease-in-out infinite 3.2s; }}
        .zb-food-item:nth-child(6)  {{ top: 85%; right: 7%; animation: drift1 14s ease-in-out infinite 1.8s; }}
        .zb-food-item:nth-child(7)  {{ top: 22%; left: 48%; animation: drift2 10s ease-in-out infinite 4.0s; }}
        .zb-food-item:nth-child(8)  {{ top: 60%; left: 44%; animation: drift3 8s ease-in-out infinite 0.5s; }}
        .zb-food-item:nth-child(9)  {{ top: 40%; right:48%; animation: drift4 15s ease-in-out infinite 2.0s; }}
        .zb-food-item:nth-child(10) {{ top: 90%; left: 30%; animation: drift5 11s ease-in-out infinite 3.8s; }}
        .zb-food-item:nth-child(11) {{ top: 3%; left: 60%; animation: drift1 13s ease-in-out infinite 1.0s; }}
        .zb-food-item:nth-child(12) {{ top: 78%; right:40%; animation: drift2 9s ease-in-out infinite 2.8s; }}

        body:hover .zb-food-item {{ opacity: 0.10; }}
        .zb-food-item:hover {{
            opacity: 0.55 !important;
            filter: drop-shadow(0 0 18px rgba(255,133,51,0.65)) !important;
            transform: scale(1.35) !important;
            z-index: 1; pointer-events: all !important;
            animation: hoverGlow 1.2s ease-in-out infinite !important;
        }}

        /* ==========================================================================
           PREMIUM HEADER — single-row glass bar
           ========================================================================== */

        @keyframes headerSlide {{
            from {{ transform: translateY(-100%); opacity: 0; }}
            to {{ transform: translateY(0); opacity: 1; }}
        }}

        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            z-index: 99999 !important;
            pointer-events: auto !important;
            height: var(--header-total) !important;
            min-height: var(--header-total) !important;
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            justify-content: space-between !important;
            align-items: center !important;
            gap: 0 !important;
            padding: var(--safe-top) var(--space-3) 0 var(--space-3) !important;
            background: rgba(10,10,10,0.85) !important;
            backdrop-filter: blur(24px) saturate(1.4) !important;
            -webkit-backdrop-filter: blur(24px) saturate(1.4) !important;
            border-bottom: 1px solid var(--border-light) !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4) !important;
            animation: headerSlide 0.3s var(--ease-out) both;
        }}
        /* Force all children inside the header to be fully interactive */
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) *,
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) button,
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) div {{
            pointer-events: auto !important;
            cursor: pointer !important;
        }}
        /* Column children — non-shrinking, optically centered, never clipped */
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div {{
            padding: 0 3px !important;
            display: flex !important;
            align-items: center !important;
            flex-shrink: 0 !important;
            min-height: var(--header-height);
            pointer-events: auto !important;
            overflow: visible !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:first-child {{
            padding-left: 0 !important;
            flex: 0 0 auto !important;
            justify-content: flex-start !important;
        }}
        /* Brand column — trims inward to share space, never squashes its neighbors */
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:nth-child(2) {{
            flex: 1 1 0% !important;
            min-width: 0 !important;
            justify-content: flex-start !important;
            overflow: visible !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:nth-child(3),
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:nth-child(4) {{
            flex: 0 0 auto !important;
            width: auto !important;
            justify-content: flex-end !important;
            overflow: visible !important;
        }}

        @media (min-width: 768px) {{
            body.sidebar-open [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
                left: var(--sidebar-width) !important;
                padding: var(--safe-top) var(--space-5) 0 var(--space-5) !important;
            }}
        }}

        @media (min-width: 1200px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
                padding: var(--safe-top) var(--space-6) 0 var(--space-6) !important;
            }}
        }}

        /* Mobile top bar — strict single-line, no vertical stacking */
        @media (max-width: 640px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
                flex-direction: row !important;
                flex-wrap: nowrap !important;
                height: var(--header-total) !important;
                min-height: var(--header-total) !important;
                align-items: center !important;
                justify-content: space-between !important;
                padding: var(--safe-top) var(--space-2) 0 var(--space-2) !important;
            }}
            /* Hamburger, brand, back, home all stay on one compact row */
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:first-child {{
                flex: 0 0 auto !important;
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:nth-child(2) {{
                flex: 1 1 auto !important;
                min-width: 0 !important;
                overflow: hidden !important;
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:nth-child(3),
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:nth-child(4) {{
                flex: 0 0 auto !important;
                width: auto !important;
            }}
        }}

        /* ── Smart header — mobile: hide controls in idle chat, show while typing, hide on scroll down ── */
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
            transition: transform 0.35s var(--ease-out) !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:first-child,
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:last-child {{
            transition: width 0.3s var(--ease-out), opacity 0.22s var(--ease-out),
                        transform 0.3s var(--ease-out), padding 0.3s var(--ease-out) !important;
            overflow: hidden !important;
        }}
        @media (max-width: 767px) {{
            body.has-chat:not(.input-focus) [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:first-child,
            body.has-chat:not(.input-focus) [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:last-child {{
                width: 0 !important;
                padding: 0 !important;
                opacity: 0 !important;
                transform: translateY(4px) !important;
                pointer-events: none !important;
            }}
            body.scrolled-down:not(.drawer-open) [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
                transform: translateY(-100%) !important;
            }}
        }}

        /* Desktop/tablet: top-right controls always visible and right-aligned */
        @media (min-width: 768px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:first-child,
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:last-child {{
                width: auto !important;
                opacity: 1 !important;
                transform: none !important;
                pointer-events: auto !important;
                overflow: visible !important;
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:last-child {{
                justify-content: flex-end !important;
            }}
        }}

        .zb-header-brand {{
            display: flex;
            align-items: center;
            gap: var(--space-2);
            min-width: 0;
            overflow: hidden;
            flex: 1 1 auto;
        }}
        .zb-header-icon {{
            font-size: 1.15rem;
            line-height: 1;
            flex-shrink: 0;
        }}
        .zb-header-name {{
            font-size: var(--fs-small);
            font-weight: var(--fw-semibold);
            color: var(--text-primary);
            white-space: nowrap;
            letter-spacing: -0.01em;
            overflow: hidden;
            text-overflow: ellipsis;
            flex: 0 1 auto;
            min-width: 0;
        }}
        .zb-header-sep {{
            width: 3px;
            height: 3px;
            background: var(--text-tertiary);
            border-radius: 50%;
            flex-shrink: 0;
        }}
        .zb-header-status {{
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: var(--fs-xs);
            font-weight: var(--fw-medium);
            color: var(--green);
            letter-spacing: 0.01em;
            white-space: nowrap;
            flex-shrink: 0;
        }}
        .zb-header-status::before {{
            content: '';
            width: 5px;
            height: 5px;
            background: var(--green);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--green-glow);
            display: inline-block;
            flex-shrink: 0;
            animation: statusPulse 2.2s var(--ease-out) infinite;
        }}
        @keyframes statusPulse {{
            0%, 100% {{ box-shadow: 0 0 6px var(--green-glow); opacity: 1; }}
            50% {{ box-shadow: 0 0 2px var(--green-glow), 0 0 14px var(--green-glow); opacity: 0.8; }}
        }}

        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) .stButton > button {{
            background: rgba(255,255,255,0.04) !important;
            border: 1px solid var(--border-light) !important;
            border-radius: var(--radius-sm) !important;
            color: var(--text-secondary) !important;
            font-size: 0.65rem !important;
            font-weight: var(--fw-medium) !important;
            padding: 3px 8px !important;
            height: 28px !important;
            min-height: 28px !important;
            line-height: 1 !important;
            transition: all var(--transition-fast) !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            white-space: nowrap !important;
            pointer-events: auto !important;
            cursor: pointer !important;
            z-index: 99999 !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) .stButton > button:hover {{
            background: rgba(255,255,255,0.09) !important;
            color: var(--text-primary) !important;
            border-color: var(--border-medium) !important;
            transform: translateY(-1px) !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) .stButton > button:active {{
            transform: scale(0.95) !important;
        }}

        @media (min-width: 768px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) .stButton > button {{
                padding: 4px 12px !important;
                height: 30px !important;
                min-height: 30px !important;
                font-size: 0.7rem !important;
            }}
        }}
        @media (max-width: 767px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div:nth-child(2) {{
                min-width: 0 !important;
            }}
            .zb-header-brand {{
                flex: 1 1 0% !important;
                min-width: 0 !important;
            }}
            .zb-header-name {{
                font-size: 0.8rem;
            }}
            .zb-header-sep {{
                display: none;
            }}
            .zb-header-status {{
                font-size: 0.55rem;
            }}
            .zb-header-status::before {{
                width: 4px;
                height: 4px;
            }}
        }}

        /* Mobile: top-right button keeps a consistent 44px touch target, never wraps */
        @media (max-width: 640px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div .stButton > button {{
                width: 44px !important;
                min-width: 44px !important;
                height: 44px !important;
                min-height: 44px !important;
                font-size: 1.05rem !important;
                padding: 0 !important;
                flex-shrink: 0 !important;
                margin: 0 !important;
            }}
        }}

        /* Native header control buttons (☰ / ✦) — 46px touch targets (after cascade) */
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div .stButton > button {{
            width: 46px !important;
            min-width: 46px !important;
            height: 44px !important;
            min-height: 44px !important;
            padding: 0 !important;
            font-size: 1.15rem !important;
            line-height: 1 !important;
            border-radius: var(--radius-md) !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}
        @media (max-width: 480px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div .stButton > button {{
                width: 42px !important;
                min-width: 42px !important;
                height: 42px !important;
                min-height: 42px !important;
                font-size: 1.05rem !important;
            }}
        }}

        /* ==========================================================================
           NAV DRAWERS — left menu & right quick actions (real buttons inside real columns)
           ========================================================================== */

        @keyframes drawerInLeft {{
            from {{ transform: translateX(-100%); }}
            to {{ transform: translateX(0); }}
        }}
        @keyframes drawerInRight {{
            from {{ transform: translateX(100%); }}
            to {{ transform: translateX(0); }}
        }}

        .zb-menu-anchor,
        .zb-panel-anchor {{
            display: none !important;
        }}

        /* Full-screen native backdrop — real button, really closes via rerun */
        [data-testid*="zb_backdrop_menu"],
        [data-testid*="zb_backdrop_panel"] {{
            position: fixed !important;
            top: var(--header-total) !important;
            left: 0 !important;
            right: 0 !important;
            bottom: 0 !important;
            width: 100vw !important;
            height: calc(100dvh - var(--header-total)) !important;
            border: none !important;
            border-radius: 0 !important;
            box-shadow: none !important;
            background: rgba(0,0,0,0.45) !important;
            backdrop-filter: blur(6px) !important;
            -webkit-backdrop-filter: blur(6px) !important;
            z-index: 999990 !important;
            cursor: default !important;
            animation: heroFade 0.2s var(--ease-out) both;
        }}
        [data-testid*="zb_backdrop_menu"]:hover,
        [data-testid*="zb_backdrop_panel"]:hover {{
            background: rgba(0,0,0,0.45) !important;
        }}

        /* ── Remove ghost box outlines from drawer backdrops & their wrappers ── */
        [data-testid*="zb_backdrop_menu"],
        [data-testid*="zb_backdrop_panel"],
        [data-testid="stElementContainer"]:has([data-testid*="zb_backdrop"]),
        button[data-testid*="zb_backdrop"] {{
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
        }}

        /* ── Collapse empty Streamlit DOM containers ── */
        .element-container:empty,
        [data-testid="stElementContainer"]:empty,
        [data-testid="stMarkdown"]:empty {{
            display: none !important;
            border: none !important;
            margin: 0 !important;
            padding: 0 !important;
        }}

        /* Drawer panel — fixed glass column (one real stColumn) */
        [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) {{
            position: fixed !important;
            top: var(--header-total) !important;
            bottom: 0 !important;
            z-index: 999999 !important;
            width: min(330px, 86vw) !important;
            height: calc(100dvh - var(--header-total)) !important;
            flex: 0 0 auto !important;
            display: flex !important;
            flex-direction: column !important;
            gap: 0 !important;
            padding: var(--space-3) !important;
            padding-bottom: 140px !important;
            overflow-y: auto !important;
            -webkit-overflow-scrolling: touch !important;
            overscroll-behavior: contain;
            background: rgba(10,10,10,0.88) !important;
            backdrop-filter: blur(28px) saturate(1.5) !important;
            -webkit-backdrop-filter: blur(28px) saturate(1.5) !important;
            box-shadow: 12px 0 48px rgba(0,0,0,0.5) !important;
        }}
        [data-testid="stColumn"]:has(.zb-menu-anchor) {{
            left: 0 !important;
            border-right: 1px solid var(--border-light) !important;
            border-radius: 0 20px 20px 0 !important;
            animation: drawerInLeft 0.32s var(--ease-out) both;
        }}
        [data-testid="stColumn"]:has(.zb-panel-anchor) {{
            right: 0 !important;
            border-left: 1px solid var(--border-light) !important;
            border-radius: 20px 0 0 20px !important;
            animation: drawerInRight 0.32s var(--ease-out) both;
        }}

        /* Inner drawer bottom clearance — last items scroll well clear of the screen bottom */
        [data-testid="stColumn"]:has(.zb-menu-anchor) > div,
        [data-testid="stColumn"]:has(.zb-panel-anchor) > div {{
            padding-bottom: 80px !important;
        }}

        /* ==========================================================================
           DRAWER / CHAT INPUT LAYERING
           The drawer column and stBottom are BOTH position:fixed elements rendered
           inside section.main's subtree. Their ancestor stacking contexts differ
           per Streamlit version/DOM, so z-index escalation alone cannot guarantee
           order (the two values may never compete). While a drawer is open we
           therefore fully suppress the chat bar — hidden + inert + demoted — so
           it can never visually cover or intercept the drawer, no matter which
           stacking context wins. When body.drawer-open is removed, every one of
           these declarations releases and the bar returns exactly as it was.
           ========================================================================== */

        /* 1. Chat bar fully suppressed while a drawer/dialog is open */
        body.drawer-open [data-testid="stBottom"],
        body.drawer-open [data-testid="stBottom"] > div,
        body.drawer-open [data-testid="stBottom"] *,
        body.drawer-open [data-testid="stChatInput"],
        body.dialog-open [data-testid="stBottom"],
        body.dialog-open [data-testid="stBottom"] > div,
        body.dialog-open [data-testid="stBottom"] *,
        body.dialog-open [data-testid="stChatInput"] {{
            pointer-events: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            z-index: 100 !important;
        }}

        /* 2. Lift the whole chat surface so everything inside it (drawer, backdrop)
              outranks the bar even in nested-context browsers */
        body.drawer-open section.main,
        body.drawer-open .main,
        body.drawer-open [data-testid="stMain"],
        body.dialog-open section.main,
        body.dialog-open .main,
        body.dialog-open [data-testid="stMain"] {{
            position: relative !important;
            z-index: 999995 !important;
        }}

        /* 3. The active drawer panel and its buttons keep full interactivity */
        body.drawer-open [data-testid="stColumn"]:has(.zb-menu-anchor), [data-testid="stColumn"]:has(.zb-panel-anchor),
        body.drawer-open [data-testid="stColumn"]:has(.zb-menu-anchor), [data-testid="stColumn"]:has(.zb-panel-anchor) * {{
            pointer-events: auto !important;
        }}

        /* 4. Fallback: the drawer renders in the DOM ⇔ it is open. Even if the
              body class is ever missed, its mere presence suppresses the bar. */
        body:has([data-testid="stColumn"] .zb-menu-anchor) [data-testid="stBottom"],
        body:has([data-testid="stColumn"] .zb-menu-anchor) [data-testid="stBottom"] > div,
        body:has([data-testid="stColumn"] .zb-menu-anchor) [data-testid="stBottom"] *,
        body:has([data-testid="stColumn"] .zb-menu-anchor) [data-testid="stChatInput"],
        body:has([data-testid="stColumn"] .zb-panel-anchor) [data-testid="stBottom"],
        body:has([data-testid="stColumn"] .zb-panel-anchor) [data-testid="stBottom"] > div,
        body:has([data-testid="stColumn"] .zb-panel-anchor) [data-testid="stBottom"] *,
        body:has([data-testid="stColumn"] .zb-panel-anchor) [data-testid="stChatInput"] {{
            pointer-events: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            z-index: 100 !important;
        }}

        /* 5. Compact drawer on small phones — every item fits above the bottom edge
              without fighting the chat area: tighter rows, slimmer header/footer */
        @media (max-width: 767px) {{
            [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) {{
                padding: var(--space-2) !important;
                padding-bottom: 100px !important;
                gap: 2px !important;
            }}
            [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .stButton > button {{
                padding: 6px 12px !important;
                min-height: 34px !important;
                font-size: 0.78rem !important;
                line-height: 1.2 !important;
            }}
            [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .zb-drawer-head {{
                padding: var(--space-1) var(--space-1) var(--space-2) !important;
                margin-bottom: var(--space-1) !important;
            }}
            [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .zb-drawer-foot {{
                padding-top: var(--space-2) !important;
                font-size: 0.68rem !important;
            }}
        }}

        /* Drawer header / footer */
        .zb-drawer-head {{
            padding: var(--space-2) var(--space-1) var(--space-3);
            border-bottom: 1px solid var(--border-subtle);
            margin-bottom: var(--space-2);
        }}
        .zb-drawer-title {{
            display: block;
            font-size: 1rem;
            font-weight: var(--fw-semibold);
            color: var(--text-primary);
        }}
        .zb-drawer-sub {{
            display: block;
            font-size: var(--fs-xs);
            color: var(--text-tertiary);
            margin-top: 2px;
        }}
        .zb-drawer-foot {{
            margin-top: auto;
            padding-top: var(--space-3);
            font-size: var(--fs-xs);
            color: var(--text-tertiary);
            text-align: center;
            letter-spacing: 0.02em;
        }}

        /* Drawer items — native buttons, 48px touch target, hover lift */
        [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .stButton > button {{
            width: 100%;
            min-height: 48px !important;
            gap: 10px;
            justify-content: flex-start;
            text-align: left;
            background: rgba(255,255,255,0.03) !important;
            border: 1px solid transparent !important;
            border-radius: var(--radius-md) !important;
            color: var(--text-secondary) !important;
            font-family: var(--font-sans) !important;
            font-size: 0.9rem !important;
            font-weight: var(--fw-medium) !important;
            padding: 0 14px !important;
            margin-bottom: 4px;
            box-shadow: none !important;
            transition: all var(--transition-fast) !important;
        }}
        [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .stButton > button:hover {{
            background: rgba(255,255,255,0.07) !important;
            border-color: var(--border-light) !important;
            color: var(--text-primary) !important;
            transform: translateY(-1px) !important;
        }}
        [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .stButton > button:active {{
            transform: scale(0.98) !important;
        }}

        /* Drawer close ✕ button */
        [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) [data-testid*="baseButton-close"],
        [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) button[data-testid*="_close"] {{
            width: 42px !important;
            min-width: 42px !important;
            height: 42px !important;
            min-height: 42px !important;
            padding: 0 !important;
            justify-content: center !important;
            font-size: 1rem !important;
            border-radius: var(--radius-md) !important;
            align-self: flex-end;
        }}

        body.drawer-open {{
            overflow: hidden !important;
        }}
        body.drawer-open section.main,
        body.drawer-open [data-testid="stAppViewContainer"] {{
            overflow: hidden !important;
        }}

        /* ==========================================================================
           COMPACT HERO
           ========================================================================== */

        @keyframes heroFade {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .zb-hero {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            text-align: center;
            padding: 3vh 0 var(--space-2);
            animation: heroFade 0.5s var(--ease-out) both;
        }}
        .zb-hero-icon {{
            font-size: 1.75rem;
            margin-bottom: 2px;
            display: block;
            line-height: 1;
        }}
        .zb-hero-title {{
            font-size: var(--fs-hero);
            font-weight: var(--fw-bold);
            letter-spacing: -0.02em;
            background: linear-gradient(180deg, #FFFFFF 30%, rgba(255,255,255,0.6) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 0 0 2px 0;
            line-height: 1.15;
        }}

        /* Preserve native emoji colors inside gradient headers */
        .zb-native-emoji,
        .zb-header-icon {{
            -webkit-text-fill-color: initial !important;
            -webkit-background-clip: initial !important;
            background-clip: initial !important;
            background: none !important;
            color: initial !important;
            filter: none !important;
            display: inline-block;
        }}

        /* Hide Streamlit's default header anchor link icon */
        .main h1 a,
        .main h2 a,
        .main h3 a,
        [data-testid="stHeaderActionElements"],
        a.header-action-link {{
            display: none !important;
            visibility: hidden !important;
        }}
        .zb-hero-sub {{
            font-size: clamp(1rem, 3vw, 1.2rem);
            color: var(--text-secondary);
            font-weight: var(--fw-normal);
            margin: 0 0 24px 0;
            line-height: 1.3;
            max-width: 560px;
        }}

        @media (max-width: 480px) {{
            .zb-hero {{
                padding: 2vh 0 var(--space-2);
            }}
            .zb-hero-icon {{
                font-size: 1.4rem;
            }}
            .zb-hero-title {{
                font-size: clamp(1.4rem, 7vw, 2rem);
            }}
            .zb-hero-sub {{
                margin-bottom: 24px;
                font-size: clamp(0.95rem, 3.5vw, 1.1rem);
                line-height: 1.4;
            }}
        }}
        @media (min-width: 1200px) {{
            .zb-hero {{
                padding: 4vh 0 var(--space-2);
            }}
            .zb-hero-icon {{
                font-size: 1.6rem;
            }}
        }}

        /* ==========================================================================
           QUICK ACTION CHIPS — wrapping pill grid
           (Anchor lives inside the actual stHorizontalBlock holding the buttons)
           ========================================================================== */

        .zb-chips-anchor {{
            display: none !important;
        }}
        [data-testid="stColumn"] .stMarkdown:has(.zb-chips-anchor, .zb-fu-anchor) {{
            display: none !important;
        }}

        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) {{
            display: flex !important;
            flex-wrap: wrap !important;
            justify-content: center;
            gap: var(--space-2) !important;
            padding: 0 0 var(--space-2) 0 !important;
            margin-bottom: var(--space-1) !important;
            animation: heroFade 0.5s var(--ease-out) 0.1s both;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) > [data-testid="stColumn"],
        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) > div {{
            flex: 0 0 auto !important;
            width: auto !important;
            min-width: 0 !important;
            padding: 0 !important;
            max-width: none !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button {{
            background: rgba(255,255,255,0.03) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid var(--border-light) !important;
            border-radius: var(--radius-full) !important;
            padding: 6px 16px !important;
            color: var(--text-secondary) !important;
            font-family: var(--font-sans) !important;
            font-size: 0.75rem !important;
            font-weight: var(--fw-medium) !important;
            white-space: normal !important;
            word-wrap: break-word !important;
            min-height: 40px !important;
            height: auto !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            text-align: center !important;
            line-height: 1.3 !important;
            transition: all var(--transition-fast) !important;
            box-shadow: none !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button:hover {{
            background: rgba(255,133,51,0.09) !important;
            border-color: rgba(255,133,51,0.45) !important;
            color: var(--text-primary) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 28px rgba(255,133,51,0.16) !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button:active {{
            transform: scale(0.96) !important;
        }}
        @media (min-width: 768px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button {{
                font-size: 0.8125rem !important;
                padding: 7px 18px !important;
            }}
        }}

        /* Mobile — chips become full-width pill grid */
        @media (max-width: 768px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) > [data-testid="stColumn"],
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) > div {{
                flex: 1 1 100% !important;
                width: 100% !important;
                max-width: none !important;
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button {{
                width: 100% !important;
                max-width: none !important;
                white-space: normal !important;
            }}
        }}

        /* ==========================================================================
           GLASSMORPHIC CHAT BUBBLES
           ========================================================================== */

        @keyframes bubbleIn {{
            from {{ opacity: 0; transform: translateY(8px) scale(0.98); }}
            to {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}

        /* ── ChatGPT-style thinking pill shown while streaming ── */
        @keyframes zbTypingBounce {{
            0%, 60%, 100% {{ transform: translateY(0); opacity: 0.4; }}
            30% {{ transform: translateY(-5px); opacity: 1; }}
        }}
        .zb-typing {{
            display: inline-flex !important;
            align-items: center;
            gap: 5px;
            padding: 10px 16px;
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border-light);
            border-radius: var(--radius-full);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: var(--shadow-sm);
            animation: bubbleIn 0.3s var(--ease-out) both;
        }}
        .zb-typing-dot {{
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--brand), #FFB27A);
            box-shadow: 0 0 10px var(--brand-glow);
            animation: zbTypingBounce 1.2s var(--ease-out) infinite;
        }}
        .zb-typing-dot:nth-child(2) {{ animation-delay: 0.18s; }}
        .zb-typing-dot:nth-child(3) {{ animation-delay: 0.36s; }}

        .stChatMessage {{
            background: transparent !important;
            border: none !important;
            padding: var(--space-1) 0 !important;
            gap: var(--space-2) !important;
            align-items: flex-start !important;
            animation: bubbleIn 0.3s var(--ease-out) both;
        }}
        .stChatMessage:first-child {{
            margin-top: var(--space-2) !important;
        }}

        /* Premium glass avatars — emoji glyph in a frosted circle */
        [data-testid="chatAvatarIcon-user"],
        [data-testid="chatAvatarIcon-assistant"] {{
            display: flex !important;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            align-items: center;
            justify-content: center;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border-light);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            flex-shrink: 0;
            font-size: 1.05rem;
            line-height: 1;
            user-select: none;
        }}
        [data-testid="chatAvatarIcon-user"] svg,
        [data-testid="chatAvatarIcon-assistant"] svg {{
            display: none !important;
        }}
        [data-testid="chatAvatarIcon-user"]::before {{
            content: '\1F37D';
        }}
        [data-testid="chatAvatarIcon-assistant"]::before {{
            content: '\2728';
        }}

        /* Avatar color coding — warm glass for you, brand glow for ZingyByte */
        [data-testid="chatAvatarIcon-user"] {{
            background: linear-gradient(135deg, rgba(16,163,127,0.16), rgba(255,255,255,0.05)) !important;
            border-color: rgba(16,163,127,0.35) !important;
            box-shadow: 0 4px 16px rgba(16,163,127,0.12) !important;
        }}
        [data-testid="chatAvatarIcon-assistant"] {{
            background: linear-gradient(135deg, rgba(255,133,51,0.16), rgba(255,255,255,0.05)) !important;
            border-color: rgba(255,133,51,0.4) !important;
            box-shadow: 0 0 0 1px rgba(255,133,51,0.12), 0 4px 18px rgba(255,133,51,0.2) !important;
        }}
        [data-testid="chatAvatarIcon-user"]::before,
        [data-testid="chatAvatarIcon-assistant"]::before {{
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.35));
        }}

        /* User bubble — glass card */
        [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stMarkdown {{
            background: rgba(255,255,255,0.05) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid var(--border-light) !important;
            padding: var(--space-3) var(--space-4) !important;
            border-radius: var(--radius-lg) !important;
            border-bottom-right-radius: var(--radius-sm) !important;
            display: inline-block !important;
            max-width: 85% !important;
            float: right !important;
            font-size: var(--fs-body) !important;
            line-height: var(--lh-relaxed) !important;
            color: var(--text-primary) !important;
            clear: both;
            box-shadow: var(--shadow-md) !important;
            overflow-wrap: break-word;
            word-break: break-word;
        }}
        [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {{
            flex-direction: row-reverse !important;
        }}

        /* Assistant bubble — clean, readable text */
        [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) .stMarkdown {{
            color: var(--text-primary) !important;
            font-size: var(--fs-body) !important;
            line-height: var(--lh-relaxed) !important;
            padding: var(--space-2) 0 !important;
            clear: both;
            float: left !important;
            max-width: 95% !important;
            overflow-wrap: break-word;
            word-break: break-word;
        }}

        [data-testid="stChatMessage"]::after {{
            content: '';
            display: table;
            clear: both;
        }}

        /* ── Bubble container/content chrome reset ── */
        [data-testid="stChatMessageContent"] {{
            background: transparent !important;
            padding: 0 !important;
        }}

        /* ── Chat width — 88% on desktop, full width on mobile ── */
        .stChatMessage {{
            max-width: 88% !important;
        }}
        [data-testid="stChatMessage"] {{
            max-width: 88% !important;
        }}
        @media (max-width: 768px) {{
            .stChatMessage {{
                max-width: 100% !important;
                padding: 4px 0 !important;
            }}
            [data-testid="stChatMessage"] {{
                max-width: 100% !important;
            }}
            [data-testid="stChatMessage"] .stMarkdown {{
                font-size: 1rem !important;
            }}
            [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stMarkdown {{
                max-width: 90% !important;
                padding: 12px 16px !important;
                font-size: 0.95rem !important;
            }}
            [data-testid="stChatInput"] {{
                padding: 4px 6px !important;
                border-radius: 22px !important;
                width: calc(100% - 32px) !important;
                max-width: calc(100% - 32px) !important;
                box-sizing: border-box !important;
                margin: 0 16px !important;
            }}
        }}

        /* ── Markdown: tables & code scroll horizontally on small screens ── */
        [data-testid="stChatMessage"] .stMarkdown {{
            min-width: 0;
        }}
        [data-testid="stChatMessage"] .stMarkdown table {{
            display: block;
            max-width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            border-collapse: collapse;
            font-size: var(--fs-small);
        }}
        [data-testid="stChatMessage"] .stMarkdown pre {{
            max-width: 100%;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            background: rgba(255,255,255,0.03) !important;
            border: 1px solid var(--border-subtle) !important;
            border-radius: var(--radius-md) !important;
            font-family: var(--font-mono);
            font-size: var(--fs-small) !important;
            padding: var(--space-3) !important;
        }}
        [data-testid="stChatMessage"] .stMarkdown table th,
        [data-testid="stChatMessage"] .stMarkdown table td {{
            padding: var(--space-1) var(--space-2) !important;
            border-color: var(--border-medium) !important;
        }}
        [data-testid="stChatMessage"] .stMarkdown img {{
            max-width: 100%;
            border-radius: var(--radius-md);
        }}

        /* Streaming text cursor */
        .zb-cursor {{
            display: inline-block;
            width: 2px;
            height: 1em;
            vertical-align: text-bottom;
            margin-left: 2px;
            background: var(--brand);
            box-shadow: 0 0 8px var(--brand-glow);
            animation: cursorBlink 0.8s steps(1) infinite;
        }}
        @keyframes cursorBlink {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0; }}
        }}

        /* ── Copy action ── */
        .zb-chat-actions {{
            display: flex;
            gap: var(--space-1);
            margin-top: var(--space-1);
            opacity: 0;
            transition: opacity var(--transition-fast);
        }}
        .stChatMessage:hover .zb-chat-actions {{
            opacity: 1;
        }}
        @media (max-width: 768px) {{
            .zb-chat-actions {{
                opacity: 1;
            }}
        }}

        .zb-chat-action-btn {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 4px 10px;
            font-size: var(--fs-xs);
            font-weight: var(--fw-medium);
            color: var(--text-tertiary);
            background: rgba(255,255,255,0.02);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-sm);
            cursor: pointer;
            font-family: var(--font-sans);
            transition: all var(--transition-fast);
        }}
        .zb-chat-action-btn:hover {{
            color: var(--text-secondary);
            background: rgba(255,255,255,0.05);
            border-color: var(--border-light);
        }}
        .zb-chat-action-btn.copied {{
            color: var(--green);
            border-color: rgba(16,163,127,0.2);
            background: rgba(16,163,127,0.06);
        }}

        /* ==========================================================================
           FOLLOW-UP QUESTIONS — glass pill grid
           (Anchor lives inside the actual stHorizontalBox holding the buttons)
           ========================================================================== */

        .zb-fu-anchor {{
            display: none !important;
        }}

        .zb-followup {{
            margin-top: var(--space-2);
            padding-top: var(--space-2);
            border-top: 1px solid var(--border-subtle);
        }}
        .zb-followup-label {{
            font-size: var(--fs-xs);
            color: var(--text-tertiary);
            font-weight: var(--fw-medium);
            margin-bottom: var(--space-2);
            display: block;
            letter-spacing: 0.02em;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) {{
            display: flex !important;
            flex-wrap: wrap !important;
            gap: var(--space-2) !important;
            margin-top: var(--space-1) !important;
            animation: heroFade 0.4s var(--ease-out) 0.15s both;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) > [data-testid="stColumn"],
        [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) > div {{
            width: auto !important;
            padding: 0 !important;
            min-width: 0 !important;
            flex: 0 1 auto !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) .stButton > button {{
            background: rgba(255,255,255,0.02) !important;
            border: 1px solid var(--border-subtle) !important;
            border-radius: var(--radius-full) !important;
            color: var(--text-secondary) !important;
            font-family: var(--font-sans) !important;
            font-size: 0.82rem !important;
            font-weight: var(--fw-medium) !important;
            padding: 8px 14px !important;
            min-height: 38px !important;
            height: auto !important;
            text-align: left !important;
            line-height: 1.3 !important;
            transition: all var(--transition-fast) !important;
            width: auto !important;
            white-space: nowrap !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) .stButton > button:hover {{
            background: rgba(255,133,51,0.08) !important;
            border-color: rgba(255,133,51,0.4) !important;
            color: var(--text-primary) !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 8px 20px rgba(255,133,51,0.14) !important;
        }}

        @media (max-width: 640px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) {{
                display: flex !important;
                flex-wrap: wrap !important;
                gap: 8px !important;
                justify-content: flex-start !important;
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) .stButton > button {{
                min-height: 38px !important;
                white-space: nowrap !important;
            }}
        }}

        /* ==========================================================================
           STICKY INPUT BAR — native stBottom container (Streamlit 1.31+)
           ========================================================================== */

        /* 1. Make Streamlit's bottom sticky container fully transparent */
        [data-testid="stBottom"] {{
            background: transparent !important;
            background-color: transparent !important;
            padding-bottom: max(10px, env(safe-area-inset-bottom)) !important;
        }}
        [data-testid="stBottom"] > div {{
            background: transparent !important;
            background-color: transparent !important;
        }}

        /* 2. Style the chat input widget as a floating premium bar, centered in stBottom */
        [data-testid="stChatInput"] {{
            width: min(850px, calc(100% - 16px)) !important;
            max-width: none !important;
            margin: 0 auto !important;
            background: rgba(15,15,15,0.72) !important;
            backdrop-filter: blur(24px) saturate(1.6) !important;
            -webkit-backdrop-filter: blur(24px) saturate(1.6) !important;
            border: 1px solid var(--border-medium) !important;
            border-radius: 28px !important;
            padding: 6px 8px !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.4) !important;
            z-index: 999 !important;
            transition: transform var(--transition-base), box-shadow var(--transition-base), border-color var(--transition-base) !important;
            overflow: hidden;
        }}
        [data-testid="stChatInput"]:focus-within {{
            border-color: rgba(255,133,51,0.5) !important;
            box-shadow: 0 12px 48px rgba(0,0,0,0.7), 0 0 0 2px rgba(255,133,51,0.2) !important;
        }}

        /* Sidebar offset for desktop — only while the sidebar is actually open */
        @media (min-width: 768px) {{
            body.sidebar-open [data-testid="stBottom"] {{
                left: var(--sidebar-width) !important;
                width: calc(100% - var(--sidebar-width)) !important;
            }}
        }}

        @media (max-width: 480px) {{
            [data-testid="stChatInput"] {{
                padding: 3px 5px !important;
                border-radius: 24px !important;
            }}
        }}

        [data-testid="stChatInput"] textarea {{
            color: var(--text-primary) !important;
            font-size: var(--fs-body) !important;
            padding: var(--space-3) var(--space-4) !important;
            background: transparent !important;
            border: none !important;
            min-height: 24px !important;
            max-height: 140px !important;
            overflow-y: auto !important;
            line-height: var(--lh-normal) !important;
            scrollbar-width: thin;
        }}
        [data-testid="stChatInput"] textarea::placeholder {{
            color: var(--text-tertiary) !important;
            font-weight: var(--fw-normal) !important;
        }}
        [data-testid="stChatInput"] textarea:focus {{
            box-shadow: none !important;
            border: none !important;
        }}

        [data-testid="stChatInput"] button {{
            background: var(--brand) !important;
            color: #fff !important;
            border-radius: var(--radius-md) !important;
            height: 36px !important;
            width: 36px !important;
            min-width: 36px !important;
            margin-right: 4px !important;
            padding: 0 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: all var(--transition-fast) !important;
            align-self: center !important;
        }}
        [data-testid="stChatInput"] button:hover {{
            background: #ff9955 !important;
            transform: scale(1.05) !important;
        }}
        [data-testid="stChatInput"] button:active {{
            transform: scale(0.94) !important;
        }}
        [data-testid="stChatInput"] button svg {{
            fill: #fff !important;
            width: 16px !important;
            height: 16px !important;
        }}

        /* ==========================================================================
           SIDEBAR — Desktop fixed / Mobile drawer overlay
           ========================================================================== */

        [data-testid="stSidebar"] {{
            position: fixed !important;
            top: var(--header-total) !important;
            left: -100% !important;
            display: block !important;
            width: min(var(--sidebar-width), 85vw) !important;
            height: calc(100dvh - var(--header-total)) !important;
            z-index: 1000 !important;
            background: rgba(10,10,10,0.96) !important;
            backdrop-filter: blur(28px) saturate(1.5) !important;
            -webkit-backdrop-filter: blur(28px) saturate(1.5) !important;
            border-right: 1px solid var(--border-light) !important;
            transition: left 0.3s var(--ease-out) !important;
            padding: 0 !important;
            box-shadow: 4px 0 24px rgba(0,0,0,0.3) !important;
            overflow-y: auto !important;
        }}

        body.sidebar-open [data-testid="stSidebar"] {{
            left: 0 !important;
            z-index: 999999 !important;
        }}

        body.sidebar-open::after {{
            content: '';
            position: fixed;
            inset: 0;
            top: var(--header-total);
            background: rgba(0,0,0,0.5);
            z-index: 999998;
            pointer-events: auto;
            animation: heroFade 0.2s var(--ease-out) both;
        }}

        /* Mobile — sidebar must outrank the fixed chat bar (stBottom) while open */
        @media (max-width: 767px) {{
            [data-testid="stSidebar"],
            body.sidebar-open [data-testid="stSidebar"] {{
                z-index: 999999 !important;
            }}
            [data-testid="stSidebar"] + div,
            [data-testid="stSidebarOverlay"],
            body.sidebar-open::after {{
                z-index: 999998 !important;
            }}
            body.sidebar-open section.main,
            body.sidebar-open .main,
            body.sidebar-open [data-testid="stMain"] {{
                position: relative !important;
                z-index: 999995 !important;
            }}
            body.sidebar-open [data-testid="stBottom"],
            body.sidebar-open [data-testid="stBottom"] > div,
            body.sidebar-open [data-testid="stBottom"] *,
            body.sidebar-open [data-testid="stChatInput"] {{
                pointer-events: none !important;
                z-index: 100 !important;
            }}
            [data-testid="stSidebar"],
            [data-testid="stSidebar"] *,
            body.sidebar-open [data-testid="stSidebar"] * {{
                pointer-events: auto !important;
            }}
            body.sidebar-open [data-testid="stSidebar"] {{
                width: 100vw !important;
                left: 0 !important;
                border-right: none !important;
                border-radius: 0 !important;
            }}
            body.sidebar-open [data-testid="stBottom"],
            body.sidebar-open [data-testid="stBottom"] > div,
            body.sidebar-open [data-testid="stBottom"] *,
            body.sidebar-open [data-testid="stChatInput"] {{
                visibility: hidden !important;
            }}
        }}

        @media (min-width: 768px) {{
            [data-testid="stSidebar"] {{
                left: -100% !important;
                top: var(--header-total) !important;
                width: var(--sidebar-width) !important;
                height: calc(100dvh - var(--header-total)) !important;
                z-index: 1000 !important;
                box-shadow: none !important;
            }}
            body.sidebar-open [data-testid="stSidebar"] {{
                left: 0 !important;
            }}
            body.sidebar-open::after {{
                display: none !important;
            }}
        }}

        [data-testid="stSidebarContent"] {{
            padding: var(--space-4) var(--space-4) calc(120px + 2 * var(--safe-bottom)) var(--space-4) !important;
            overflow-y: auto !important;
            overflow-x: hidden !important;
            height: 100% !important;
            max-height: 100% !important;
            -webkit-overflow-scrolling: touch !important;
            overscroll-behavior: contain !important;
            scrollbar-width: thin;
        }}

        @media (max-width: 480px) {{
            [data-testid="stSidebarContent"] {{
                padding: var(--space-3) var(--space-3) calc(120px + 2 * var(--safe-bottom)) var(--space-3) !important;
            }}
        }}

        /* Mobile — sidebar scrolls independently of the page, never the body */
        @media (max-width: 767px) {{
            [data-testid="stSidebarContent"] {{
                height: 100% !important;
                max-height: 100% !important;
                overflow-y: auto !important;
                -webkit-overflow-scrolling: touch !important;
                overscroll-behavior: contain !important;
                scroll-padding-top: 0 !important;
            }}
            body.sidebar-open,
            body.sidebar-open [data-testid="stSidebar"],
            body.sidebar-open [data-testid="stSidebar"] * {{
                overscroll-behavior: contain !important;
                touch-action: pan-y !important;
            }}
        }}

        /* ── Sidebar brand ── */
        .zb-sidebar-header {{
            display: flex;
            align-items: center;
            gap: var(--space-2);
            padding: var(--space-4) var(--space-4) var(--space-3);
            border-bottom: 1px solid var(--border-subtle);
            margin-bottom: var(--space-3);
        }}
        .zb-sidebar-header .zb-header-icon {{
            font-size: 1.1rem;
        }}
        .zb-sidebar-header .zb-header-name {{
            font-size: var(--fs-small);
            font-weight: var(--fw-semibold);
            color: var(--text-primary);
        }}

        .zb-sidebar-close {{
            margin-left: auto;
            background: rgba(255,255,255,0.06);
            border: 1px solid var(--border-medium);
            border-radius: var(--radius-full);
            color: var(--text-secondary);
            width: 34px;
            height: 34px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.95rem;
            line-height: 1;
            transition: all var(--transition-fast);
            font-family: var(--font-sans);
            flex-shrink: 0;
        }}
        .zb-sidebar-close:hover {{
            background: rgba(255,255,255,0.12);
            color: var(--text-primary);
            border-color: var(--border-light);
        }}

        /* ── Sidebar reopen tab — floats top-left whenever the sidebar is closed ──
           Visibility is driven by the body class synced from real sidebar geometry
           (zbSyncSidebar), NOT by :not(.sidebar-open) — so it never flashes on reruns. */
        .zb-sidebar-reopen {{
            position: fixed;
            left: 10px;
            top: calc(var(--header-total) + 10px);
            z-index: 999985;
            width: 40px;
            height: 40px;
            border-radius: var(--radius-full);
            background: rgba(255,255,255,0.08);
            border: 1px solid var(--border-medium);
            color: var(--text-primary);
            font-size: 1.05rem;
            line-height: 1;
            display: none;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            pointer-events: auto;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.35);
            transition: all var(--transition-fast);
            font-family: var(--font-sans);
        }}
        body.sidebar-tab-visible .zb-sidebar-reopen {{
            display: inline-flex;
        }}
        .zb-sidebar-reopen:hover {{
            background: rgba(255,133,51,0.25);
            border-color: rgba(255,133,51,0.5);
            color: #fff;
        }}
        body.theme-orange .zb-sidebar-reopen {{
            background: rgba(255,133,51,0.16);
            border-color: rgba(255,133,51,0.45);
            color: var(--text-primary);
        }}

        .zb-section-label {{
            font-size: var(--fs-xs) !important;
            font-weight: var(--fw-semibold) !important;
            color: var(--text-tertiary) !important;
            margin-bottom: 6px !important;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            display: block;
        }}

        /* ── Conversation items ── */
        .zb-conv-item {{
            padding: 6px 10px;
            border-radius: var(--radius-md);
            margin-bottom: 1px;
            cursor: pointer;
            transition: all var(--transition-fast);
            border: 1px solid transparent;
            display: flex;
            flex-direction: column;
        }}
        .zb-conv-item:hover {{
            background: var(--bg-elevated);
            border-color: var(--border-subtle);
        }}
        .zb-conv-item.active {{
            background: rgba(255,255,255,0.04);
            border-color: var(--border-light);
        }}
        .zb-conv-title-text {{
            font-size: var(--fs-small);
            font-weight: var(--fw-medium);
            color: var(--text-primary);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: block;
            line-height: 1.3;
        }}
        .zb-conv-meta {{
            font-size: var(--fs-xs);
            color: var(--text-tertiary);
            display: flex;
            gap: var(--space-2);
            margin-top: 1px;
        }}
        .zb-conv-group-label {{
            font-size: var(--fs-xs) !important;
            font-weight: var(--fw-semibold) !important;
            color: var(--text-tertiary) !important;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            padding: 6px 0 2px;
            display: block;
        }}
        .zb-no-convs {{
            font-size: var(--fs-small);
            color: var(--text-tertiary);
            text-align: center;
            padding: var(--space-3) 0;
        }}

        /* ── Sidebar buttons ── */
        [data-testid="stSidebar"] .stButton > button {{
            background: rgba(255,255,255,0.03) !important;
            backdrop-filter: blur(8px) !important;
            -webkit-backdrop-filter: blur(8px) !important;
            border: 1px solid var(--border-subtle) !important;
            border-radius: var(--radius-md) !important;
            color: var(--text-secondary) !important;
            font-family: var(--font-sans) !important;
            font-size: var(--fs-small) !important;
            font-weight: var(--fw-medium) !important;
            width: 100% !important;
            padding: var(--space-2) var(--space-3) !important;
            transition: all var(--transition-fast) !important;
            min-height: 40px !important;
        }}
        [data-testid="stSidebar"] .stButton > button:hover {{
            background: rgba(255,255,255,0.07) !important;
            color: var(--text-primary) !important;
            border-color: var(--border-light) !important;
            transform: translateY(-1px) !important;
        }}

        /* ── Search ── */
        .zb-conv-search {{
            width: 100%;
            padding: 7px 10px;
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            color: var(--text-primary);
            font-family: var(--font-sans);
            font-size: var(--fs-small);
            outline: none;
            transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
            box-sizing: border-box;
            margin-bottom: 6px;
        }}
        .zb-conv-search:focus {{
            border-color: rgba(255,255,255,0.15);
            box-shadow: 0 0 0 3px rgba(255,255,255,0.04);
        }}
        .zb-conv-search::placeholder {{
            color: var(--text-tertiary);
        }}

        /* ── Tips ── */
        .zb-tip-item {{
            display: flex;
            align-items: flex-start;
            gap: var(--space-2);
            padding: var(--space-2) var(--space-3);
            font-size: var(--fs-xs);
            color: var(--text-tertiary);
            line-height: var(--lh-normal);
            border-radius: var(--radius-sm);
            transition: background var(--transition-fast);
        }}
        .zb-tip-item:hover {{
            background: var(--bg-card);
        }}
        .zb-tip-icon {{
            flex-shrink: 0;
            font-size: 0.8rem;
        }}

        /* ── Keyboard hint ── */
        .zb-kbd-hint {{
            font-size: var(--fs-xs);
            color: var(--text-tertiary);
            text-align: center;
            padding: var(--space-2) 0;
            letter-spacing: 0.01em;
        }}
        .zb-kbd-hint kbd {{
            display: inline-block;
            padding: 1px 5px;
            font-size: 0.55rem;
            font-family: var(--font-sans);
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border-subtle);
            border-radius: 3px;
            color: var(--text-secondary);
        }}

        /* ── Slider ── */
        [data-testid="stSidebar"] [data-testid="stSlider"] > div {{
            font-size: var(--fs-xs) !important;
            color: var(--text-secondary) !important;
        }}

        /* ==========================================================================
           ERRORS & ALERTS
           ========================================================================== */

        [data-testid="stAlert"], [data-testid="stException"] {{
            background: rgba(255,75,75,0.06) !important;
            border: 1px solid rgba(255,75,75,0.15) !important;
            border-radius: var(--radius-md) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            padding: var(--space-3) var(--space-4) !important;
            margin: var(--space-3) 0 !important;
        }}
        [data-testid="stAlert"] p, [data-testid="stException"] *, .stException p {{
            color: #FF6B6B !important;
            font-weight: var(--fw-medium) !important;
            font-size: var(--fs-small) !important;
        }}

        /* ==========================================================================
           MISC — Dividers, misc overrides
           ========================================================================== */

        hr {{
            border: none;
            height: 1px;
            background: var(--border-subtle);
            margin: var(--space-3) 0;
        }}

        .element-container:empty {{ display: none !important; }}

        /* ==========================================================================
           RESPONSIVE — fine-tuning for all screen sizes
           ========================================================================== */

        @media (max-width: 480px) {{
            .stChatMessage {{
                padding: 2px 0 !important;
            }}
            [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stMarkdown {{
                max-width: 90% !important;
                padding: 12px 16px !important;
                font-size: 0.95rem !important;
            }}
            [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) .stMarkdown {{
                max-width: 100% !important;
            }}
        }}

        @media (max-width: 414px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
                padding: var(--safe-top) var(--space-2) 0 var(--space-2) !important;
            }}
            .zb-header-brand {{
                gap: var(--space-1);
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button {{
                font-size: 0.7rem !important;
                padding: 5px 12px !important;
            }}
        }}

        @media (max-width: 390px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) > div .stButton > button {{
                width: 42px !important;
                min-width: 42px !important;
                height: 44px !important;
                min-height: 44px !important;
                font-size: 1rem !important;
                padding: 0 !important;
            }}
            .zb-chat-action-btn {{
                padding: 3px 8px;
                font-size: 0.55rem;
            }}
            .main .block-container {{
                padding: calc(var(--header-total) + var(--pad-xs)) var(--pad-xs) 168px var(--pad-xs) !important;
            }}
        }}

        @media (max-width: 360px) {{
            .zb-header-name {{
                font-size: var(--fs-xs);
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button {{
                font-size: 0.65rem;
                padding: 5px 10px;
            }}
            .main .block-container, [data-testid="stMainBlockContainer"] {{
                padding: calc(var(--header-total) + var(--pad-xs)) var(--pad-md) 165px var(--pad-md) !important;
            }}
        }}

        @media (min-width: 1200px) {{
            .stChatMessage {{
                padding: var(--space-2) 0 !important;
                max-width: 80% !important;
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) {{
                gap: var(--space-2) !important;
            }}
        }}

        /* ── Mobile: compact header + background dim (outside frozen block) ── */
        @media (max-width: 768px) {{
            :root {{
                --header-height: 52px;
            }}
            .zb-food-bg {{
                opacity: 0.55;
            }}
            .zb-food-item {{
                font-size: 2.4rem;
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
                justify-content: space-between !important;
                flex-wrap: nowrap !important;
                padding-right: 16px !important;
            }}
            .zb-chat-actions {{
                flex-wrap: wrap !important;
            }}
            .zb-chat-action-btn {{
                flex: 0 1 auto !important;
                max-width: 100% !important;
                white-space: nowrap !important;
            }}
            .stChatMessage {{
                min-width: 0 !important;
                max-width: 100% !important;
                overflow: visible !important;
            }}
            [data-testid="stChatMessage"] [data-testid="stHorizontalBlock"] {{
                flex-wrap: wrap !important;
            }}
            [data-testid="stChatMessage"] [data-testid="stColumn"] {{
                min-width: 0 !important;
                flex: 1 1 0% !important;
            }}
        }}

        /* ── Landscape phones (≤480px tall) — reclaim vertical space ── */
        @media (orientation: landscape) and (max-height: 480px) {{
            :root {{
                --header-height: 44px;
            }}
            .main .block-container {{
                padding-bottom: 160px !important;
            }}
            .zb-hero {{
                padding: 1vh 0 2vh !important;
            }}
            .zb-food-bg {{
                opacity: 0.35;
            }}
            [data-testid="stChatMessage"] {{
                padding: 1px 0 !important;
            }}
        }}

        /* ==========================================================================
           TIMESTAMPS & MESSAGE ACTIONS
           ========================================================================== */

        .zb-ts {{
            font-size: 0.65rem;
            color: var(--text-tertiary);
            letter-spacing: 0.02em;
            clear: both;
            margin-top: 2px;
        }}
        [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .zb-ts {{
            float: right;
        }}
        [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) .zb-ts {{
            float: left;
        }}

        [data-testid*="baseButton-like_"],
        [data-testid*="baseButton-dislike_"],
        [data-testid*="baseButton-share_"],
        [data-testid*="baseButton-regen_"] {{
            width: 42px !important;
            min-width: 42px !important;
            height: 42px !important;
            min-height: 42px !important;
            padding: 0 !important;
            font-size: 1rem !important;
            line-height: 1 !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            background: rgba(255,255,255,0.02) !important;
            border: 1px solid var(--border-subtle) !important;
            border-radius: var(--radius-md) !important;
            color: var(--text-tertiary) !important;
            box-shadow: none !important;
            transition: all var(--transition-fast) !important;
        }}
        [data-testid*="baseButton-like_"]:hover,
        [data-testid*="baseButton-dislike_"]:hover,
        [data-testid*="baseButton-share_"]:hover,
        [data-testid*="baseButton-regen_"]:hover {{
            background: rgba(255,255,255,0.06) !important;
            color: var(--text-primary) !important;
            transform: translateY(-1px) !important;
        }}
        [data-testid="stHorizontalBlock"]:has(button[data-testid*="baseButton-like_"]) {{
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            align-items: center !important;
            justify-content: flex-start !important;
            gap: 6px !important;
            width: fit-content !important;
            margin: 2px 0 4px !important;
        }}
        [data-testid="stHorizontalBlock"]:has(button[data-testid*="baseButton-like_"]) > [data-testid="stColumn"],
        [data-testid="stHorizontalBlock"]:has(button[data-testid*="baseButton-like_"]) > div {{
            flex: 0 0 auto !important;
            width: auto !important;
            max-width: none !important;
            min-width: 0 !important;
            padding: 0 !important;
        }}
        @media (max-width: 480px) {{
            [data-testid*="baseButton-like_"],
            [data-testid*="baseButton-dislike_"],
            [data-testid*="baseButton-share_"],
            [data-testid*="baseButton-regen_"] {{
                width: 40px !important;
                min-width: 40px !important;
                height: 40px !important;
                min-height: 40px !important;
            }}
        }}
        @media (max-width: 360px) {{
            [data-testid*="baseButton-like_"],
            [data-testid*="baseButton-dislike_"],
            [data-testid*="baseButton-share_"],
            [data-testid*="baseButton-regen_"] {{
                width: 38px !important;
                min-width: 38px !important;
                height: 38px !important;
                min-height: 38px !important;
            }}
        }}

        /* ── Feedback row: compact like/dislike + status indicator ── */
        [data-testid="stHorizontalBlock"]:has(.zb-fb-status) {{
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            align-items: center !important;
            gap: 6px !important;
            margin: 2px 0 6px !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-fb-status) > [data-testid="stColumn"] {{
            flex: 0 0 auto !important;
            width: auto !important;
            min-width: 0 !important;
            max-width: none !important;
            padding: 0 !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-fb-status) .stButton > button {{
            width: 40px !important;
            min-width: 40px !important;
            height: 40px !important;
            min-height: 40px !important;
            padding: 0 !important;
            font-size: 1rem !important;
            line-height: 1 !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            background: rgba(255,255,255,0.02) !important;
            border: 1px solid var(--border-subtle) !important;
            border-radius: var(--radius-md) !important;
            color: var(--text-tertiary) !important;
            transition: all var(--transition-fast) !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-fb-status) .stButton > button:hover {{
            background: rgba(255,255,255,0.06) !important;
            color: var(--text-primary) !important;
            transform: translateY(-1px) !important;
        }}
        .zb-fb-status {{
            font-size: var(--fs-xs);
            font-weight: var(--fw-medium);
            color: var(--brand);
            letter-spacing: 0.02em;
            white-space: nowrap;
        }}

        /* ==========================================================================
           LIGHT THEME (toggled from ☰ menu) — clean glass on light surfaces
           ========================================================================== */

        body.theme-light {{
            --bg-deep           : #F4F4F6;
            --bg-surface        : rgba(255,255,255,0.65);
            --bg-card           : rgba(0,0,0,0.03);
            --bg-elevated       : rgba(0,0,0,0.05);
            --bg-hover          : rgba(0,0,0,0.08);
            --border-subtle     : rgba(0,0,0,0.06);
            --border-light      : rgba(0,0,0,0.10);
            --border-medium     : rgba(0,0,0,0.15);
            --text-primary      : #1A1A1A;
            --text-secondary    : rgba(26,26,26,0.65);
            --text-tertiary     : rgba(26,26,26,0.45);
            --brand-glow        : rgba(255,133,51,0.15);
            --shadow-sm         : 0 1px 2px rgba(0,0,0,0.08);
            --shadow-md         : 0 4px 12px rgba(0,0,0,0.08);
            --shadow-lg         : 0 8px 24px rgba(0,0,0,0.10);
            --shadow-xl         : 0 16px 48px rgba(0,0,0,0.14);
            --green-glow        : rgba(16,163,127,0.35);
        }}
        body.theme-light [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
            background: rgba(255,255,255,0.85) !important;
        }}
        body.theme-light [data-testid="stSidebar"] {{
            background: rgba(255,255,255,0.95) !important;
        }}
        body.theme-light [data-testid="stColumn"]:has(.zb-menu-anchor),
        body.theme-light [data-testid="stColumn"]:has(.zb-panel-anchor) {{
            background: rgba(255,255,255,0.94) !important;
        }}
        body.theme-light [data-testid*="zb_backdrop_menu"],
        body.theme-light [data-testid*="zb_backdrop_panel"] {{
            background: rgba(0,0,0,0.28) !important;
        }}
        body.theme-light [data-testid="stChatInput"] {{
            background: rgba(255,255,255,0.85) !important;
        }}
        body.theme-light [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stMarkdown {{
            background: rgba(0,0,0,0.05) !important;
        }}
        body.theme-light .zb-hero-title {{
            background: linear-gradient(180deg, #1A1A1A 30%, rgba(26,26,26,0.6) 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        body.theme-light [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button,
        body.theme-light [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) .stButton > button,
        body.theme-light [data-testid="stSidebar"] .stButton > button,
        body.theme-light [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .stButton > button,
        body.theme-light [data-testid*="baseButton-like_"],
        body.theme-light [data-testid*="baseButton-dislike_"],
        body.theme-light [data-testid*="baseButton-share_"],
        body.theme-light [data-testid*="baseButton-regen_"] {{
            background: rgba(0,0,0,0.03) !important;
            color: var(--text-secondary) !important;
        }}
        body.theme-light [data-testid*="baseButton-like_"]:hover,
        body.theme-light [data-testid*="baseButton-dislike_"]:hover,
        body.theme-light [data-testid*="baseButton-share_"]:hover,
        body.theme-light [data-testid*="baseButton-regen_"]:hover {{
            background: rgba(0,0,0,0.06) !important;
            color: var(--text-primary) !important;
        }}
        body.theme-light .zb-chat-action-btn {{
            background: rgba(0,0,0,0.03);
            border-color: var(--border-subtle);
        }}
        body.theme-light [data-testid="stChatMessage"] .stMarkdown pre {{
            background: rgba(0,0,0,0.04) !important;
        }}
        body.theme-light [data-testid="stChatInput"] textarea {{
            color: var(--text-primary) !important;
        }}

        /* ==========================================================================
           ORANGE THEME (toggled from ☰ menu) — warm amber glass
           ========================================================================== */

        body.theme-orange {{
            background: var(--bg-deep) !important;
            --bg-deep          : #1D130D;
            --bg-surface       : rgba(255,140,60,0.07);
            --bg-card          : rgba(255,140,60,0.08);
            --bg-elevated      : rgba(255,140,60,0.11);
            --bg-hover         : rgba(255,140,60,0.15);
            --border-subtle    : rgba(255,150,70,0.14);
            --border-light     : rgba(255,150,70,0.22);
            --border-medium    : rgba(255,150,70,0.32);
            --text-primary     : #F3E4D0;
            --text-secondary   : rgba(243,228,208,0.62);
            --text-tertiary    : rgba(243,228,208,0.38);
            --brand            : #FF9A3C;
            --brand-glow       : rgba(255,154,60,0.35);
            --green            : #FF9A3C;
            --green-glow       : rgba(255,154,60,0.45);
            --shadow-sm        : 0 1px 2px rgba(255,120,40,0.10);
            --shadow-md        : 0 4px 12px rgba(255,120,40,0.14);
            --shadow-lg        : 0 8px 24px rgba(0,0,0,0.35);
            --shadow-xl        : 0 16px 48px rgba(0,0,0,0.45);
        }}

        /* Warm ambient glow behind everything */
        body.theme-orange [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(1100px 700px at 85% -10%, rgba(255,140,60,0.14), transparent 60%),
                radial-gradient(900px 650px at 5% 110%, rgba(255,90,40,0.10), transparent 60%),
                var(--bg-deep) !important;
        }}
        body.theme-orange .stApp {{
            background:
                radial-gradient(1200px 800px at 80% -10%, rgba(255,140,60,0.08), transparent 60%),
                var(--bg-deep) !important;
        }}

        /* Floating food emojis take on a warm amber tint (frozen block untouched) */
        body.theme-orange .zb-food-item {{
            filter: sepia(0.5) hue-rotate(-16deg) saturate(1.4) brightness(0.92);
            opacity: 0.06;
        }}

        body.theme-orange [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
            background: rgba(26,17,9,0.80) !important;
            border-bottom-color: rgba(255,150,70,0.22) !important;
        }}
        body.theme-orange [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) .stButton > button {{
            background: rgba(255,140,60,0.10) !important;
            border-color: rgba(255,150,70,0.24) !important;
            color: var(--text-primary) !important;
        }}
        body.theme-orange [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) .stButton > button:hover {{
            background: rgba(255,140,60,0.16) !important;
            border-color: rgba(255,160,70,0.40) !important;
            box-shadow: 0 0 14px rgba(255,140,60,0.20) !important;
        }}

        body.theme-orange [data-testid="stSidebar"] {{
            background: rgba(24,16,9,0.96) !important;
            border-right-color: rgba(255,150,70,0.15) !important;
        }}
        body.theme-orange [data-testid="stColumn"]:has(.zb-menu-anchor),
        body.theme-orange [data-testid="stColumn"]:has(.zb-panel-anchor) {{
            background: rgba(24,16,9,0.97) !important;
        }}
        body.theme-orange [data-testid*="zb_backdrop_menu"],
        body.theme-orange [data-testid*="zb_backdrop_panel"] {{
            background: rgba(20,8,2,0.50) !important;
        }}
        body.theme-orange .zb-sidebar-close {{
            background: rgba(255,140,60,0.08);
            border-color: rgba(255,150,70,0.20);
            color: var(--text-secondary);
        }}
        body.theme-orange .zb-sidebar-close:hover {{
            background: rgba(255,140,60,0.14);
            color: var(--text-primary);
        }}

        body.theme-orange .zb-hero-title {{
            background: linear-gradient(180deg, #FFC49A 20%, #FF9A3C 100%);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        body.theme-orange .zb-hero-icon {{
            filter: drop-shadow(0 0 14px rgba(255,140,60,0.45));
        }}

        body.theme-orange [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) .stMarkdown {{
            background: rgba(255,140,60,0.08) !important;
            border-color: rgba(255,150,70,0.25) !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
        }}
        body.theme-orange [data-testid="chatAvatarIcon-user"],
        body.theme-orange [data-testid="chatAvatarIcon-assistant"] {{
            background: rgba(255,140,60,0.10);
            border-color: rgba(255,150,70,0.30);
            box-shadow: 0 4px 12px rgba(255,120,40,0.18);
        }}
        body.theme-orange [data-testid="chatAvatarIcon-assistant"]::before {{
            text-shadow: 0 0 10px rgba(255,154,60,0.70);
        }}

        body.theme-orange [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button,
        body.theme-orange [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) .stButton > button,
        body.theme-orange [data-testid="stSidebar"] .stButton > button,
        body.theme-orange [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .stButton > button {{
            background: rgba(255,140,60,0.07) !important;
            border-color: rgba(255,150,70,0.20) !important;
            color: var(--text-secondary) !important;
        }}
        body.theme-orange [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor) .stButton > button:hover,
        body.theme-orange [data-testid="stHorizontalBlock"]:has(.zb-fu-anchor) .stButton > button:hover,
        body.theme-orange [data-testid="stSidebar"] .stButton > button:hover,
        body.theme-orange [data-testid="stColumn"]:has(.zb-menu-anchor, .zb-panel-anchor) .stButton > button:hover {{
            background: rgba(255,140,60,0.14) !important;
            border-color: rgba(255,154,60,0.45) !important;
            color: var(--text-primary) !important;
            box-shadow: 0 0 16px rgba(255,140,60,0.15) !important;
        }}

        body.theme-orange [data-testid*="baseButton-like_"],
        body.theme-orange [data-testid*="baseButton-dislike_"],
        body.theme-orange [data-testid*="baseButton-share_"],
        body.theme-orange [data-testid*="baseButton-regen_"] {{
            background: rgba(255,140,60,0.06) !important;
            border-color: rgba(255,150,70,0.18) !important;
            color: var(--text-tertiary) !important;
        }}
        body.theme-orange [data-testid*="baseButton-like_"]:hover,
        body.theme-orange [data-testid*="baseButton-dislike_"]:hover,
        body.theme-orange [data-testid*="baseButton-share_"]:hover,
        body.theme-orange [data-testid*="baseButton-regen_"]:hover {{
            background: rgba(255,140,60,0.12) !important;
            border-color: rgba(255,154,60,0.40) !important;
            color: var(--text-primary) !important;
            box-shadow: 0 0 12px rgba(255,140,60,0.18) !important;
        }}

        body.theme-orange .zb-chat-action-btn {{
            background: rgba(255,140,60,0.07);
            border-color: rgba(255,150,70,0.20);
            color: var(--text-tertiary);
        }}

        body.theme-orange [data-testid="stChatMessage"] .stMarkdown pre {{
            background: rgba(255,140,60,0.05) !important;
            border-color: rgba(255,150,70,0.15) !important;
        }}

        body.theme-orange [data-testid="stChatInput"] {{
            background: rgba(30,19,10,0.85) !important;
            border-color: rgba(255,150,70,0.38) !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.45), 0 0 14px rgba(255,140,60,0.12) !important;
        }}
        body.theme-orange [data-testid="stChatInput"]:focus-within {{
            border-color: rgba(255,154,60,0.65) !important;
            box-shadow: 0 12px 48px rgba(0,0,0,0.70), 0 0 0 2px rgba(255,154,60,0.22) !important;
        }}
        body.theme-orange [data-testid="stChatInput"] button:hover {{
            background: #FF5C0A !important;
        }}
        body.theme-orange [data-testid="stChatInput"] textarea {{
            color: var(--text-primary) !important;
        }}
        body.theme-orange [data-testid="stChatInput"] textarea::placeholder {{
            color: var(--text-tertiary) !important;
        }}

        body.theme-orange .zb-ts {{
            color: var(--text-tertiary) !important;
        }}

        /* ==========================================================================
           ACCESSIBILITY — visible focus rings, respect reduced motion
           ========================================================================== */

        :is(button, [role="button"], a, [tabindex]):focus-visible,
        [data-testid="stChatInput"] textarea:focus-visible {{
            outline: 2px solid var(--brand) !important;
            outline-offset: 2px !important;
            border-radius: var(--radius-md) !important;
        }}

        @media (prefers-reduced-motion: reduce) {{
            *,
            *::before,
            *::after {{
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }}
        }}

        .stApp .stChatMessage + .element-container {{
            margin-top: 0 !important;
        }}
        [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"] + [data-testid="stElementContainer"] {{
            margin-top: 0 !important;
        }}

        /* ==========================================================================
           STREAMLIT INTERACTION HARDENING — tap highlight, theme snap, chip scroll
           ========================================================================== */

        /* ── Aggressively disable text selection on Streamlit buttons & children ── */
        div[data-testid="stButton"] > button,
        div[data-testid="stButton"] > button * {{
            user-select: none !important;
            -webkit-user-select: none !important;
            -moz-user-select: none !important;
            -webkit-tap-highlight-color: transparent !important;
        }}
        div[data-testid="stButton"] > button:hover {{
            cursor: pointer !important;
        }}

        /* ── Force cinematic transitions on Streamlit's root containers ── */
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stHeader"],
        [data-testid="stSidebar"] {{
            transition: background-color 0.6s cubic-bezier(0.22, 1, 0.36, 1),
                        background 0.6s cubic-bezier(0.22, 1, 0.36, 1) !important;
        }}

        /* ── Prevent ghost text: bind Streamlit text to theme tokens ── */
        [data-testid="stAppViewContainer"] p,
        [data-testid="stAppViewContainer"] h1,
        [data-testid="stAppViewContainer"] h2,
        [data-testid="stAppViewContainer"] h3 {{
            transition: color 0.4s ease-in-out !important;
            color: var(--text-primary) !important;
        }}
        [data-testid="stAppViewContainer"] button p,
        [data-testid="stAppViewContainer"] button span {{
            color: inherit !important;
        }}
        [data-testid="stAppViewContainer"] .zb-ts,
        [data-testid="stAppViewContainer"] .zb-section-label,
        [data-testid="stAppViewContainer"] .zb-conv-meta,
        [data-testid="stAppViewContainer"] .zb-conv-group-label,
        [data-testid="stAppViewContainer"] .zb-no-convs,
        [data-testid="stAppViewContainer"] .zb-followup-label,
        [data-testid="stAppViewContainer"] .zb-kbd-hint,
        [data-testid="stAppViewContainer"] .zb-sidebar-close {{
            color: var(--text-tertiary) !important;
        }}
        [data-testid="stAppViewContainer"] .zb-hero-sub {{
            color: var(--text-secondary) !important;
        }}

        /* ── Suggestion chips: single horizontal row that scrolls on mobile ── */
        [data-testid="stHorizontalBlock"] {{
            display: flex !important;
            flex-wrap: nowrap !important;
            overflow-x: auto !important;
            gap: 12px !important;
            align-items: center !important;
            justify-content: flex-start !important;
            scrollbar-width: none !important;
            -ms-overflow-style: none !important;
            padding-bottom: 4px !important;
        }}
        [data-testid="stHorizontalBlock"]::-webkit-scrollbar {{
            display: none !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-header-anchor) {{
            justify-content: space-between !important;
            overflow: visible !important;
            padding-bottom: 0 !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor, .zb-fu-anchor) > [data-testid="stColumn"],
        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor, .zb-fu-anchor) > div {{
            flex: 0 0 auto !important;
            width: auto !important;
            min-width: max-content !important;
            max-width: none !important;
            padding: 0 !important;
        }}
        [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor, .zb-fu-anchor) .stButton > button {{
            white-space: nowrap !important;
            width: auto !important;
        }}

        /* Desktop/tablet: chips + follow-ups wrap into a centered pill grid */
        @media (min-width: 769px) {{
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor, .zb-fu-anchor) {{
                flex-wrap: wrap !important;
                overflow-x: visible !important;
                justify-content: center !important;
            }}
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor, .zb-fu-anchor) > [data-testid="stColumn"],
            [data-testid="stHorizontalBlock"]:has(.zb-chips-anchor, .zb-fu-anchor) > div {{
                flex: 0 0 auto !important;
                min-width: max-content !important;
            }}
        }}

        /* ── Prevent chat messages from hiding behind the fixed input bar ── */
        .main .block-container,
        [data-testid="stAppViewBlockContainer"],
        [data-testid="stMainBlockContainer"] {{
            padding-bottom: clamp(165px, 20vh, 180px) !important;
        }}
        /* Auto-scroll (scrollIntoView block:end) aligns the last bubble's bottom
           with the VIEWPORT bottom — which sits behind the fixed chat bar. The
           scroll-margin makes the scroller stop above the bar, so no message or
           follow-up chip ever lands under the input box. */
        .stChatMessage {{
            scroll-margin-bottom: 170px;
        }}
        @media (max-width: 768px) {{
            .stChatMessage {{
                scroll-margin-bottom: 200px;
            }}
        }}

        /* ── Toasts: always above the fixed header, never hidden behind it ── */
        [data-testid="stToast"] {{
            z-index: 1000001 !important;
            top: calc(var(--header-total) + 10px) !important;
            right: 12px !important;
        }}
        @media (max-width: 480px) {{
            [data-testid="stToast"] {{
                right: 8px !important;
                left: 8px !important;
                width: auto !important;
                max-width: none !important;
            }}
        }}

        /* ── Opaque solid background for bottom chat bar so text doesn't bleed through ── */
        [data-testid="stBottom"] {{
            z-index: 9999 !important;
        }}
        [data-testid="stChatInput"] {{
            z-index: 9999 !important;
            background: var(--bg-deep, #0A0A0A) !important;
            box-shadow: 0 -8px 32px rgba(0,0,0,0.6) !important;
        }}

        /* ── About dialog — glassmorphic modal (renders above EVERYTHING, incl. chat bar) ── */
        [data-testid="stDialog"],
        div[role="dialog"] {{
            z-index: 1000000 !important;
            background: rgba(15,15,15,0.75) !important;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 20px !important;
            box-shadow: 0 24px 80px rgba(0,0,0,0.6) !important;
            overflow: hidden;
        }}
        [data-testid="stDialog"] [data-testid="stDialogScrollableContent"] {{
            padding: 18px 24px 24px 24px !important;
        }}
        [data-testid="stDialog"] h1,
        [data-testid="stDialog"] h2,
        [data-testid="stDialog"] h3,
        [data-testid="stDialog"] h4 {{
            color: var(--text-primary) !important;
        }}
        [data-testid="stDialog"] p,
        [data-testid="stDialog"] li {{
            color: var(--text-secondary) !important;
            line-height: 1.65 !important;
        }}
        [data-testid="stDialog"] li {{
            margin-bottom: 6px !important;
        }}
        [data-testid="stDialog"] .stButton > button {{
            border-radius: var(--radius-full) !important;
            border: 1px solid rgba(255,133,51,0.4) !important;
            background: rgba(255,133,51,0.12) !important;
            color: var(--text-primary) !important;
            font-weight: var(--fw-semibold) !important;
            transition: all var(--transition-fast) !important;
        }}
        [data-testid="stDialog"] .stButton > button:hover {{
            background: rgba(255,133,51,0.22) !important;
            box-shadow: 0 8px 24px rgba(255,133,51,0.2) !important;
        }}

        /* ── About dialog — mobile: viewport-filling, scrollable top-to-bottom ──
           Root cause on phones: Streamlit centers stDialog with
           top:50% + translate(-50%,-50%); content taller than the viewport
           extends ABOVE the screen, so the top is clipped and the user must
           fight the page scroll. On mobile we pin the dialog to the viewport
           (100dvh), drop the centering transform, and let the WHOLE overlay
           scroll (Streamlit 1.48 has no inner stDialogScrollableContent node —
           the overlay itself is the only scroll container). Desktop keeps the
           existing centered card. */
        @media (max-width: 768px) {{
            [data-testid="stDialog"] {{
                top: 0 !important;
                left: 0 !important;
                right: 0 !important;
                bottom: 0 !important;
                width: 100vw !important;
                max-width: 100vw !important;
                height: 100dvh !important;
                max-height: 100dvh !important;
                margin: 0 !important;
                transform: none !important;
                border-radius: 0 !important;
                display: block !important;
                overflow-y: auto !important;
                -webkit-overflow-scrolling: touch !important;
                overscroll-behavior: contain !important;
                padding-bottom: env(safe-area-inset-bottom, 0px) !important;
            }}
            /* Older Streamlit builds: dedicated scrollable node — scrolls internally */
            [data-testid="stDialog"] [data-testid="stDialogScrollableContent"] {{
                flex: 1 1 auto !important;
                min-height: 0 !important;
                height: auto !important;
                max-height: none !important;
                overflow-y: auto !important;
                -webkit-overflow-scrolling: touch !important;
                overscroll-behavior: contain !important;
                padding: calc(env(safe-area-inset-top, 0px) + 16px) 20px
                         calc(env(safe-area-inset-bottom, 0px) + 24px) 20px !important;
            }}
            /* Background page must not scroll while the dialog is open */
            body:has([data-testid="stDialog"]) {{
                overflow: hidden !important;
                overscroll-behavior: none !important;
            }}
            /* Chat bar suppressed while the dialog exists in the DOM (⇔ open) */
            body:has([data-testid="stDialog"]) [data-testid="stBottom"],
            body:has([data-testid="stDialog"]) [data-testid="stBottom"] > div,
            body:has([data-testid="stDialog"]) [data-testid="stBottom"] *,
            body:has([data-testid="stDialog"]) [data-testid="stChatInput"] {{
                visibility: hidden !important;
                opacity: 0 !important;
                pointer-events: none !important;
                z-index: 100 !important;
            }}
        }}
        </style>

        <script>
        /* ── Navigation + smart header runtime (init once; survives reruns) ── */
        window.__zbNavInit = window.__zbNavInit || (function() {{
            var zbLastNav = 0;

            /* Sidebar drawer — explicit set + lock so pointerup+click double-fire is harmless */
            function zbNavLock() {{
                var now = Date.now();
                if (now - zbLastNav < 250) return true;
                zbLastNav = now;
                return false;
            }}
            window.zbSetSidebar = function(open) {{
                if (zbNavLock()) return;
                zbSidebarFreeze(450);
                document.body.classList.toggle('sidebar-open', !!open);
            }};
            /* Slide-transition guard: while a manual open/close transition is running
               (300ms), the auto-sync would see mid-animation geometry and undo the
               request. Freeze the sync until the transition has finished, then let
               the real geometry be the authority again. */
            var zbSidebarFreezeUntil = 0;
            function zbSidebarFreeze(ms) {{
                zbSidebarFreezeUntil = Date.now() + ms;
            }}
            function zbSyncSidebar() {{
                var sb = document.querySelector('[data-testid="stSidebar"]');
                if (!sb) return;
                if (Date.now() < zbSidebarFreezeUntil) return; /* mid-transition — leave the class alone */
                var rect = sb.getBoundingClientRect();
                var open = rect.right > rect.width * 0.2;
                var was = document.body.classList.contains('sidebar-open');
                document.body.classList.toggle('sidebar-open', open);
                /* Reopen tab visibility follows the real geometry only (never the
                   Python one-shot class, so it cannot flash on reruns) */
                document.body.classList.toggle('sidebar-tab-visible', !open);
                if (open && !was) {{
                    /* Always open from the top of the chat list */
                    sb.scrollTop = 0;
                    var c = document.querySelector('[data-testid="stSidebarContent"]');
                    if (c) c.scrollTop = 0;
                }}
            }}
            zbSidebarFreeze(500); /* first load: let the initial class render untouched */
            window.__zbSidebarFreeze = function(ms) {{ zbSidebarFreeze(ms); }};
            /* Dialog: snap the scrollable content to the top on first open */
            var zbDialogWasOpen = false;
            function zbSyncDialog() {{
                var d = document.querySelector('[data-testid="stDialog"]');
                var open = !!d;
                if (open && !zbDialogWasOpen) {{
                    var c = d.querySelector('[data-testid="stDialogScrollableContent"]') || d;
                    if (c) setTimeout(function() {{ c.scrollTop = 0; }}, 80);
                }}
                zbDialogWasOpen = open;
            }}
            if (window.MutationObserver) {{
                new MutationObserver(function() {{
                    setTimeout(zbSyncSidebar, 60);
                    setTimeout(zbSyncDialog, 60);
                }})
                    .observe(document.documentElement, {{
                        childList: true, subtree: true, attributes: true,
                        attributeFilter: ['class', 'style', 'aria-hidden'],
                    }});
            }}
            setInterval(zbSyncSidebar, 500);
            setInterval(zbSyncDialog, 500);
            /* Click any real Streamlit button by key (drives drawer closes through reruns) */
            window.zbClickNav = function(key) {{
                var el = document.querySelector('button[data-testid*="' + key + '"]');
                if (el) el.click();
            }};

            /* Smart header: hide on scroll down, show on scroll up */
            var lastY = 0;
            function zbOnScroll() {{
                var y = window.scrollY || document.documentElement.scrollTop || 0;
                if (y > 150 && y > lastY + 4) document.body.classList.add('scrolled-down');
                else if (y < lastY - 4 || y < 150) document.body.classList.remove('scrolled-down');
                lastY = y;
            }}
            window.addEventListener('scroll', zbOnScroll, {{ passive: true }});
            var zbMainEl = document.querySelector('section.main');
            if (zbMainEl) zbMainEl.addEventListener('scroll', zbOnScroll, {{ passive: true }});

            /* Show header actions while typing, hide 2s after a message is sent */
            document.addEventListener('focusin', function(e) {{
                if (e.target && e.target.matches && e.target.matches('[data-testid="stChatInput"] textarea')) {{
                    document.body.classList.add('input-focus');
                }}
            }});
            document.addEventListener('focusout', function(e) {{
                if (e.target && e.target.matches && e.target.matches('[data-testid="stChatInput"] textarea')) {{
                    setTimeout(function() {{
                        var a = document.activeElement;
                        if (!a || !a.closest('[data-testid="stChatInput"]')) document.body.classList.remove('input-focus');
                    }}, 2000);
                }}
            }});

            /* Auto-scroll to bottom only when already near the bottom */
            function zbAutoScroll() {{
                var main = document.querySelector('section.main');
                var h = main ? main.scrollHeight : document.body.scrollHeight;
                if (h - (window.innerHeight + (window.scrollY || 0)) < 180) {{
                    window.scrollTo({{ top: h, behavior: 'smooth' }});
                    if (main) main.scrollTop = main.scrollHeight;
                }}
            }}

            /* New message → keep nav visible 2s, then hide (spec: sent → wait 2s → hide) */
            var zbChatCount = 0;
            var zbMsgWatcher = new MutationObserver(function() {{
                var n = document.querySelectorAll('.stChatMessage').length;
                if (n > zbChatCount) {{
                    zbChatCount = n;
                    document.body.classList.add('input-focus');
                    setTimeout(function() {{ document.body.classList.remove('input-focus'); }}, 2000);
                    zbAutoScroll();
                }}
            }});

            /* ESC closes everything */
            document.addEventListener('keydown', function(e) {{
                if (e.key === 'Escape') {{
                    window.zbClickNav('zb_backdrop_menu');
                    window.zbClickNav('zb_backdrop_panel');
                    zbSidebarFreeze(450);
                    document.body.classList.remove('sidebar-open');
                }}
            }});

            /* Swipe-to-close drawers */
            var zbSwipe = null;
            document.addEventListener('touchstart', function(e) {{
                if (e.touches && e.touches[0]) {{
                    zbSwipe = {{ x: e.touches[0].clientX, y: e.touches[0].clientY }};
                }}
            }}, true);
            document.addEventListener('touchend', function(e) {{
                if (!zbSwipe || !e.changedTouches[0]) {{ zbSwipe = null; return; }}
                var dx = e.changedTouches[0].clientX - zbSwipe.x;
                var dy = e.changedTouches[0].clientY - zbSwipe.y;
                zbSwipe = null;
                if (Math.abs(dx) < 60 || Math.abs(dy) > Math.abs(dx)) return;
                if (dx < 0 && document.querySelector('.zb-menu-anchor')) window.zbClickNav('zb_backdrop_menu');
                if (dx > 0 && document.querySelector('.zb-panel-anchor')) window.zbClickNav('zb_backdrop_panel');
            }}, true);

            /* Sidebar close button + reopen tab + tap-outside-to-close (mobile) */
            document.addEventListener('click', function(e) {{
                if (!e.target || !e.target.closest) return;
                if (e.target.closest('[data-zb-action="close"]')) {{
                    zbSidebarFreeze(450);
                    document.body.classList.remove('sidebar-open');
                    e.preventDefault();
                    return;
                }}
                if (e.target.closest('[data-zb-action="open-sidebar"]')) {{
                    zbSidebarFreeze(450);
                    document.body.classList.add('sidebar-open');
                    var c = document.querySelector('[data-testid="stSidebarContent"]');
                    if (c) setTimeout(function() {{ c.scrollTop = 0; }}, 120);
                    e.preventDefault();
                    return;
                }}
                if (window.innerWidth < 768) {{
                    var sb = document.querySelector('[data-testid="stSidebar"]');
                    if (sb && !sb.contains(e.target) && document.body.classList.contains('sidebar-open')) {{
                        zbSidebarFreeze(450);
                        document.body.classList.remove('sidebar-open');
                    }}
                }}
            }});

            document.addEventListener('DOMContentLoaded', function() {{
                zbChatCount = document.querySelectorAll('.stChatMessage').length;
                setTimeout(zbAutoScroll, 100);
                setTimeout(zbAutoScroll, 500);
                var target = document.querySelector('section.main') || document.body;
                zbMsgWatcher.observe(target, {{ childList: true, subtree: true, characterData: true }});
            }});
            return true;
        }})();
        </script>
        """,
        unsafe_allow_html=True
    )

    # No-JS theme fallback: re-bind the palette on :root straight from Python when
    # the orange theme is active. CSS :root overrides win by cascade, and the
    # <style> element disappears on dark runs — zero dependence on body classes.
    theme = st.session_state.get("theme", "dark")
    if theme == "orange":
        st.markdown(
            """
            <style>
            :root {
                --bg-deep          : #1D130D;
                --bg-surface       : rgba(255,140,60,0.07);
                --bg-card          : rgba(255,140,60,0.08);
                --bg-elevated      : rgba(255,140,60,0.11);
                --bg-hover         : rgba(255,140,60,0.15);
                --border-subtle    : rgba(255,150,70,0.14);
                --border-light     : rgba(255,150,70,0.22);
                --border-medium    : rgba(255,150,70,0.32);
                --text-primary     : #F3E4D0;
                --text-secondary   : rgba(243,228,208,0.62);
                --text-tertiary    : rgba(243,228,208,0.38);
                --brand            : #FF9A3C;
                --brand-glow       : rgba(255,154,60,0.35);
                --green            : #FF9A3C;
                --green-glow       : rgba(255,154,60,0.45);
                --shadow-sm        : 0 1px 2px rgba(255,120,40,0.10);
                --shadow-md        : 0 4px 12px rgba(255,120,40,0.14);
                --shadow-lg        : 0 8px 24px rgba(0,0,0,0.35);
                --shadow-xl        : 0 16px 48px rgba(0,0,0,0.45);
            }
            html, body { background: #1D130D !important; }
            [data-testid="stAppViewContainer"] {
                background:
                    radial-gradient(1100px 700px at 85% -10%, rgba(255,140,60,0.14), transparent 60%),
                    radial-gradient(900px 650px at 5% 110%, rgba(255,90,40,0.10), transparent 60%),
                    #1D130D !important;
            }
            .zb-hero-title {
                background: linear-gradient(180deg, #FFC49A 20%, #FF9A3C 100%);
                -webkit-background-clip: text;
                background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            [data-testid="stChatInput"] textarea { color: #F3E4D0 !important; }
            [data-testid="stChatInput"] textarea::placeholder { color: rgba(243,228,208,0.38) !important; }
            </style>
            """,
            unsafe_allow_html=True
        )