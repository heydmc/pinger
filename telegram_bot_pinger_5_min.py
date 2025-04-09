import requests
from flask import Flask
import os

app = Flask(__name__)

# URLs for your bots
BOT_1_URL = "https://telegram-bot-6uyz.onrender.com"
BOT_2_URL = "https://chess-membership-bot.onrender.com"

def ping_bot_1():
    try:
        print(f"Pinging Bot 1: {BOT_1_URL} ...")
        response = requests.get(BOT_1_URL, timeout=15)
        print(f"Bot 1 Response: {response.status_code} - {response.text[:100]}")
    except Exception as e:
        print(f"Bot 1 Ping Failed: {e}")

def ping_bot_2():
    try:
        print(f"Pinging Bot 2: {BOT_2_URL} ...")
        response = requests.get(BOT_2_URL, timeout=15)
        print(f"Bot 2 Response: {response.status_code} - {response.text[:100]}")
    except Exception as e:
        print(f"Bot 2 Ping Failed: {e}")

@app.route("/")
def home():
    return "Pinger is ready! Hit /ping1 or /ping2"

@app.route("/ping1")
def ping1():
    ping_bot_1()
    return "Pinged Bot 1"

@app.route("/ping2")
def ping2():
    ping_bot_2()
    return "Pinged Bot 2"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
