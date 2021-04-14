import socket
import sys
import time
try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('socked has been created')
except socket.error:
    print('socket is not created')
    sys.exit()
servername=''
port=8081
sock.bind((servername,port))
sock.listen(1)
list=[]
payload=['']
count=0
count1=0
host,addr=sock.accept()
# the host address is accepted.
while True:
    msg=host.recv(1407)
    if(len(msg)==0):
        break
    msg=str(msg.decode('utf-8'))
    seq_number=''
    for i in range(6):
        seq_number=seq_number+msg[i]
    payload[0]=payload[0]+msg[7:]
    print('The Sequence Number of Message is',seq_number)
    list.append(seq_number)
    if(count>=1):
        val=int(list[count])
        val_1=int(list[count-1])
        if(val-val_1!=1):
            print('Data not found')
    count=count+1
sock.close()
