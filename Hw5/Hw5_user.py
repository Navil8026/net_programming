#클라이언트
from calendar import c
from socket import *
import time

socket1 = 8000
socket2 = 8080
while True:
    dev1 = socket(AF_INET, SOCK_STREAM)
    dev2 = socket(AF_INET, SOCK_STREAM)
    f = open('data.txt','a+')

    device = input("device 입력 : ")
    if device == '1':
        dev1.connect(('localhost',socket1))
        dev1.send('Request'.encode())
        message = dev1.recv(1024).decode()
        f.write(f"-{time.strftime('%c',time.localtime(time.time()))}: Device1: {message}\n")
        dev1.close()

    elif device == '2':
        dev2.connect(('localhost',socket2))
        dev2.send('Request'.encode())
        message = dev2.recv(1024).decode()
        f.write(f"-{time.strftime('%c',time.localtime(time.time()))}: Device2: {message}\n")
        dev2.close()

    elif device == 'quit':
        dev1.connect(('localhost',socket1))
        dev1.send('quit'.encode())
        dev1.close()

        dev2.connect(('localhost',socket2))
        dev2.send('quit'.encode())
        dev2.close()
        f.close()
        break
    else:
        print("error!")
    f.close()