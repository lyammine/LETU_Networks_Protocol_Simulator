#Name: Logan Turner & Leila Yammine
#Course: COSC 3603 Networks & Data Communications
#Date: 11/20/13
#Assignment #: Protocol Testing Simulator
#Program Description: 
#Development Environment: Python IDLE

from socket import *

# Table of each session's client, server, and values
sessions = {}

gatewaySocket = socket(AF_INET, SOCK_DGRAM)
gatewayAddress = ("",3000)
gatewaySocket.bind(gatewayAddress)

while true:
    print("Listening...")
    data, addr = gatewaySocket.recvfrom(1024)
    if "@@@RegisterRequest" in data:
        handleRegistration(data, addr)

gatewaySocket.close()


def handleRegistration(data, addr):
    print("Registration request from address {0}:".format(addr))
    print(data)
    # Extract values from message according to specification
    words = data.split()
    clientType = words[1]
    sessionName = words[2]

    matchingSessions = set(s for s in sessions if sessions[s]['SessionName'] == sessionName)

    if matchingSessions:
        
    if clientType == "client":
        clientAddr = addr
        serverAddr = ""
    elif clientType == "server":
        clientAddr = ""
        serverAddr = addr

    if not matchingSessions:
        # This new session is half-complete
        sessions.add(dict(SessionName=sessionName, ClientAddr=clientAddr, ServerAddr=serverAddr))
    else:
        # This existing session is updated
        thisSession = matchingSessions[0]

