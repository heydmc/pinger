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
    urls = [
        "https://telegram-bot-6uyz.onrender.com",     # Existing bot
        "https://chess-membership-bot.onrender.com",      # 🔁 Add new bot URL here
    ]
    
    while True:
        for url in urls:
            try:
                print(f"Pinging {url} ...")
                response = requests.get(url)
                print(f"Status from {url}: {response.status_code}")
            except Exception as e:
                print(f"Error pinging {url}: {e}")
        time.sleep(60)  # 1 minutes

if __name__ == "__main__":
    threading.Thread(target=ping_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
