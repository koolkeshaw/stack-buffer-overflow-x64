#This program is used to create a file containing all possible bytes
import binascii
FILENAME="allBytes"
msg=""
for i in range(0,16,1):
    for j in range (0,16,1):
        bin1=format(i,'01x')#convert 'i' into a hexadecimal {'x'} of length {'1'}, for padding use {'0'}
        bin2=format(j,'01x')
        msg=msg+binascii.unhexlify(bin1+bin2)

with open(FILENAME,"wb") as f:
    f.write(msg)