# 🤖 Telegram Bot (Python)

हा टेलिग्राम बॉट **Arena.ai MCP Agent** द्वारे स्वयंचलितपणे तयार केला गेला आहे.

## 🚀 फीचर्स (Features)
- `/start` आणि `/help` कमांड्सला प्रतिसाद देतो.
- `/about` कमांडद्वारे बॉटची माहिती देतो.
- युझरने पाठवलेला मेसेज पुन्हा पाठवतो (Echo).

---

## 🛠️ कसं रन करायचं? (How to Run)

### १. प्रोजेक्ट क्लोन करा (Clone the repository)
```bash
git clone https://github.com/jogdandkrishna-hash/telegram-bot-python.git
cd telegram-bot-python
```

### २. व्हर्च्युअल एन्व्हायरमेंट तयार करा (Create Virtual Environment)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### ३. लायब्ररीज इन्स्टॉल करा (Install dependencies)
```bash
pip install -r requirements.txt
```

### ४. Environment Variables सेट करा (Setup Token)
एक `.env` फाईल बनवा आणि त्यात तुमचा टेलिग्राम बॉट टोकन टाका:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```
*(टीप: टेलिग्रामवर [@BotFather](https://t.me/BotFather) कडून तुम्ही नवीन बॉट टोकन मिळवू शकता)*

### ५. बॉट रन करा (Run the bot)
```bash
python bot.py
```

---
Made with ❤️ by Arena.ai MCP Agent
