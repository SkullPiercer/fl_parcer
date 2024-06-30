import os
from dotenv import load_dotenv

import telebot

from utils import (
    generate_keyboard,
    get_data_from_fl,
    get_data_from_habr,
    get_data_from_hh
)


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


@bot.callback_query_handler(func=lambda call: call.data.startswith('parse_'))
def send_posts(call):
    """Sends vacancies with links."""
    chat_id = call.message.chat.id
    try:
        sites = {
            'fl.ru': get_data_from_fl(),
            'habr-freelance': get_data_from_habr(),
            'hh.ru': get_data_from_hh()
        }
        posts = sites[call.data.split('_')[1]]
        bot.send_message(
            chat_id,
            posts,
            parse_mode='Markdown'
        )
    except:
        message = 'Произошла непредвиденная ошибка, попробуйте позже ):'
        bot.send_message(
            chat_id,
            message
        )


if __name__ == '__main__':
    bot.polling()
