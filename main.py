import os
import time
from dotenv import load_dotenv

import telebot


load_dotenv()

TOKEN = os.getenv('TOKEN')
RETRY_PERIOD = 30
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    while True:
        try:
            bot.send_message(chat_id, 'Привет')
        except:
            bot.send_message(chat_id, 'Произошла ошибка, попробуйте позже')
        finally:
            time.sleep(RETRY_PERIOD)


bot.polling()
