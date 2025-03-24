import time
import requests
from flask import Flask
import threading
import os

app = Flask(__name__)

TELEGRAM_BOT_URL = "https://telegram-bot-6uyz.onrender.com"

@app.route("/")
def home():
    return "Pinger is running!"

def ping_bot():
    while True:
        try:
            print("Pinging bot...")
            response = requests.get(TELEGRAM_BOT_URL)
            print(f"Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(300)  # 5 minutes

if __name__ == "__main__":
    threading.Thread(target=ping_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
