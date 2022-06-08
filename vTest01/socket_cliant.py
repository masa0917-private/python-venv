'''
ウェルノウンポート番号  (0-1023)
登録済ポート番号        (1024-49151)
動的・プライベート　ポート番号  (46152-65535)
'''
import socket

# # TCP
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(('127.0.0.1', 50007))
#     s.sendall(b'Hello')
#     data = s.recv(1024)
#     print(repr(data))

# UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello UDP', ('127.0.0.1', 50007))