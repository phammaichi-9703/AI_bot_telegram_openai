import telebot

def send_welcome(bot: telebot.TeleBot, message):
    """Phản hồi khi người dùng gửi lệnh /start hoặc /help."""
    bot.reply_to(message, "Hello! I'm your AI assistant. Ask me anything!")
