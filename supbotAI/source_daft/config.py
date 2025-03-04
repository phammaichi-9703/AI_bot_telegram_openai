import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # URL Webhook (HTTPS bắt buộc)
WEBHOOK_PORT = int(os.getenv("WEBHOOK_PORT", 8443))  # Cổng webhook
