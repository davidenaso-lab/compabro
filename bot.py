import os
import threading
import time
from flask import Flask
import telebot

STAFF_CHAT_ID = -5598663431
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return 'ok'

def run_bot():
    while True:
        try:
            bot = telebot.TeleBot(os.environ["BOT_TOKEN"])
            @bot.message_handler(func=lambda m: True)
            def forward(message):
                if message.text and not message.text.startswith('/'):
                    bot.send_message(STAFF_CHAT_ID, message.text)
            bot.infinity_polling()
        except Exception:
            time.sleep(5)

threading.Thread(target=run_bot, daemon=True).start()
flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
