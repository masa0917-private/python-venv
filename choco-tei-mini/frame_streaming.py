# coding: UTF-8

# from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    while True:
        driver.get("http://192.168.178.178/xaccja/getCamImage")
        time.sleep(0.01)
except KeyboardInterrupt:
    print('--- Finish ---')

# html = driver.page_source.encode('utf-8')

# soup = BeautifulSoup(html, "html.parser")
# print (soup.select_one("#lv_img"))

