# coding: UTF-8

# from bs4 import BeautifulSoup
from requests import options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from bs4 import BeautifulSoup

REFRESH_RATE = 10


service = ChromeService(executable_path=ChromeDriverManager().install())

# # ブラウザを非表示にするときに使用
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# driver = webdriver.Chrome(service=service, options=options)

driver = webdriver.Chrome(service=service)


driver.get("http://192.168.178.178/xaccja/getCamImage")

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'lxml')
results = soup.find("img")
src = results.get("src")

print('===== src =====')
print(src)
print('===============')

time.sleep(REFRESH_RATE)

driver.quit()


