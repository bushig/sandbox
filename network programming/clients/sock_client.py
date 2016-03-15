import socket

addres=('localhost', 8000)

s=socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = bin(1)
    if not data:
        break
    s.sendto(bytes(data, 'utf8'), addres)
    data=s.recv(1024)
    if not data:
        print('server didnt respond')
        break
    print('recived: {}'.format(data.decode('utf-8')))

s.close()
