#just edit lines that have word "your"
#the librarys or pip command you have to write in terminal is between the quotation 'pip install telethon'

from telethon import TelegramClient, events

api_id = 94575
api_hash = 'a3406de8d171bb422bb6ddf3bbd800e2'
bot_token = "your token"
bot = TelegramClient('bot', api_id, api_hash)

MONITOR_CHANNEL = 'your channel id with no @'

@bot.on(events.NewMessage(chats=MONITOR_CHANNEL))
async def monitor_channel(event):
    try:
        # check no forward messages
        if event.fwd_from:
            return

        # text of message
        message_text = event.text or ""

        #if have id, do not change it
        if "your channel id with @" not in message_text:
            new_text = message_text + "\n\nyour channel id with @" if message_text.strip() else "your channel id with @"
            await bot.edit_message(MONITOR_CHANNEL, event.id, new_text)
            print(f"changed {event.id} successfully.")

    except Exception as e:
        print(f"error: {e}")

async def main():
    await bot.start(bot_token=bot_token)
    print("has done")
    await bot.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())