import sys
import os 
import ipaddress


#----------------------------------------------------------------------------------------------
# Checks the packet with the rules and determines whether to drop, reject or accepts it 
# it calls the appropriate function which returns the proper message
#----------------------------------------------------------------------------------------------
def checkRule(line, config_list, line_num):

	# Initialization
	if(line != "Ignore"):
		fields = line.split(' ')
		direction = fields[0]
		ip = fields[1]
		ports = fields[2]
		flag = fields[3]

	curr_line = 1

	# Check each rules, drop if no matches
	while (curr_line <= len(config_list)):
		# If ignore just skip it
		if(config_list[curr_line - 1] == "Ignore"):
			curr_line += 1
			continue

		config_fields = config_list[curr_line-1].split()

		# Assume that there are no flags set at first 
		config_flag = False 

		# Check if a flag is available
		if(len(config_fields) >4):
			config_flag = True;

		# Check if direction matches with the rule
		if(direction == config_fields[0]):
			# Check if ip address matches
			if(matchIP(ip, config_fields[2].split("\n")[0])):

					# Check if the port matches
					if(matching_ports(ports, config_fields[3])):

						# Check if the rule flag is set but packet flag is 0, then skip
						if(config_flag == True and int(flag) == 0):
							curr_line += 1
							continue
						
						# A rule has been found
						return output_rule(config_fields[1], fields, curr_line)


		curr_line += 1

	# No rule has been found
	return drop_packet(fields)

#----------------------------------------------------------------------------------------------
# Checks if the packet ip falls under the rule ip address, returns bool
#----------------------------------------------------------------------------------------------
def matchIP(ip, ip_range):
	# Wild IP then return true 
	if(ip_range == "*"):
		return 1
	else:
		# Comparing ip address
		rule_ip, mask = ip_range.split("/")
		# Reference: https://stackoverflow.com/questions/19744206/converting-dot-decimal-ip-address-to-binary-python
		# Convert ip to binary
		packet_ip = ''.join(format(int(x), '08b') for x in ip.split('.'))
		rule_ip = ''.join(format(int(x), '08b') for x in rule_ip.split('.'))
		
		# Check only the unmasked part
		if(packet_ip[:int(mask)] == rule_ip[:int(mask)]):
			return True
		else:
			return False

	


#----------------------------------------------------------------------------------------------
# Checks if the ip is valid
#----------------------------------------------------------------------------------------------
def checkIP(ip):
	if(ip == "*"):
		return True
	# Split by .
	ip_split = ip.split(".")

	# check if there are 4 elem
	if(len(ip_split) < 4):
		print(1)
		return False

	# Check if each elem is valid
	for elem in ip_split:
		if(elem.isdigit()):
			if(int(elem) < 0 or int(elem) > 255):
				print(2)
				return False
		else:
			return False	

	return True
#----------------------------------------------------------------------------------------------
# Checks if the packet port matches with the ports specified in the rules, returns bool
#----------------------------------------------------------------------------------------------
def matching_ports(packet_port, ports):
	# If wild port in return true
	if(ports.split()[0] == "*"):
		return True

	# Compare with all of the 
	else:
		ports = ports.split(',')
		for port in ports:
			if(int(packet_port) == int(port)):
				return True
		return False


#-----------------------------------------------------------------------------------------------------------------
# Returns the drop packet message
#-----------------------------------------------------------------------------------------------------------------
def drop_packet(fields):
	return "drop() %s %s %s %s" % (fields[0], fields[1], fields[2], fields[3])



#-----------------------------------------------------------------------------------------------------------------
# Returns the accept or reject message based on the rule
#-----------------------------------------------------------------------------------------------------------------
def output_rule(action, fields, line_num):
	return "%s(%d) %s %s %s %s" % (action, line_num, fields[0], fields[1], fields[2], fields[3])



#-----------------------------------------------------------------------------------------------------------------
# Checks if the rule is valid, returns bool
#-----------------------------------------------------------------------------------------------------------------
def checkRuleLine(line):

	# ignore  line
	if(line == "Ignore"):
		return 1
	# Splitting by white space
	fields = line.split()

	# Check the ranges
	if(len(fields) > 5 or len(fields) < 4):
		return False

	# Variable assignment for simplicity
	direction = fields[0]
	action = fields[1]
	ip = fields[2]
	ports = fields[3] 


	# Check ip and mask
	if(ip != "*"):
		ip_split, mask = ip.split("/")
		if(mask.isdigit()):
			if(int(mask) < 8 or int(mask) > 32):
				sys.stderr.write("invalid IP\n")
				return False
		if(not checkIP(ip_split)):
			sys.stderr.write("invalid IP\n")
			return False

	# If length is >= 5 then set flag and check if its established
	if(len(fields) >=5):
		flag = fields[4] 
		if(flag != "established"):
			sys.stderr.write("Invalid flag \n")
			return False

	# Check direction
	if(direction != "in" and direction != "out"):
		sys.stderr.write("Invalid direction \n")
		return False

	# Check actions
	if(action != "accept" and action != "reject" and action != "drop"):
		sys.stderr.write("Invalid action \n")
		return False

	# Checks port 
	if(ports != "*"):
		ports = fields[3].split(",")
		for port in ports:
			if(port.isdigit()):
				port = int(port)
				if(port < 0 or port > 65536):
					sys.stderr.write("Invalid port range \n")
					return False
			else:
				sys.stderr.write("Port needs to be an int \n")
				return False
	return True

#----------------------------------------------------------------------------------------------
# Check if packet is valid, returns bool
#----------------------------------------------------------------------------------------------
def checkPacketLine(line):

	# Split by white space
	fields = line.split()

	# Check fields
	if(len(fields) < 4):
		return False

	# Initialzation
	direction = fields[0]
	ip = fields[1]
	ports = fields[2] 
	flag = fields[3]

	# Check ip
	if(not checkIP(ip)):
		sys.stderr.write("invalid IP\n")
		return False
	# Check flag
	if(flag != "0" and flag != "1"):
		sys.stderr.write("invalid Flag\n")
		return False

	# Check direction
	if(direction != "in" and direction != "out"):
		sys.stderr.write("Invalid direction \n")
		return False


	# Check port
	if(ports != "*"):
		if(ports.isdigit()):
			ports = int(ports)
			if(ports < 0 or ports > 65536):
				sys.stderr.write("Invalid port range\n")
				return False
		else:
			sys.stderr.write("Port needs to be an int\n")
			return False
	return True


def main():

	if(len(sys.argv) == 2):
		filename = sys.argv[1]; 
	else:
		sys.stderr.write("Error!! usage: python3 fw.py filename\n")
		sys.exit(0)

	# Read the config file into a list
	try:
		config_list = []
		f = open(filename, 'r')
		for line in f:

			# Check if line is blank or is a comment, ignore it
			if(line.isspace() == True or line.strip()[0] == "#"):
				config_list.append("Ignore")
			elif(line.strip().split()[0] != "in" and line.strip().split()[0] != "out"):
				config_list.append("Ignore")
			else:
				config_list.append(line.strip())
			 
	except:
		 sys.stderr.write('Error: Cannot find filename:' + filename +"\n")
		 sys.exit(0)
	

	# Look for any invalid lines in the config file	
	line_num = 0
	for elem in config_list:
		line_num += 1 
		# Prints the line number and the invalid rule
		if(not checkRuleLine(elem)):
			sys.stderr.write("Rule Line Number " + str(line_num )+ "\nError!! " + elem)
			sys.exit(0)
		

	# Reading and checking for any invalid packets
	line_num = 0
	for line in sys.stdin:
		line_num += 1
		# Prints the line number and the invalid packet
		if(not checkPacketLine(line)):
			sys.stderr.write("Packet Line Number " + str(line_num)+ "\nError!! " + line)
			sys.exit(0)
		result = checkRule(line, config_list, line_num)

		
		print(result, end = '')
	
main()
	
