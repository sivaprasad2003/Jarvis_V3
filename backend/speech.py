# backend/speech.py
# Minimal TTS + speech recognition wrapper (merge of both repos)
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
from .config import VOICE_RATE, VOICE_VOLUME
engine.setProperty("rate", VOICE_RATE)
engine.setProperty("volume", VOICE_VOLUME)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_time_limit=7):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            return r.recognize_google(audio)
        except Exception as e:
            return ""
