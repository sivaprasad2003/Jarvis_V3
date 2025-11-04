# backend/config.py
"""
Central config for Jarvis_V3.
"""
import os

# Google Gemini API (from original Jarvis repo)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")

# HuggingFace cookie path (optional, from V2 repo)
HF_COOKIE_PATH = os.getenv("HF_COOKIE_PATH", "backend/cookie.json")

# Hotword model / constants
HOTWORD_TRIGGER = "jarvis"

# Other local settings
VOICE_RATE = 150
VOICE_VOLUME = 1.0
