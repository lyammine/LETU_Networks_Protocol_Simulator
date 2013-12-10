#Name: Logan Turner & Leila Yammine
#Course: COSC 3603 Networks & Data Communications
#Date: 11/20/13
#Assignment #: Protocol Testing Simulator
#Program Description: 
#Development Environment: Python IDLE

# This gateway between client and server simulates packet loss, duplication, corruption, and out-of-order delivery.

from socket import *
from texty import *
import datetime

# Table of each session's client, server, and values
sessions = []

gatewaySocket = socket(AF_INET, SOCK_DGRAM)
gatewayAddress = ("",3000)
gatewaySocket.bind(gatewayAddress)

# -- Function Definitions --

def sendConfirmation(addresses):
    confirmationMessage = "@@@Confirmation {0}".format(datetime.datetime.now())
    for address in addresses:
        gatewaySocket.sendto(confirmationMessage, address)
        print("Confirmation sent to {0}".format(address))

def handleRegistration(data, addr):
    print("Registration request from address {0}:".format(addr))
    print(tab(data))
    # Extract values from message according to specification
    words = data.split()
    hostType = words[1]
    sessionName = words[2]

    matchingSession = next((s for s in sessions if s["SessionName"] == sessionName), None)

    if matchingSession:
        thisSession = matchingSession
    else:
        thisSession = dict(SessionName=sessionName, ClientAddr="", ServerAddr="")
        sessions.append(thisSession)
    if hostType == "client":
        thisSession["ClientAddr"] = addr
    if hostType == "server":
        thisSession["ServerAddr"] = addr
    if (thisSession["ClientAddr"] and thisSession["ServerAddr"]):
        print("Creating confirmation message for session \"{0}\"".format(thisSession["SessionName"]))
        sendConfirmation([thisSession["ClientAddr"], thisSession["ServerAddr"]])

while True:
    print("Listening...")
    data, addr = gatewaySocket.recvfrom(1024)
    if "@@@RegisterRequest" in data:
        handleRegistration(data, addr)
    else:
        # Determine from which host the data comes and to which host it should be forwarded
        matchingClientSession = next((s for s in sessions if s["ClientAddr"] == addr), None)
        if matchingClientSession:
            print("Received data from client in session \"{0}\":".format(matchingClientSession["SessionName"]))
            print(tab(data))
            print("Forwarding to server.")
            gatewaySocket.sendto(data, matchingClientSession["ServerAddr"])
        else:
            matchingServerSession = next((s for s in sessions if s["ServerAddr"] == addr), None)
            if matchingServerSession:
                print("Received data from server in session \"{0}\":".format(matchingServerSession["SessionName"]))
                print(tab(data))
                print("Forwarding to client.")
                gatewaySocket.sendto(data, matchingServerSession["ClientAddr"])
            else:
                print("Received data from unknown source. Ignored.")

gatewaySocket.close()
