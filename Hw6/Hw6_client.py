from socket import *

port = 3333
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send [mboxID] message" or "receive [mboxID]"):')

    sock.sendto(msg.encode(), ('localhost', port))

    data, addr = sock.recvfrom(BUFFSIZE)
    if data.decode() == 'quit':
        break
    else:
        print(data.decode())