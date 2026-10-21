import logging

# 1. Platform & Version Constants
PLATFORM_NAME = "ZINGYBYTE"
VERSION = "2.0.0"

# 2. Model Configuration
DEFAULT_MODEL = "openai/gpt-oss-20b"
FALLBACK_MODELS = [
    "openai/gpt-oss-20b",
    "qwen/qwen3.8-27b",
    "openai/gpt-oss-120b",
]

AVAILABLE_MODELS = {
    "⚡ Auto (Unlimited Failover)": "auto",
    "🚀 GPT OSS 20B (Ultra-fast)": "openai/gpt-oss-20b",
    "🎯 Qwen 3.8 27B (High Accuracy)": "qwen/qwen3.8-27b",
    "🧠 GPT OSS 120B (Deep Reasoning)": "openai/gpt-oss-120b",
}

# 3. Streamlit Page Configuration
PAGE_CONFIG = {
    "page_title": "ZingyByte AI — Your Food Buddy",
    "page_icon": "🍔",
    "layout": "wide"
}

# 4. Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ZingyByteApp")
