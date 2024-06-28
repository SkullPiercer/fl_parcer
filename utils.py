import os
import requests
from dotenv import load_dotenv

from telebot import types
from bs4 import BeautifulSoup

#
load_dotenv()
RESOURCES = {
    'fl.ru': '',
    'habr-freelance': '',
    'hh.ru': ''
}
HEADERS = {'User-Agent': os.getenv('USER_AGENT')}
RESPONSE_URL = os.getenv('URL')


#
def get_data_from_site(site_title):
    response = requests.get(RESPONSE_URL, headers=HEADERS)
    return response.status_code


print(get_data_from_site('fl.ru'))
print(HEADERS)


# Keyboards
def generate_keyboard():
    """Site selection keyboard."""
    markup = types.InlineKeyboardMarkup()
    for title in RESOURCES:
        button = types.InlineKeyboardButton(
            text=title,
            callback_data=f'parse_{title}'
        )
        markup.add(button)
    return markup
