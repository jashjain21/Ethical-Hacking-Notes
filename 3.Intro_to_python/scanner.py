#!/bin/python3
import sys,socket
from datetime import datetime 

#Define our target
if len(sys.argv) == 2:
	#print(sys.argv)#-------> argv is ['scanner.py', '192.168.1.0']

	target=socket.gethostbyname(sys.argv[1]) #translating host name to ipv4 not necessary we could 		#dirctly declare target=sys.argv[1] bt just taking extra step in case someone just had put a	 	 #hostname 
else:
	print("Invalid amount of arguemnts")
	print("Syntax: python3 scanner.py <ip>")

#isnt a very good script coz if someone types a port which doesnt exist then this might run into ann error na

#creating a banner 
print("-" *50)
print("Scanning Target " + target)
print("Time Started: "+ str(datetime.now())) 
print("-" *50)

try:
	for port in range(50,85):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port)) #connect_ex returns an error indicator if port is open result is going to be 0 if port is closed result back is going to trigger an error which is going to be 1
		if result == 0:
			print("Port {} is open".format(port))
		s.close()#close the connection

except KeyboardInterrupt:
	print("\n Exiting program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("coundt connect to server")
	sys.exit()
	
		
		

#python3 scanner.py <ip>
