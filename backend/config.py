# backend/config.py
"""
Central config for Jarvis_V3.
"""
import os
from pathlib import Path

# Google Gemini API (from original Jarvis repo)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")

# HuggingFace cookie path (optional, from V2 repo)
HF_COOKIE_PATH = str(Path(__file__).resolve().parent / "cookie.json")


# Hotword model / constants
HOTWORD_TRIGGER = "jarvis"

# Other local settings
VOICE_RATE = 150
VOICE_VOLUME = 1.0

# Absolute path to .../Jarvis_V3/frontend
FRONTEND_DIR = str(Path(__file__).resolve().parents[1] / "frontend")
