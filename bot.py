import os
import asyncio
from telethon import TelegramClient, events

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE_NUMBER')

client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start(phone=phone)
    print("Bot started... Listening for messages.")

    @client.on(events.NewMessage)
    async def handler(event):
        text = event.raw_text.lower()
        # Customize your keywords here to detect visa slot openings
        if "visa slot open" in text or "f-1 slot available" in text:
            print("Visa slot alert detected!")
            # Here, add your notification logic, e.g. send email or desktop notification

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
