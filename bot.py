import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]
chat_id = os.environ["CHAT_ID"]

async def main():
    with open("session/session.txt", "r") as f:
        session_str = f.read()
    client = TelegramClient(StringSession(session_str), api_id, api_hash)
    await client.start()
    print("✅ Logged in and running bot...")

    # Replace this with your slot-checking logic
    found_slots = True  # Simulated
    if found_slots:
        await client.send_message(chat_id, "✅ F1 Visa Slot Available!")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
