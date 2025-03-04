import telebot
from flask import Flask, request
from config import TELEGRAM_API_KEY, WEBHOOK_URL, WEBHOOK_PORT
from handler.command_handler import send_welcome
from handler.message_handler import handle_message

# Khởi tạo bot Telegram và Flask server
bot = telebot.TeleBot(TELEGRAM_API_KEY)
app = Flask(__name__)

# Định nghĩa route để nhận dữ liệu từ Telegram
@app.route("/webhook", methods=["POST"])
def webhook():
    if request.headers.get("content-type") == "application/json":
        json_str = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return "OK", 200
    return "Forbidden", 403

# Xử lý lệnh /start và /help
@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
    send_welcome(bot, message)

# Xử lý tin nhắn thông thường
@bot.message_handler(func=lambda message: True)
def message_handler(message):
    handle_message(bot, message)

if __name__ == "__main__":
    # Thiết lập Webhook với Telegram
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

    print(f"Bot is running with webhook at {WEBHOOK_URL}")
    
    # Chạy Flask server trên cổng 8443 (HTTPS bắt buộc)
    app.run(host="0.0.0.0", port=WEBHOOK_PORT, ssl_context=('cert.pem', 'key.pem'))
