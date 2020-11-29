import os

from call_selenium import webdriver

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'))
driver.get('https://www.detik.com/')

