import sys
import os
import binascii
from sys import argv
import socket
import string
import random
import hashlib
import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

from time import sleep

backend = default_backend()
BUFF_SIZE = 4096
cipherType = ""
sessionKey = ""
IV = ""
derivedKey = ""
# Reference: https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python/23728630#23728630
nonce = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))


# Use the session key if aes256, if aes128 take a md5 hash of it
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
        derivedKey = (sessionKey[0:32]).encode()



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


# for sending files
def sendFile(filename, clientSocket):
    # try to open file
    try:
        file = open(filename, 'rb')

    # Throw an exception if file can't be read from, send error to client, print status error, close connection
    except:
        clientSocket.sendall(encryptData("Error".encode()))
        print((datetime.datetime.now()).strftime("%H:%M:%S") + ": status: error - Can't read from the speficied file" )
        clientSocket.close()
        return -1

    # Send can proceed messeage
    clientSocket.sendall(encryptData("Proceed".encode()))
    dataTotal = ""
    # read from file until EOF
    while 1:

        data = binascii.hexlify(file.read(BUFF_SIZE)).decode()
        dataTotal += data
        if data == '':
            break
            
    # encrypt and send length of data to client
    size = (len(dataTotal))
    clientSocket.sendall(encryptData(str(size).encode()))

    # There is a problem which python just skips command, this is a work around
    confirmation = decryptData(clientSocket.recv(BUFF_SIZE)).decode()
    if(confirmation == "Ready"): 
        # encrypt and send data to client
        for i in range(0, size, BUFF_SIZE-1):
            clientSocket.sendall(encryptData(dataTotal[i: min(i+BUFF_SIZE-1, size)].encode()))
    file.close()


# for recieving files
def recvFile(filename, clientSocket):
    # try to open file
    try:
        file = open(filename, 'wb')

    # Throw an exception if file cant be written, send error to client, print status error, close connection
    except:
        clientSocket.sendall(encryptData("Error".encode()))
        print((datetime.datetime.now()).strftime("%H:%M:%S") + ": status: error - cannot write to file" )
        clientSocket.close()
        return -1

    # Send can proceed messeage
    clientSocket.sendall(encryptData("Proceed".encode()))
    size = int(decryptData(clientSocket.recv(BUFF_SIZE)).decode())
    # Work around for socket sending wrong data when cipher is null and file is huge
    clientSocket.sendall(encryptData("Ready".encode()))
    dataTotal = ""
    # Read from client until they are done sending
    while 1:
        data = decryptData(clientSocket.recv(BUFF_SIZE))
        dataTotal += data.decode()
        if len(dataTotal) >= size:
            break
        # decrypt and write to file
    dataTotal = binascii.unhexlify(dataTotal)
    file.write(dataTotal)
    file.close()


def main():
    global IV, sessionKey, cipherType

    # Check args
    if(len(argv) != 3):
        print("Error!! Usage <python3 Server.py port key>")
        sys.exit(0)
    port = argv[1]
    key = argv[2]

    if(port.isdigit() == False):
        print("Port must be an integer")
        sys.exit(0)

    print("Listening on port " + port)
    print("Using secret key: " + key)

    #Initialize socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    serverSocket.bind(('', int(port)))
    serverSocket.listen(1)

    # Keep server alive
    while 1:
        # Accept client connection and recieve data
        (clientSocket, addr) = serverSocket.accept()
        firstData = clientSocket.recv(BUFF_SIZE)
        cipherType, nonce = (firstData.decode()).split(":")

        # Compute IV and the sessionkey
        IV = hashlib.sha256((key + nonce + "IV").encode()).hexdigest()
        sessionKey = hashlib.sha256((key + nonce + "SK").encode()).hexdigest()

        # computer the key used for encryption and decryption
        deriveKey()

        # Printing info with time stamp
        print((datetime.datetime.now()).strftime("%H:%M:%S") + ": new connection from " + str(addr[0]) + " cipher= "+ cipherType)
        print((datetime.datetime.now()).strftime("%H:%M:%S") + ": nonce=" + nonce)
        print((datetime.datetime.now()).strftime("%H:%M:%S") + ": IV=" + IV)
        print((datetime.datetime.now()).strftime("%H:%M:%S") + ": SK=" + sessionKey)

        try:
            # Sending a random 8 byte to client
            challenge = binascii.hexlify(os.urandom(8))
            clientSocket.sendall(encryptData(challenge))
            challengeResponse = decryptData(clientSocket.recv(BUFF_SIZE)).decode()

            # Matching what the client sends, hashes it with a concatenatuon with the key
            # to authenticate
            if(hashlib.sha256((key + challenge.decode()).encode()).hexdigest() != challengeResponse):
                clientSocket.sendall(encryptData("Badkey".encode()))
                print((datetime.datetime.now()).strftime("%H:%M:%S") + ": status: error - bad key" )
                clientSocket.close()
                continue
        except:
            print((datetime.datetime.now()).strftime("%H:%M:%S") + ": status: error - bad key" )    
            clientSocket.close()
            continue        
        # send success message
        clientSocket.sendall(encryptData("Good".encode()))

        # get filename and operation
        filename, operation = (decryptData((clientSocket.recv(BUFF_SIZE))).decode()).split(":")
        print((datetime.datetime.now()).strftime("%H:%M:%S") + ": command:" + operation + ", filename:" + filename)


        if(operation == "read"):
            val = sendFile(filename, clientSocket)
        else:
            val = recvFile(filename, clientSocket)
        if(val != -1):
            # send success message
            clientSocket.sendall(encryptData("Success".encode()))
            print((datetime.datetime.now()).strftime("%H:%M:%S") + ": status: success" )

if __name__ == "__main__":
    main()
