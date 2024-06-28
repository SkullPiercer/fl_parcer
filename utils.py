import os
import requests
from dotenv import load_dotenv

from bs4 import BeautifulSoup

load_dotenv()
RESOURCES = {
    'fl.ru': '',
    'habr-freelance': '',
    'hh.ru': ''
}
HEADERS = {'User-Agent': os.getenv('USER_AGENT')}
RESPONSE_URL = os.getenv('URL')


def get_data_from_site(site_title):
    response = requests.get(RESPONSE_URL, headers=HEADERS)
    return response.status_code


print(get_data_from_site('fl.ru'))
print(HEADERS)
