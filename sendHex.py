import socket

TARGET="127.0.0.1"
PORT=2888

scket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
scket.connect((TARGET,PORT))
scket.recv(1024)
msg=""
with open("allAllowedHalfBytes.txt","rb") as f:
	for line in f.readline():
		msg=msg+line

msg=msg+"\n"
with open("inputSent","w") as f:
	f.write(msg)
scket.send(msg)
print "Sent msg of size: "+str(len(msg))
#info=[msg[i:i+3]for i in range(0,len(msg),3)]
#print info

response= scket.recv(1024)
with open("output","w") as f:
	f.write(response)

