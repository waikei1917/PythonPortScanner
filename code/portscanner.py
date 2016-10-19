import socket
import subprocess
import sys
from datetime import datetime

print('Hello')
#clear the screen
subprocess.call('clear',shell=True)

#Ask for input
remoteServer = input("Enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

#print a banner with information on which host we are about to scan
print("-"*60)
print("Please wait, scanning remote host", remoteServerIP)
print("-"*60)

#Check scan start time
t1 = datetime.now()

#scan port 1 to 1024
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print("Port {}:     open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()

t2 = datetime.now()

total = t2-t1

print("Scanning Completed in:",total)

