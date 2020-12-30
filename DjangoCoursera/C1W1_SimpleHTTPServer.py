from socket import *

# the function will be in a infinite loop awaiting requests
def createServer():
    # this creates the socket
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # this specifies the socket is a server on localhost port 9000
        serversocket.bind(('localhost', 9000))
        # this tells the OS to hold temporarily up to 5 pending connection requests
        serversocket.listen(5)
        while True:
            # accept sits there waiting for a request, and only finishes when it recieves a request
            (clientsocket, address) = serversocket.accept()

            # first thing we do is recieve as client always sends first (HTTP protocol)
            rd = clientsocket.recv(5000).decode() # decode makes it UTF-8 to Unicode
            # most servers would read request and figure out what to send back... we are just gonna print it in this example
            pieces = rd.split('\n')
            if len(pieces) > 0:
                print(pieces[0])

            data = 'HTTP/1.1 200 OK\r\n'
            data += 'Content-Type: text/html; charset=utf-8\r\n'
            data += '\r\n' # blank line after sending header
            data += '<html><body>Hello World</body></html>\r\n\r\n' # blank line after finishing sending content
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR) # once the data is sent we end the connection (and the client side will then do the same)
            # after this, the loop restarts, always awaiting requests
    
    except KeyboardInterrupt: # needed to stop server from terminal
        print('\nShutting down....\n')
    except Exception as exc: # needed for error handling
        print('Error:\n')
        print('exc')

    serversocket.close()

if __name__=='__main__':
    print('Access http://localhost:9000')
    createServer()
