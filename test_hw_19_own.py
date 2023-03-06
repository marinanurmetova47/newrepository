import json
import pytest
import requests
import logging
from assertpy import assert_that

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

url = 'http://httpbin.org/get'        # отправили запрос на указанній url


def test_get():
    response = requests.get(url)
    # expected_keys = ['userId', 'id', 'title', 'body']
    # assert response.content ==
    print(response.text)
    # assert_that(response.text).contains_key('userId', 'id', 'title', 'body')
    # assert_that(response.text).contains_key(*expected_keys)
