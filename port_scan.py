#!/bin/python3

import sys
import socket
from datetime import datetime as dt


#Get IP of remote host that will be scanned.
if len(sys.argv) == 4:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid number of arguments!!")
	print("Proper syntax: port_scan.py <ip> <start port> <end port>")



if (int(sys.argv[2]) >= 0) and (int(sys.argv[2]) <= 65535):
	x = int(sys.argv[2])
else:
	print("Invalid starting port!")
	print("First port must be a port from 0 to 65535.")
	
	
	
if (int(sys.argv[3]) > int(sys.argv[2])) and (int(sys.argv[3]) <= 65535):
	y = int(sys.argv[3])
else: 
	print("Invalid ending port!")
	print("Last port must be greater than first part and no higher than 65535.")


#Create simple banner to display information to user on scan.
t1 = dt.now()
print ("-"* 50)
print("Scanning underway on remote host "+ target)
print("Time started: " + str(t1))
print("-"*50)
print("\n")



#Do port scanning
count = 0
try:
	for port in range(x,y):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))
			count += 1
		s.close()
			
except KeyboardInterrupt:
    print ("\nExiting the program.")
    sys.exit()

except socket.gaierror:
    print ("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Couldn't connect to the server")
    sys.exit()



#Ending banner		
t2 = dt.now()
diff = t2 - t1
print("\n")
print("-"*50)
print("There are {} ports open".format(count))
print("Scan completed in {}".format(diff))
print("-"*50)

	

