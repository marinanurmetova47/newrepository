import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page_objects import PageObject as PO


@pytest.fixture(scope='function')
def driver():
    url = 'https://rozetka.com.ua/'
    driver = webdriver.Chrome()
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(30)
    driver.get(url)
    time.sleep(2)
    yield driver
    time.sleep(2)
    driver.quit()


def test_web_test(driver):
    element = driver.find_element(By.XPATH,PO.feild_locator)
    element.send_keys(PO.expected_text)
    element_2 = driver.find_element(By.XPATH, PO.search_locator)
    element_2.click()


def test_web_test_1(driver):
    element = driver.find_element(By.XPATH,PO.search_locator_3)
    element.click()
    element_2 = driver.find_element(By.XPATH, PO.search_locator_4)
    element_2.click()




