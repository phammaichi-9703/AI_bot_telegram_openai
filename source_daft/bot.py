import os
import telebot
import openai
from config import TELEGRAM_API_KEY, OPENAI_API_KEY
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize bot and OpenAI
bot = telebot.TeleBot(TELEGRAM_API_KEY)
openai.api_key = OPENAI_API_KEY

client = openai.Client()

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your AI assistant. Ask me anything!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Thinking...")
    response = chat_with_gpt(message.text)
    bot.send_message(message.chat.id, response)

print("Bot is running...")
bot.polling()
