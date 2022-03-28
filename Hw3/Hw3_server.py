from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('',3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ',addr)
    while True:
        data = client.recv(1024).decode()
        data = data.replace(' ','')
        index = 0
        if not data:
            break
        elif data.find('+') != -1:
            index = data.find('+')
            answer = int(data[:index]) + int(data[index+1:])
        elif data.find('-') != -1:
            index = data.find('-')
            answer = int(data[:index]) - int(data[index+1:])
        elif data.find('*') != -1:
            index = data.find('*')
            answer = int(data[:index]) * int(data[index+1:])
        elif data.find('/') != -1:
            index = data.find('/')
            answer = round(int(data[:index]) / int(data[index+1:]),1)
        else:
            break
        answer = str(answer)
        client.send(answer.encode())
    client.close()