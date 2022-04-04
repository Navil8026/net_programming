from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
msg_dict = {}

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    data = data.decode()
    print(data)
    if data.find(' ') > -1:
        type_data, message = data.split(' ',1)
        
        if type_data == 'send':
            mboxID, message = message.split(' ',1)
            # msg_dict[mboxID] = message #message를 dict에 넣기
            if mboxID not in msg_dict:
                msg_dict[mboxID] = []
            msg_dict[mboxID].append(message)
            sock.sendto('OK'.encode(), addr) #ok문자 전송

        elif type_data == 'receive':
            mboxID = message
            if mboxID not in msg_dict or not msg_dict[mboxID]:
                sock.sendto('No messages'.encode(), addr)
            else:
                sock.sendto(msg_dict[mboxID].pop(0).encode(), addr)
        else:
            print("error!")
    elif data == 'quit':
        sock.sendto('quit'.encode(),addr)
        break
    else:
        print("error!")
