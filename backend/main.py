# backend/main.py
import eel
import threading
from .speech import speak, listen
from .chat_integration import ask
from .config import HOTWORD_TRIGGER

FRONTEND_DIR = '../frontend'

eel.init(FRONTEND_DIR)

@eel.expose
def ask_chat(message):
    "Called from the frontend to get an assistant reply."
    resp = ask(message)
    return resp

@eel.expose
def tts_say(text):
    speak(text)
    return "ok"

def assistant_loop():
    # Simple hotword loop (blocking)
    while True:
        print("Listening for hotword...")
        text = listen(timeout=6, phrase_time_limit=4).lower()
        if not text:
            continue
        print("Heard:", text)
        if HOTWORD_TRIGGER in text:
            speak("Yes?")
            query = listen(timeout=6, phrase_time_limit=8)
            if not query:
                speak("I didn't catch that.")
                continue
            reply = ask(query)
            speak(reply)

def start_assistant_loop_in_thread():
    t = threading.Thread(target=assistant_loop, daemon=True)
    t.start()

def start_app():
    start_assistant_loop_in_thread()
    eel.start('index.html', size=(900,700))

if __name__ == "__main__":
    start_app()
