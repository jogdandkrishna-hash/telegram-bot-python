import os
import telebot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize bot with Token
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not API_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set!")

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    welcome_text = (
        "👋 Hello! I am your Telegram Bot created using MCP Agent.\n\n"
        "How can I help you today?\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Get help info\n"
        "/about - About this bot"
    )
    bot.reply_to(message, welcome_text)

# Handle '/about'
@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = (
        "🤖 **Telegram Bot**\n\n"
        "Created with love using python-telegram-bot and Arena.ai MCP Agent.\n"
        "Powering automation with Model Context Protocol!"
    )
    bot.reply_to(message, about_text, parse_mode="Markdown")

# Echo all other text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response_text = f"You said: {message.text}"
    bot.reply_to(message, response_text)

if __name__ == '__main__':
    print("Bot is starting... Press Ctrl+C to stop.")
    bot.infinity_polling()
