#서버
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ',addr)
    client.send(b'Hello ' + addr[0].encode())
    print(client.recv(1024).decode())
    client.send((20171541).to_bytes(8,'big'))
    client.close()