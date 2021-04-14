import socket
import time
import sys
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('Socket has been Created')
name ='80.78.215.2'
port = 8881
try:
    sock.connect((name,port))
    print('Connection is Establised')
except socket.error:
    print('Connection is Refused')
    sys.exit()
with open ('sample.txt','r') as reader:
    inline =reader.read()
    reader.close()
    list=['A']
    len=0
    while(len<1400):
        list[0]=list[0]+inline
        len=len+1
    len=0
    seq_number='100000'
    while(len<65000):
        message=seq_number+';'+list[0]
        message=bytes(message,'utf-8')
        try:
            sock.sendto(message,(name,port))
            print('Data send to the receiver')
            time.sleep(5)
        except socket.error:
            print('No receiver found')
            sys.exit()
        seq_number=int(seq_number)
        seq_number=seq_number+1
        seq_number=str(seq_number)
        len=len+1400
    msg='All packets sent to the receiver'
    print(msg)
sock.close()
