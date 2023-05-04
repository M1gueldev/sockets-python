from socket import *

addr = ("localhost", 8008)

if __name__ == '__main__':
    srvSock = socket(AF_INET, SOCK_STREAM)
    srvSock.bind(addr)
    srvSock.listen()
    while True:
        cliSock, addr = srvSock.accept()
        print('...conexion recibida')
        data = cliSock.recv(1000)
        cliSock.send(b'HTTP/1.0 200 OK\n')
        cliSock.send(b'Content-Type: text/html\n')
        cliSock.send(b'\n')  # header and body should be separated by additional newline
        cliSock.send(b"""
                <html>
                <body>
                <h1>Miguel Murillo Bernal</h1>
                <h2>9117995</h2>
                </body>
                </html>
            """)
        cliSock.close()
    srvSock.close()

