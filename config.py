import logging

# 1. Platform & Version Constants
PLATFORM_NAME = "ZINGYBYTE"
VERSION = "2.0.0"

# 2. Model Configuration
DEFAULT_MODEL = "groq/compound-mini"

# 3. Streamlit Page Configuration
PAGE_CONFIG = {
    "page_title": "ZingyByte AI — Your Food Buddy",
    "page_icon": "🍔",
    "layout": "wide"
}

# 4. Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ZingyByteApp")