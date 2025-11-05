# backend/chat_integration.py
import os
import json
import requests

from .config import GEMINI_API_KEY, HF_COOKIE_PATH

# ------------ Gemini (placeholder -> optional real call later) ------------
def ask_gemini(prompt: str) -> str:
    if not GEMINI_API_KEY or "YOUR_GEMINI_API_KEY" in GEMINI_API_KEY:
        return None  # signal "not configured"
    # Minimal placeholder so the app runs. Replace with real Gemini call if you like.
    return f"[Gemini placeholder] You asked: {prompt}"

# ------------ Hugging Face Inference API (recommended) ------------
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")  # set this env var

# Choose a default chat/instruct model you like
HF_DEFAULT_MODEL = os.getenv("HF_MODEL", "meta-llama/Llama-3-8b-instruct")

def ask_hf_api(prompt: str) -> str:
    if not HF_TOKEN:
        return None  # signal "not configured"
    url = f"https://api-inference.huggingface.co/models/{HF_DEFAULT_MODEL}"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()
        # Common response shapes:
        if isinstance(data, list) and data and isinstance(data[0], dict):
            if "generated_text" in data[0]:
                return data[0]["generated_text"]
            if "summary_text" in data[0]:
                return data[0]["summary_text"]
        # Text-generation-inference sometimes returns a dict with "generated_text"
        if isinstance(data, dict) and "generated_text" in data:
            return data["generated_text"]
        # Fallback: stringify first 2k chars
        return json.dumps(data, ensure_ascii=False)[:2000]
    except Exception as e:
        return f"HuggingFace Inference API error: {e}"

# ------------ Cookie fallback (unofficial; just confirms load) ------------
def ask_hf_cookie(prompt: str) -> str:
    try:
        with open(HF_COOKIE_PATH, "r", encoding="utf-8") as f:
            cookies = json.load(f)  # dict {name: value}
        if not isinstance(cookies, dict) or not cookies:
            return "cookie.json present but empty/invalid (expected JSON object)."
        known = ", ".join(cookies.keys())
        # Here we just confirm cookie load. Implementing the unofficial web calls is brittle;
        # prefer the official API above. If you insist, I can wire requests to the web UI.
        return f"Loaded cookies: {known}. (Using official API is recommended; set HUGGINGFACEHUB_API_TOKEN.)"
    except FileNotFoundError:
        return "HuggingFace cookie.json missing; place your cookie JSON at backend/cookie.json"
    except Exception as e:
        return f"Failed to load cookie.json: {e}"

# ------------ Router ------------
def ask(prompt: str) -> str:
    # 1) Gemini if configured
    resp = ask_gemini(prompt)
    if isinstance(resp, str):
        return resp
    # 2) Hugging Face official API if token present
    resp = ask_hf_api(prompt)
    if isinstance(resp, str):
        return resp
    # 3) Fallback: cookies (just acknowledge)
    return ask_hf_cookie(prompt)
