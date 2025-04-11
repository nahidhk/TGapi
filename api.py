from telethon.sync import TelegramClient
import json
import os
# 📜 Telegram API configuration
# 🔍 Check if config.json already exists
if os.path.exists("config.json"):
    with open("config.json", "r") as f:
        config = json.load(f)
        api_id = config["api_id"]
        api_hash = config["api_hash"]
else:
    # 🔐 যদি না থাকে তাহলে ইনপুট নাও
    api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API Hash: ")

    # 📂 Save to config.json
    with open("config.json", "w") as f:
        json.dump({"api_id": api_id, "api_hash": api_hash}, f, indent=4)
    print("✅ Saved API info to config.json")

# 🚀 Telegram client start
with TelegramClient('my_session', api_id, api_hash) as client:
    me = client.get_me()
    print("\n🧾 Account Info:")
    print(me.stringify())
