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



#Create simple banner to display information to user on scan.
t1 = dt.now()
print ("-"* 50)
print("Scanning underway on remote host "+ target)
print("Time started: " + str(t1))
print("-"*50)


try:
	for port in range(int(sys.argv[2]),int(sys.argv[3])):
		s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect((target, port))
		if result == 0:
			print("Port {} is open".format(port))
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
		
t2 = dt.now()
diff = t2 - t1
print("Scan completed in {}".format(diff))

	

