# 📹 Telegram Video Downloader Bot

**Simple Python bot for downloading videos and other media from Telegram channels/groups.**  
🚀 Lightweight, beginner-friendly, and easy to set up! 🐍💻  

---

## 🔹 Features

- `/start` – Greet users and explain usage  
- `/link <telegram_post_link>` – Download media from a Telegram post link  
- Supports **video, audio, and documents**  
- Saves files locally in organized folders:  
  - `downloads/videos/`  
  - `downloads/audio/`  
  - `downloads/documents/`  
- Automatically forwards downloaded files to a **target chat ID**  
- Works with **private and public channels/groups** if the bot has access  

---

## ⚡ Requirements

- Python 3.10+  
- [Pyrogram 2.x](https://docs.pyrogram.org/)  
- `tgcrypto`  
- `python-dotenv`  

Install requirements:

```bash
pip install -r requirements.txt
```
### 🛠 Installation
Clone the repository:
```bash
git clone https://github.com/KAWDHITHA-NIRMAL/Telegram-Video-Downloader
```

- Install dependencies:
```bash
pip install -r requirements.txt
```
- Create a .env file with your credentials:
```ini
API_ID=your_api_id  #https://my.telegram.org
API_HASH=your_api_hash # https://my.telegram.org
BOT_TOKEN=your_bot_token #https://t.me/BotFather
TARGET_CHAT_ID=-1001234567890 #https://t.me/ChatidTelegramBot

```
#### 🚀 Usage

* Start the bot:
```bash
python bot.py
```

* Open Telegram and start your bot with /start:
```bash
/start
```

* Download media using /link with the post link:
```bash
/link https://t.me/channelusername/123
```
> The bot will download the media and forward it to the TARGET_CHAT_ID. ✅

##### 📁 Folder Structure
```bash
telegram_video_bot/
├── bot.py                # Main bot script
├── config.py             # Configuration & folder setup
├── requirements.txt      # Python dependencies
├── downloads/            # Media download folder
│   ├── videos/
│   ├── audio/
│   └── documents/
├── .env                  # Environment variables (API keys, target chat)
└── README.md             # Project documentation
```

###### 🌟 Supported Media

- Video (.mp4, .mkv, .mov)
- Audio (.mp3, .ogg, .wav)
- Documents (.pdf, .txt, .zip, etc.)
> Any other media types supported by Telegram can also be forwarded.

### 💡 Notes
- The bot can’t access messages in private channels/groups unless added as a member/admin.
- Maximum file size is limited by Telegram bot API (~2 GB).
- Folder paths are configurable in config.py.

### 🎨 Future Improvements
- Auto-delete downloaded files after forwarding to save disk space
- Handle multiple links in a single message
- Add download progress bar
- Deploy with Docker for easy hosting

### 🐍 Beginner Tips

- Keep your .env file private and never share API keys.
- Make sure the bot has permission to read messages in channels/groups.
- Test with a public channel first to ensure everything works.

---

## 👨‍💻 Creator Info

```json
{
  "creator": "K. Nirmal",
  "role": "CodeXSL Developer"
}
```

---

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px;">
  <a href="https://whatsapp.com/channel/0029VatTpZU7oQhkw1WbZS0B" target="_blank"><img src="https://social-card-codex.vercel.app/api?channellink=https%3A%2F%2Fwhatsapp.com%2Fchannel%2F0029VatTpZU7oQhkw1WbZS0B&theme=dark&overrideVerified=true&overrideVerifiedIcon=https%3A%2F%2Fstatic.whatsapp.net%2Frsrc.php%2Fv4%2FyM%2Fr%2FSGDtYg_EYce.png" alt="CodeX Developers" style="width: 300px; max-width: 100%; height: auto;" /></a>
  <a href="https://t.me/codex_developer" target="_blank"><img src="https://telegram-card.vercel.app/?username=codex_developer&theme=dark" alt="CodeX Developers tg" style="width: 300px; max-width: 100%; height: auto;" /></a>
</div>
