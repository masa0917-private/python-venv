import io
import sys
import requests
import base64
import cv2
import numpy as np

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

r = requests.get('http://192.168.178.178/xaccja/getCamImage')
# print(r.headers)
# print(r.text)


print(r.content)

# b_text = r.content.decode()
# b_text = r.content.split()

# print(base64.b64decode(r.text))

# print(type(b_text))



# byte_data=r"r.content"

# with open(r.content, 'rb') as f:
#     img_base64 = f.read()

# img_binary = base64.b64decode(r.content)        # img_base64)
# jpg = np.frombuffer(img_binary, dtype=np.uint8)

# img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)

# cv2.imwrite(r"decode.jpg", img)

# cv2.imshow('window title', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()