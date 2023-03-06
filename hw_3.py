from selenium import webdriver

mobile_emulation = { "deviceName": "iPhone SE" }

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',


                          desired_capabilities = chrome_options.to_capabilities())

driver.get("https://youtube.com")


import time
time.sleep(10)
driver.quit()

