# Session.py
# Classes for handling individual connection sessions

from texty import *

class Session:

    def __init__(self, simulator, sessionName):
        self.simulator = simulator
        self.name = sessionName

    def readyForData():
        return self.clientAddress and self.serverAddress


    def registerHost(address, isClient, networkParameters):
        if isClient:
            self.clientAddress = address
        else:
            self.serverAddress = address
        self.networkParameters = networkParameters
        if readyForData():
            simulator.SendConfirmation([clientAddress, serverAddress])

    def forwardData():



    def HandleMessage(sessionName, sourceAddress, message):

        # -- Determine if the message belongs to me. --

        # If sessionName is non-empty and different from my own, reply that I can't take it
        if sessionName and (sessionName != self.name):
            return false

        # If sessionName or sourceAddress is mine, reply that I can take it
        if (sessionName == self.name) or (sourceAddress == self.clientAddress) or (sourceAddress == self.serverAddress):
            print("Session \"{0}\" claims this message".format(self.name))
            # determine message type, send it to the thread
            return true;


        # -- Determine what kind of message this is: registration or data --

        # registration from the first host gets recorded, check for parameter errors, registration timeout begins

        # registration from the second host gets recorded, check for parameter errors, confirmation gets sent out
            # registration timeout ends, data timeout begins

        # data from an unconfirmed host gets an error message sent back

        # data from a confirmed host gets passed on to the other host
