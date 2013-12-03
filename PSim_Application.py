# This is a generic client or server application.
# Pass it arguments for "hostType", "sessionName", and "seed".

import sys
from socket import *
from texty import *


# -- Setup --

# Parse command line arguments
hostType = sys.argv[1]
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
request = requestTemplate.format(hostType, sessionName, through, delay, duplicate, jitterPercent, jitterMax, corruptPackets, corruptBits, timeout, seed)


# -- Register with gateway --

# Gateway's address
host = "localhost"
port = 3000
addr = (host,port)

# Make UDP socket
hostSocket = socket(AF_INET, SOCK_DGRAM)

# -- Function Definitions --

def runClientApp():
    for i in range (0,5):
        print("Enter request to send to server:")
        hostSocket.sendto(raw_input("> "), addr)
        print("Waiting for server response...")
        serverData = hostSocket.recv(1024)
        print("Received data from server:")
        print(tab(serverData))
    print("Done!")

def runServerApp():
    for i in range (0,5):
        print("Listening for client requests...")
        clientRequest = hostSocket.recv(1024)
        print("Received request from client:")
        print(tab(clientRequest))
        print("Enter data to return to client:")
        hostSocket.sendto(raw_input("> "), addr)
    print("Done!")

# Send registration request to gateway
print("Sending registration request:")
print(tab(request))
hostSocket.sendto(request,addr)

# If confirmed, run client or server application
response = hostSocket.recv(1024)
print("Response:")
print(tab(response))
if "@@@Confirmation" in response:
    if hostType == "client":
        print("-- Running client application --")
        runClientApp()
    elif hostType == "server":
        print("-- Running server application --")
        runServerApp()

hostSocket.close()
