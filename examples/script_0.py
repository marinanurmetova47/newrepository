import logging

import requests

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)

url_0 = 'https://rozetka.com.ua/'

response = requests.get(url_0).json()
print(type(response))

logging.info(f'{response}')