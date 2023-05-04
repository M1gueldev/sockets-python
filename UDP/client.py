from socket import *

ADDR = ('localhost', 9876)
BUFFER = 1024
cliSock = socket(AF_INET, SOCK_DGRAM)

if __name__ == '__main__':
    while True:
        data = input('> ')
        cliSock.sendto(data.encode("utf-8"), ADDR)
        data, ADDR = cliSock.recvfrom(BUFFER)
        ans = data.decode("utf-8")
        if ans == 'CLOSE':
            print('Coneccion cerrada')
            cliSock.close()
            break
        else:
            print(ans)
