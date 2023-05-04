from socket import *

FREE = 'Libre'
aux = [FREE] * 50


def aux_print():
    ans = ''
    for i,d in enumerate(aux):
        ans = ans + d
        if i % 5 == 4:
            ans = ans + '\n'
        else:
            ans = ans + ' , '
    print(ans)
    return ans.encode()


def my_parse(sdf):
    s = str(sdf, 'utf-8')
    # head = s.rstrip('0123456789')
    # tail = s[len(head):]
    aux = s.rsplit(' ', 1)
    return aux[0], aux[1]


def can_reserve(t):
    return len(aux) >= (aux.index(FREE)+int(t))


def reserve(h: str,t: str):
    for i in range(0, int(t)):
        aux[aux.index(FREE)] = h


if __name__ == '__main__':
    addr = ("localhost", 2156)
    srvSock = socket(AF_INET, SOCK_STREAM)
    srvSock.bind(addr)
    srvSock.listen()
    while True:
        cliSock, addr = srvSock.accept()
        print ('...conexion recibida')
        data = cliSock.recv(200)
        if (data) == b'Q':
            break
        h, t = my_parse(data)
        if (can_reserve(t)):
            reserve(h,t)
            cliSock.send(aux_print())
        else:
            cliSock.send(b'No hay suficientes asientos disponibles')
            cliSock.send(aux_print())
    cliSock.close()
    srvSock.close()
