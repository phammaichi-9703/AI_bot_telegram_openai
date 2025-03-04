import telebot
from service.openai_service import chat_with_gpt

def handle_message(bot: telebot.TeleBot, message):
    """Xử lý tin nhắn từ người dùng."""
    bot.reply_to(message, "Thinking...")
    response = chat_with_gpt(message.text)
    bot.send_message(message.chat.id, response)
