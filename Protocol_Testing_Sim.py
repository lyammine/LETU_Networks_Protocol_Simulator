#Name: Logan Turner & Leila Yammine
#Course: COSC 3603 Networks & Data Communications
#Date: 11/20/13
#Assignment #: Protocol Testing Simulator
#Program Description: 
#Development Environment: Python IDLE

# This gateway between client and server simulates packet loss, duplication, corruption, and out-of-order delivery.

from socket import *
import datetime

# Table of each session's client, server, and values
<<<<<<< HEAD
sessions = {}

gatewaySocket = socket(AF_INET, SOCK_DGRAM)
gatewayAddress = ("",3000)
gatewaySocket.bind(gatewayAddress)


=======
sessions = []

# -- Function Definitions --
>>>>>>> c33c78841df766d80bbcced4788255036ae035b3

def sendConfirmation(addresses):
    confirmationMessage = "@@@Confirmation {0}".format(datetime.datetime.now())
    for address in addresses:
        gatewaySocket.sendto(confirmationMessage, address)
        print("Confirmation sent to {0}".format(address))

def handleRegistration(data, addr):
    print("Registration request from address {0}:".format(addr))
    print("\t{0}".format(data.replace("\n", "\n\t")))
    # Extract values from message according to specification
    words = data.split()
    clientType = words[1]
    sessionName = words[2]

<<<<<<< HEAD
    matchingSessions = set(s for s in sessions if sessions[s]['SessionName'] == sessionName)
        

    if not matchingSessions:
         if clientType == "client":
            clientAddr = addr
            serverAddr = ""
        elif clientType == "server":
            clientAddr = ""
            serverAddr = addr
        # This new session is half-complete
        entry = dict(SessionName=sessionName, ClientAddr=clientAddr, ServerAddr=serverAddr)
        sessions.add(entry)
=======
    matchingSession = next((s for s in sessions if s["SessionName"] == sessionName), None)

    if matchingSession:
        thisSession = matchingSession
>>>>>>> c33c78841df766d80bbcced4788255036ae035b3
    else:
        thisSession = dict(SessionName=sessionName, ClientAddr="", ServerAddr="")
        sessions.append(thisSession)
    if clientType == "client":
        thisSession["ClientAddr"] = addr
    if clientType == "server":
        thisSession["ServerAddr"] = addr
    if (thisSession["ClientAddr"] and thisSession["ServerAddr"]):
        print("Creating confirmation message for session \"{0}\"".format(thisSession["SessionName"]))
        sendConfirmation([thisSession["ClientAddr"], thisSession["ServerAddr"]])

gatewaySocket = socket(AF_INET, SOCK_DGRAM)
gatewayAddress = ("",3000)
gatewaySocket.bind(gatewayAddress)

<<<<<<< HEAD
if __name__ == "__main__":
    
    while(1):
        print("Listening...")
        data, addr = gatewaySocket.recvfrom(1024)
        if "@@@RegisterRequest" in data:
            handleRegistration(data, addr)

    gatewaySocket.close()
=======
while True:
    print("Listening...")
    data, addr = gatewaySocket.recvfrom(1024)
    if "@@@RegisterRequest" in data:
        handleRegistration(data, addr)

gatewaySocket.close()
>>>>>>> c33c78841df766d80bbcced4788255036ae035b3
