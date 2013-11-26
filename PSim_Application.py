# This is a generic client or server application.
# Pass it arguments for "clientType", "sessionName", and "seed".

import sys
from socket import *


# -- Setup --

# Parse command line arguments
clientType = sys.argv[1]
sessionName = sys.argv[2]
seed = sys.argv[3]
print("Arguments OK")

# TODO: Generate random network parameters from seed
through = 10
delay = 500
duplicate = 25
jitterPercent = 25
jitterMax = 250
corruptPackets = 25
corruptBits = 25
timeout = 1000

# Build a gateway registration request
requestTemplate = "@@@RegisterRequest {0} {1}\nthrough {2}\ndelay {3}\nduplicate {4}\njitter {5} {6}\ncorrupt {7} {8}\ntimeout {9}\nseed {10}"
request = requestTemplate.format(clientType, sessionName, through, delay, duplicate, jitterPercent, jitterMax, corruptPackets, corruptBits, timeout, seed)


# -- Register with gateway --

# Gateway's address
host = "localhost"
port = 3000
addr = (host,port)

# Make UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Send registration request to gateway
print("Sending registration request:")
print(request)
clientSocket.sendto(request,addr)

# If confirmed, run client or server application
response = clientSocket.recv(1024)
print("\nResponse:\n{0}".format(response))
if "@@@Confirmation" in response:
    if clientType == "client":
        print("Running client application...")
        runClientApp()
    elif clientType == "server":
        print("Running server application...")
        runServerApp()

clientSocket.close()

def runClientApp():
    for i in range (0,5):
        print("Yay client!")

def runServerApp():
    for i in range (0,5):
        print("Yay server!")
