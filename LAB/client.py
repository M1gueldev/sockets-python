from socket import *


if __name__ == '__main__':
    dest = ('localhost', 2156)
    cliSock = socket(AF_INET, SOCK_STREAM)
    cliSock.connect(dest)
    data = input('> ')
    cliSock.send(data.encode("utf-8"))
    data = cliSock.recv(1024)
    print(data.decode("utf-8"))
    cliSock.close()
