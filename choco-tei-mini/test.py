import base64

b_data=base64.b64encode('data:image/jpeg;base64,/9j/'.encode('utf-8'))
print(b_data, type(b_data))