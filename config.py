import logging

# 1. Platform & Version Constants
PLATFORM_NAME = "ZINGYBYTE"
VERSION = "2.0.0"

# 2. Model Configuration
OLLAMA_BASE_URL = "http://localhost:11434" # Ensure this matches your Ollama port
DEFAULT_MODEL = "llama3"  # Or "llama3.1", "mistral", etc.
AVAILABLE_MODELS = ["llama3", "mistral", "gemma"] 

# 3. Streamlit Page Configuration
PAGE_CONFIG = {
    "page_title": "ZingyByte AI — Smart Serve",
    "page_icon": "🍔",
    "layout": "wide"
}

# 4. Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ZingyByteApp")