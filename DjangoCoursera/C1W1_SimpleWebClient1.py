# this creates the socket code is very similar to SimpleWebBrowser
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000)) # 127.0.0.1 is same as localhost
cmd = 'GET http://127.0.0.1/sheffieldunited.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data)<1:
        break
    print(data.decode(), end='')

mysock.close()