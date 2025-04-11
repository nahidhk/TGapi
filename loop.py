from telethon.sync import TelegramClient
import json
import time  # Delay দিতে চাইলে

# 🔐 config.json থেকে API লোড
with open("config.json") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]

# ✅ Telegram client start
client = TelegramClient('my_session', api_id, api_hash)
client.start()

# 🎯 Receiver Username বা ID (যাকে পাঠাতে চাও)
receiver = input("Input UserName: ")
mymessege = input("Input Message: ")
loopnum = int(input("Input Loop Number: "))

for i in range(1, loopnum + 1):  # 1 থেকে loopnum পর্যন্ত
    message = f"{mymessege} {i}"  # বার্তা তৈরি
    client.send_message(receiver, message)
    print(f"✅ Sent: {message}")
    time.sleep(1)  # এক সেকেন্ড delay (spamming যেন না হয়)
