
import sys
from sys import argv
import binascii 
import socket
import string
import random
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from datetime import datetime
from time import sleep

backend = default_backend()
BUFF_SIZE = 4096
cipherType = ""
sessionKey = ""
IV = ""
derivedKey = ""
# Reference: https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python/23728630#23728630
nonce = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))


# Hash the key to appropriate size based on the cipher type
def deriveKey():
    global derivedKey
    if(cipherType == "null"):
        return

    # aes128 uses 16 byte keys, hashing with md5
    elif(cipherType == "aes128"):
        keyHash = hashlib.md5()
        keyHash.update(sessionKey.encode())
        derivedKey = keyHash.digest()

    # aes256 uses 32 byte key, hashing with sha256
    elif(cipherType == "aes256"):
        derivedKey = sessionKey[0:32].encode()
    else:
        sys.stderr.write("Error: bad command line arguments \n")
        sys.exit(0)


# Pads and encrypts data using speficied data, then returns it
# Reference tutorial
def encryptData(data):
    padder = padding.PKCS7(128).padder()
    paddedData = padder.update(data) + padder.finalize()
    if(cipherType == "null"):
        return data
    elif(cipherType == "aes128" or cipherType=="aes256"):
        cipher = Cipher(algorithms.AES(derivedKey), modes.CBC(IV[0:16].encode()), backend=backend)
        encryptor = cipher.encryptor()
        return encryptor.update(paddedData) + encryptor.finalize()

# Decrypts and unpads the given data and returns it
def decryptData(data):
    if(cipherType == "null"):
        return data
    elif(cipherType == "aes128" or cipherType=="aes256"):
        cipher = Cipher(algorithms.AES(derivedKey), modes.CBC(IV[0:16].encode()), backend=backend)
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(data) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()


# for sending data
def sendFile(serverSocket):
    dataTotal = ""

    # Read from standard until EOF
    while 1:
        data = binascii.hexlify(sys.stdin.buffer.read(BUFF_SIZE)).decode()
        dataTotal += data
        if data == '':
            break
    # encrypt and send length of data to server
    size = (len(dataTotal))
    serverSocket.sendall(encryptData(str(size).encode()))

    # There is a problem which python just skips command, this is a work around
    confirmation = decryptData(serverSocket.recv(BUFF_SIZE)).decode()
    if(confirmation == "Ready"): 
        # encrypt and send data to server
        for i in range(0, size, BUFF_SIZE-1):
            serverSocket.sendall(encryptData(dataTotal[i: min(i+(BUFF_SIZE-1), size)].encode()))

# for recieving data
def recvFile(serverSocket):
    # To check when to stop receiving messages
    size = int(decryptData(serverSocket.recv(BUFF_SIZE)).decode())
    # Work around for socket sending wrong data when cipher is null and file is huge
    serverSocket.sendall(encryptData("Ready".encode()))
    dataTotal = ""
    while 1:
        data = decryptData(serverSocket.recv(BUFF_SIZE)).decode()
        dataTotal += data
        if len(dataTotal) >= size:
            break
    
    dataTotal = binascii.unhexlify(dataTotal)
    # decrypt and write to file
    sys.stdout.buffer.write(dataTotal)

def main():
    global IV, sessionKey, cipherType

    # Check args
    if(len(argv) != 6):
        sys.stderr.write("Error: bad command line arguments \n")
        sys.exit(0)
    command = argv[1]

    if(command != "read" and command != "write"):
        sys.stderr.write("Error: bad command line arguments \n")
        sys.exit(0)
    
    filename = argv[2]
    if(len(argv[3].split(":")) != 2):
        sys.stderr.write("Error: bad command line arguments \n")
        sys.exit(0)
    hostname,port = argv[3].split(":")
    if(port.isdigit() == False):
        sys.stderr.write("Error: bad command line arguments \n")
        sys.exit(0)
    cipherType = argv[4]
    key = argv[5]


    # Compute IV and the sessionkey
    IV = hashlib.sha256((key + nonce + "IV").encode()).hexdigest()
    sessionKey = hashlib.sha256((key + nonce + "SK").encode()).hexdigest()

    # computer the key used for encryption and decryption
    deriveKey()


    # connect to client
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    serverSocket.connect((hostname, int(port)))

    # Send the first message unencrypted
    serverSocket.sendall((cipherType+ ':' + nonce).encode())

    # if key is wrong there will be an exception thrown
    try:
        # Reciece a random challenge
        challenge = decryptData(serverSocket.recv(BUFF_SIZE)).decode()
        response = hashlib.sha256((key + challenge).encode()).hexdigest()

        serverSocket.sendall(encryptData(response.encode()))

        data = decryptData(serverSocket.recv(BUFF_SIZE)).decode()

    except:
        sys.stderr.write("Error: wrong key\n")
        sys.exit(0)
    if(data == "Badkey"):
        sys.stderr.write("Error: wrong key\n")
        sys.exit(0)

    # send filename:operation to server
    serverSocket.sendall(encryptData((filename + ':' + command).encode()))
    data = decryptData(serverSocket.recv(BUFF_SIZE)).decode()
    if(command == "read"):
        if(data == "Error"):
            sys.stderr.write("Error: file could not be read by server\n")
            sys.exit(0)
        recvFile(serverSocket)

    else:
        if(data == "Error"):
            sys.stderr.write("Error: file could not be written by server\n")
            sys.exit(0)
        sendFile(serverSocket)

    finalMessage = decryptData(serverSocket.recv(BUFF_SIZE)).decode()
    if(finalMessage == "Success"):
        sys.stderr.write("OK\n")
        #Client disconnects
        sys.exit(0)
 
if __name__ == "__main__":
    main()
