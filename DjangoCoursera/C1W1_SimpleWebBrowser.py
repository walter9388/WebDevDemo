import socket

# this creates the socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this specifies we are the client (as opposed to the server)
mysock.connect(('data.pr4e.org', 80)) # remember 80 is http port (443 is https port)
# cmd: '\r\n' is return then newline, this is needed twice so the server knows the request is done
# note that in python we need to add encode() at the end to convert unicode to UTF-8
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)  # wait until its recieved up to 512 characters
    if len(data)<1:
        break # once no data is recieved, the server has finished, hence we end the loop
    print(data.decode(), end='') # print the recieved data as it comes, needs to be decoded: UTF-8 to unicode

mysock.close()