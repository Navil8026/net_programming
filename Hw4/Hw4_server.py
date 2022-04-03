from socket import *

s = socket()
s.bind(('',80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    filename = req[0].split()[1]    #'GET' '/index.html' 'HTTP/1.1'에서 가운데만 추출
    filename = filename.strip("/")  #자원 이름 파싱 후 / 제거

    def send_message(mimeType): #성공했을 때 HTTP Response 메세지
        access_message = f'HTTP/1.1 200 OK\r\nContent-Type: {mimeType}\r\n\r\n'
        return access_message.encode()

    if filename == 'index.html':
        f=open('index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'
        c.send(send_message(mimeType))
        c.send(f.read().encode('euc-kr'))
    elif filename == 'iot.png':
        f = open('iot.png', 'rb')
        mimeType = 'image/png'
        c.send(send_message(mimeType))
        c.send(f.read())
    elif filename == 'favicon.ico':
        f = open('favicon.ico', 'rb')
        mimeType = 'image/x_icon'
        c.send(send_message(mimeType))
        c.send(f.read())
    else:   #에러 시
        c.send('HTTP/1.1 404 Not Found\r\n'.encode())
        c.send('\r\n'.encode())
        c.send('<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'.encode())
        c.send('<BODY>Not Found</BODY></HTML>'.encode())

    print(msg)
    c.close()   #소켓 닫기