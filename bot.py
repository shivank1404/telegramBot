import os
import asyncio
from telethon import TelegramClient, events

# Load config from environment variables for security and flexibility
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE_NUMBER')

client = TelegramClient('session', api_id, api_hash)

async def send_telegram_message(client, user_id, message):
    """Send a Telegram message to the given user_id (can be int ID or '@username')."""
    await client.send_message(user_id, message)

async def main():
    print("Starting Telegram client...")
    await client.start(phone=phone)
    print("Client started. Getting your user ID...")
    
    me = await client.get_me()
    my_user_id = me.id  # numeric user ID or you can use '@username'

    print(f"Your user ID is {my_user_id}. Bot is listening for visa slot alerts...")

    @client.on(events.NewMessage)
    async def handler(event):
        text = event.raw_text.lower()
        # Keywords you want to track (customize as needed)
        keywords = ["visa slot open", "f-1 slot available", "f1 visa slot"]
        if any(keyword in text for keyword in keywords):
            print("Visa slot alert detected!")
            alert_message = f"🚨 F-1 Visa Slot Alert!\n\nMessage:\n{text}"
            try:
                await send_telegram_message(client, my_user_id, alert_message)
                print("Notification sent to your Telegram.")
            except Exception as e:
                print(f"Failed to send notification: {e}")

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
