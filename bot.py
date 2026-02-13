import os
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, DOWNLOAD_PATH

# Make sure download folder exists
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

app = Client(
    "video_downloader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# /start command
@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        "Welcome!\n\n"
        "Send /link <telegram_post_link> to download a video.\n"
        "Example:\n"
        "/link https://t.me/channelname/123"
    )

# /link command
@app.on_message(filters.command("link"))
async def link_cmd(client, message):
    if len(message.command) < 2:
        await message.reply_text("❌ Please provide a Telegram post link after /link")
        return

    link = message.command[1]
    user_id = message.chat.id

    try:
        parts = link.split("/")
        chat = parts[3]
        msg_id = int(parts[-1])

        msg = await app.get_messages(chat, msg_id)

        if not msg.video:
            await message.reply_text("❌ No video found in this link.")
            return

        await message.reply_text("⏳ Downloading video...")

        # Download video
        path = await msg.download(file_name=DOWNLOAD_PATH)

        # Send back to user
        await app.send_video(chat_id=user_id, video=path, caption="✅ Here is your video!")

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")

# Run bot
if __name__ == "__main__":
    app.run()
