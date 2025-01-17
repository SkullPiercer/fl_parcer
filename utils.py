import os
import requests
from dotenv import load_dotenv

from telebot import types
from bs4 import BeautifulSoup

# Service variables
load_dotenv()
RESOURCES = {
    'fl.ru': os.getenv('FLRU'),
    'habr-freelance': os.getenv('HABR'),
    'hh.ru': os.getenv('HH')
}
HEADERS = {'User-Agent': os.getenv('USER_AGENT')}


def get_soup_response(site_url):
    """The function takes a page url and returns a soup object."""
    response = requests.get(RESOURCES[site_url], headers=HEADERS)
    return BeautifulSoup(response.text, 'html.parser')


# Parse functions
def get_data_from_hh():
    """Parsing first page of HH with Python filter."""
    soup = get_soup_response('hh.ru')
    element_class = 'vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter'
    title_class = 'vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link'
    link_class = 'bloko-link'
    posts = soup.find_all('div', class_=element_class)
    posts_title = [
        title.find('span', class_=title_class).get_text() for title in posts
    ]
    posts_link = [
        link.find('a', class_=link_class).get('href') for link in posts
    ]
    result_message = ''
    for title, link in zip(posts_title, posts_link):
        result_message += f'[{title}]({link})\n'
    return result_message


def get_data_from_habr():
    soup = get_soup_response('habr-freelance')
    posts = soup.find_all('div', class_='task__title')
    preurl = 'https://freelance.habr.com'
    result_message = ''
    for post in posts:
        href = post.findNext("a").get("href")
        result_message += f'[{post.text}]({preurl + href})\n'
    return result_message


def get_data_from_fl():
    soup = get_soup_response('fl.ru')
    posts = soup.find_all('h2', class_='title')
    preurl = 'https://freelance.ru/'
    result_message = ''
    for post in posts:
        href = post.findNext("a").get("href")
        post = ' '.join(post.text.split())
        result_message += f'[{post}]({preurl + href})\n'
    return result_message


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

