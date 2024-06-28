import os
from dotenv import load_dotenv

import telebot

from utils import generate_keyboard

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    """Start function."""
    chat_id = message.chat.id
    bot.send_message(
        chat_id,
        'Выберите платформу: ',
        reply_markup=generate_keyboard()
    )


if __name__ == '__main__':
    bot.polling()
