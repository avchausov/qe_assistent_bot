import os
import requests
from flask import Flask, request

TOKEN = os.getenv("7551282370:AAFWAu3jT1hyeFPohbpM0irCaKrUoUf50dA")
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    text = data["message"]["text"]
    # Отправляем ответ пользователю
    requests.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": f"Вы сказали: {text}"})
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
