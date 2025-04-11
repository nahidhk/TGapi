import json
from telethon.sync import TelegramClient

with open("config.json") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]

client = TelegramClient('my_session', api_id, api_hash)
client.start()



# যেই চ্যানেল থেকে মেসেজ আনতে চাও, তার username বা ID দাও
channel_username = 'EarningHerop24'  # যেমন: 'BBCNews'

# শেষ ১০০টা মেসেজ আনছে (limit বাড়াতে পারো)
for message in client.iter_messages(channel_username, limit=1000):
    print(f"Message ID: {message.id}")
    print(f"Date: {message.date}")
    print(f"Text: {message.text}")
    print("-" * 40)
