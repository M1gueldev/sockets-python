import functools
import re
from socket import *

ADDR = ('', 9876)
BUFFER = 1024

if __name__ == '__main__':
    srv = socket(AF_INET, SOCK_DGRAM)
    srv.bind(ADDR)
    print('Servidor corriendo en: 9876')
    while True:
        data = srv.recvfrom(BUFFER)
        print('DATA: ', data)
        if data[0] == b'Q':
            srv.sendto(b'CLOSE', data[1])
            srv.close()
        else:
            nums = re.findall('\d+', format(data[0]))
            if len(nums) < 2:
                srv.sendto(b'No hay suficientes numeros')
            else:
                suma = functools.reduce(lambda x, y: int(x) + int(y), nums)
                srv.sendto(b'Respuesta: ' + str.encode(str(suma)), data[1])
