# backend/chat_integration.py
# Thin wrapper that chooses between Gemini (if API key) or a local HuggingFace path.
import json
from .config import GEMINI_API_KEY, HF_COOKIE_PATH

def ask_gemini(prompt):
    # Placeholder: integrate with Google Generative API using GEMINI_API_KEY
    # Keep minimal so the repository is runnable without keys.
    if not GEMINI_API_KEY or "YOUR_GEMINI_API_KEY" in GEMINI_API_KEY:
        return "Gemini API key not configured. Please set GEMINI_API_KEY."
    # (Integration code goes here)
    return "Gemini response (placeholder)"

def ask_hf(prompt):
    # Placeholder: attempt to use a local cookie-based HuggingFace chat
    try:
        with open(HF_COOKIE_PATH, "r") as f:
            cookies = json.load(f)
        # Use cookies + requests to call huggingface chat UI endpoints (user to implement)
        return "HuggingFace chat response (placeholder)"
    except FileNotFoundError:
        return "HuggingFace cookie.json missing; place your cookie JSON at backend/cookie.json"

def ask(prompt):
    # prefer Gemini if configured, fallback to HF
    if GEMINI_API_KEY and "YOUR_GEMINI_API_KEY" not in GEMINI_API_KEY:
        return ask_gemini(prompt)
    return ask_hf(prompt)
