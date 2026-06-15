import os
import threading
from flask import Flask
import telebot

STAFF_CHAT_ID = -5598663431
bot = telebot.TeleBot(os.environ["BOT_TOKEN"])
flask_app = Flask(__name__)

@bot.message_handler(func=lambda m: True)
def forward(message):
    if message.text and not message.text.startswith('/'):
        bot.send_message(STAFF_CHAT_ID, message.text)

@flask_app.route('/')
def home():
    return 'ok'

threading.Thread(target=bot.infinity_polling, daemon=True).start()
flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
