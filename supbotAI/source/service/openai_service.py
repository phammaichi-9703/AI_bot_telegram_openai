import openai
from config import OPENAI_API_KEY

# Khởi tạo OpenAI client
openai.api_key = OPENAI_API_KEY
client = openai.Client()

def chat_with_gpt(prompt):
    """Gửi prompt đến OpenAI GPT và nhận phản hồi."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
