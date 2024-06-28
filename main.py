import os
from dotenv import load_dotenv

import telebot
from telebot import types

from utils import RESOURCES

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


def generate_keyboard():
    markup = types.InlineKeyboardMarkup()
    for title in RESOURCES:
        button = types.InlineKeyboardButton(
            text=title,
            callback_data=f'parse_{title}'
        )
        markup.add(button)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(
        chat_id,
        'Выберите платформу: ',
        reply_markup=generate_keyboard()
    )


if __name__ == '__main__':
    bot.polling()
