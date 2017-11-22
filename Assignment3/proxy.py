import socket
import select
import binascii
import sys
import datetime
import threading

logOptions = ["","-raw","-strip","-hex"]
replaceOpt = False
toReplace = ""
replaceWith = ""


# Perfroms the autoN operations
def autoN(msg):
	msgLength = len(msg)
	offset = 0
	newMsg= ""

	# Compare the offset with the msgLength
	while offset < msgLength:
		# Divide the data into N chunks, if offset + N > msglength, pick msgLength
		msgChunk = msg[offset:min(offset+N,msgLength-1)]
		for char in msgChunk:
			asciiValue = ord(char)
			# backslash
			if asciiValue == 92:
				newMsg +="\\"
			# tab
			elif asciiValue == 9:
				newMsg +="\\t"
			# newline
			elif asciiValue == 10:
				newMsg +="\\n"
			# carriage return
			elif asciiValue == 13:
				newMsg +="\\r"
			# 32 to 127
			elif ((asciiValue > 31) and (asciiValue < 128)):
				newMsg += char
			# print hex value
			else:
				newMsg += "\\"
				hexValue = hex(ord(char))
				newMsg += hexValue[2:]
			
		newMsg += ("\n")
		offset += N
	return newMsg



# convert text to hex
# Reference: https://stackoverflow.com/questions/15884677/python-printing-hex-removes-first-0
def toHex(msg):
	msgLength = len(msg)
	offset = 0
	offsetIndex = 0
	hexTxt = ""
	while offset < msgLength:
		# the first part of the string
		offsetIndex = min(offset, msgLength)
		hexTxt += hex(offsetIndex)[2:].zfill(8) + "  "

		# if offset + 8 is less than split in 2 parts else one part
		if (offset + 8) < (msgLength):
			firststr = msg[offset:offset+8]
			secondstr = msg[offset+8:min(offset+16, msgLength-1)]
		else:
			firststr = msg[offset:(msgLength)]
			secondstr = ""

		# Convert the char to hex format, strip the 0x and then ensure its padded by a 0
		# if needed. It is seperated by a spaceand then pad the string by spaces to have
		# length of 23 for each string part. The parts are seperated by 2 spaces
		hexTxt += (' '.join(hex(ord(x))[2:].zfill(2) for x in firststr)).ljust(23)
		hexTxt += '  '
		hexTxt += (' '.join(hex(ord(x))[2:].zfill(2) for x in secondstr)).ljust(23)
		hexTxt += '  '
		#replace non-printable char with .
		firststr = ''.join([i if ord(i) < 128 and ord(i) > 31 else '.' for i in firststr])
		secondstr = ''.join([i if ord(i) < 128 and ord(i) > 31 else '.' for i in secondstr])

		hexTxt += "|" + firststr + secondstr + "|" +"\n"
		offset += 16

	return hexTxt


def logger(logOption, data, arrow):	

	# if replace flag is on
	if(replaceOpt == True):
		msg = msg.replace(toReplace, replaceWith)

	# no display if no log option, display incoming messages
	if(logOption == ""):
		if(arrow == "<--"):
			msg = msg.split("\n")
			for line in msg:
				print(line)
		return

	# if raw then pass
	elif (logOption == "-raw"):
		pass

	# if log option is strip
	elif(logOption == "-strip"):
		newMsg = ""

		# Replace non printable char with a .
		for char in msg:
			if(ord(char) > 31 and ord(char) < 128):
				newMsg += char
			else:
				newMsg += "."
		msg = newMsg

	elif(logOption == "-hex"):
		msg = toHex(msg)

	else:
		msg = autoN(msg)
	# print line with the directional arrow
	print(arrow,data)


def connectionHandler(clientSocket, serverSocket, logOption):
	incoming = "<--"
	outgoing = "-->"
	# Persistent connection until connection is closed
	while 1:
		readable, writeable, exceptable = select.select([clientSocket,serverSocket],[],[])

		# if there is something to be read from one of the sockets
		for s in readable:
			data = s.recv(1024)

		# Read and Forward the message
			if s == clientSocket:
				logger(logOption, data, outgoing)
				serverSocket.sendall(data)
			else:
				logger(logOption, data, incoming)
				clientSocket.sendall(data)


def main():

	# changing the global bool
	global replaceOpt, toReplace, replaceWith
	# Logging with replace
	if (len(sys.argv) >= 8 and sys.argv[2] == "-replace"):
		logOption = sys.argv[1]
		replaceOpt = True
		toReplace = sys.argv[3]
		replaceWith = sys.argv[4]
		srcPort = sys.argv[5]
		server = sys.argv[6]
		dstPort = sys.argv[7]

	# no logging but replace is present
	elif (len(sys.argv) == 7 and sys.argv[1] == "-replace"):
		logOption = ""
		replaceOpt = True
		toReplace = sys.argv[2]
		replaceWith = sys.argv[3]
		srcPort = sys.argv[4]
		server = sys.argv[5]
		dstPort = sys.argv[6]

	# logging option only
	elif (len(sys.argv) == 5 and not ("-replace" in sys.argv)):
		logOption = sys.argv[1]
		srcPort = sys.argv[2]
		server = sys.argv[3]
		dstPort = sys.argv[4]

	# logging option only
	elif (len(sys.argv) == 4 and not ("-replace" in sys.argv)):
		logOption = ""
		srcPort = sys.argv[1]
		server = sys.argv[2]
		dstPort = sys.argv[3]

	else:
		print("Invalid Command!!: <usage> python3 proxy.py [logOptions] [replaceOptions] srcPort server dstPort")
		sys.exit(0)

	# if log option is -autoN then extract N
	if ("-auto" in logOption):
		global N
		if ((logOption[5:]).isdigit() == True):
			N = int(logOption[5:])
		else:
			print("Error!!! -autoN, N should be an int")

	# else if it's not a valid logOption, exit the program
	elif (logOption not in logOptions):
		print("Error!!! Not a valid Log option")
		sys.exit(0)

	# make a server socket to listen to incoming messages
	listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listenSocket.bind((socket.gethostbyname(""), int(srcPort)))
	listenSocket.listen(5)

	print("Port logger running on " + socket.gethostname() + ": srcPort=" + srcPort  + " host=" + server + " dstPort=" + dstPort)

	# infinite loop to handle multiple clients, start a new thread for each connection
	while 1:
		(clientSocket, addr) = listenSocket.accept()
		conStartTime = datetime.datetime.now()
		print("New connection: " + conStartTime.strftime("%Y-%m-%d %H:%M")	+ ", from " + str(addr[0]))
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serverSocket.connect((socket.gethostbyname(server),int(dstPort)))
		
		# start a thread for every connection
		connectionThread = threading.Thread(target = connectionHandler, args = (clientSocket, serverSocket, logOption))
		connectionThread.start()
main()


