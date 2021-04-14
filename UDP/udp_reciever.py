import socket
import time
import sys

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
    print('socket has not been created')
    sys.exit()
serverip = '192.168.0.5'
port=8080
try:
    sock.connect((serverip,port))
except socket.error:
    print('Connection  is Refused')
with open ('sample.txt' , 'r') as reader:
    inline = reader.read()
    reader.close()
    list=['A']
    length=0
    while(length<1399):
        list[0]=list[0]+inline
        length=length+1
    length=0
    seq_number='100000'
    count=0
    while(length<65000):
        length = length + len(list[0])
        message=seq_number+';'+list[0]
        message=bytes(message,'utf-8')
        try:
            sock.send(message)
            time.sleep(1)
            print('Data sent to the reciever')
        except socket.error:
            print('No reciever found')
            sys.exit()
        seq_number=int(seq_number)
        seq_number=seq_number+1
        seq_number=str(seq_number)
    msg='All packets are sent to the receiver'
    print(msg)
sock.close()
