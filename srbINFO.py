# This is a next update

import json
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannel

# 🔐 Load config from JSON
with open("config.json") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]

# ⚙️ Start client
client = TelegramClient('my_session', api_id, api_hash)
client.start()

# 🔍 Channel username
channel_username = ''

# 📦 Get channel info
channel_entity = client.get_entity(channel_username)
full_info = client(GetFullChannel(channel=channel_entity))

# 🧾 Extract info
channel_basic = full_info.chats[0]
channel_extra = full_info.full_chat

# ✅ Display info nicely
channel_data = {
    "name": channel_basic.title,
    "username": channel_basic.username,
    "id": channel_basic.id,
    "access_hash": str(channel_basic.access_hash),
    "created_date": str(channel_basic.date),
    "is_verified": channel_basic.verified,
    "is_scam": channel_basic.scam,
    "is_megagroup": channel_basic.megagroup,
    "description": channel_extra.about,
    "participants_count": channel_extra.participants_count,
    "linked_chat_id": channel_extra.linked_chat_id,
    "default_banned_rights": str(channel_extra.default_banned_rights),
    "pinned_msg_id": channel_extra.pinned_msg_id,
}

# 🖨️ Pretty Print to console
print("\n📊 Telegram Channel Info:\n")
print(json.dumps(channel_data, indent=2, ensure_ascii=False))
