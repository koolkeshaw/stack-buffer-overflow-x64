import binascii
"""This function will implement ROT13 encryption on input byte"""
def useROT13(byte):
	char= binascii.b2a_base64(byte)
	updatedByte=byte
	if char.isalnum():
		updatedByte=applyROT13(byte)
	return updatedByte

SHELLCODE="reverseShell"
UPDATED_SHELLCODE="reverseShellV2"
updatedBytes=""
with open(SHELLCODE,"rb") as f:
	while True:
		byte=f.read(1)
		updatedBytes=updatedBytes+useROT13(byte)
		if byte == "":
			break
			
with open(UPDATED_SHELLCODE,"wb") as f:
	f.write(updatedBytes)
		
