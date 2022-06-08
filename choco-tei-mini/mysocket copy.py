import io
import sys
import requests
import base64
import cv2
import numpy as np
from bs4 import BeautifulSoup

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

r = requests.get('http://192.168.178.178/')
# print(r.headers)
# print(r.text)
# print(r.content)
# b_text = r.content.decode()
# b_text = r.content.split()
# print(base64.b64decode(r.text))
# print(type(b_text))

soup = BeautifulSoup(r.content, 'html.parser')

img_tag = soup.find('img')

# ほしいタグにはたどり着いているが、SRCの中身が入らない
# 動的に変化しているため取得できていないと推測する。
# Todo:動的に変化するsrcの中身抽出方法を探す。
print(img_tag)

with open('test.jpg', 'wb') as f:
    f.write(base64.b64decode(img_tag.get('src').split('base64,')[0]))