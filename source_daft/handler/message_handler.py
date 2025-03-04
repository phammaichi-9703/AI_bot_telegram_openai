def handle_message(bot, message):
    response = f"Bạn đã gửi: {message.text}"
    bot.send_message(message.chat.id, response)
