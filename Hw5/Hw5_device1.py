#서버1
from random import randint
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',8000))
s.listen(10)

while True:
    client, addr = s.accept()
    msg = client.recv(1024).decode()
    if msg == 'Request':
        temp = randint(0,40)    #온도
        humid = randint(0,100)    #습도
        lilum = randint(70,150)   #조도
        message = f"Temp={temp}, Humid={humid}, lilum={lilum}"
        client.send(message.encode())
        client.close()
    elif msg == 'quit':
        client.close()
        break
    else:
        print("error!")