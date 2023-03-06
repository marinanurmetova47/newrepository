# open wikipedia           https://en.wikipedia.org/wiki/Main_Page
# find page for First world war
# Find Verden apearanc on page
# additional Find on page 11.11.18
# additionally find time

import logging
import time
import selenium
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from data import Config, Wikipedia


# create logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler("test.log")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file_handler
ch.setFormatter(formatter)

# add file_handler to logger
logger.addHandler(ch)


expected = Wikipedia(Config.url)

# response = requests.get(expected_url)
# print(response.text)


driver = webdriver.Chrome()
driver.get(expected.url)


search_field = driver.find_element(By.ID, expected.search_field_id)
search_field.send_keys(expected.url_2) # в поле поиска передаем запрос
# search_field.send_keys(Keys.RETURN)  # отображается страница переданная в запросе

# либо можно через XPATH кнопки ввода

driver.find_element(By.XPATH, expected.search_button_id).click()

first_heading_id = 'firstHeading'
search_result = driver.find_element(By.ID, first_heading_id)
logger.debug(f'found result is {search_result.text}')
assert search_result.text == 'World War I'

time.sleep(10)