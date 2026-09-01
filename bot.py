import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{TOKEN}/sendPoll"

data = {
    "chat_id": CHAT_ID,
    "question": "🎮 امشب ماینکرفت بازی می‌کنید؟",
    "options": '["✅ آره", "❌ نه"]',
    "is_anonymous": False
}

requests.post(url, data=data)
