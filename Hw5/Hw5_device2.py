#서버2
from random import randint
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',8080))
s.listen(10)

while True:
    client, addr = s.accept()
    msg = client.recv(1024).decode()
    if msg == 'Request':
        heartbeat = randint(40,140)    #심박수
        steps = randint(2000,6000)   #걸음수
        cal = randint(1000,4000)    #소모칼로리
        message = f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
        client.send(message.encode())
        client.close()
    elif msg == 'quit':
        client.close()
        break
    else:
        print("error!")