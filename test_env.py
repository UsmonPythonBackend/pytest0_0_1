import os
from dotenv import load_dotenv

load_dotenv()

def test_env():
    base_url = os.getenv('BASE_URL')

    print(base_url)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN or not CHAT_ID:
    print("⚠️ Внимание: TELEGRAM_BOT_TOKEN не задан.")
