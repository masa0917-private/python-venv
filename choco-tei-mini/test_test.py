import socket
import circular

hostname, port = "192.168.178.178", 80
server_request = \
    "GET /hello.txt HTTP/1.1\r\n" \
    + "Host: localhost:80\r\n" \
    + "User-Agent: curl/7.68.0\r\n" \
    + "Accept: */*\r\n\r\n"
print(f"request:\n{server_request}")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5.0)
    s.connect_ex( (hostname, port) )
    #s.settimeout(None)
    ret = s.sendall(bytes(server_request, 'utf-8'))
except Exception as e:
    print(f"{e}")
    raise e

try:
    data = s.recv(8192*16)
    print( f"response({len(data)}):")
    print(data.decode('unicode-escape'))
except Exception as e:
    raise e