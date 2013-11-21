#Name: Logan Turner & Leila Yammine
#Course: COSC 3603 Networks & Data Communications
#Date: 11/20/13
#Assignment #: Protocol Testing Simulator
#Program Description: 
#Development Environment: Python IDLE

from socket import *

gatewaySocket = socket(AF_INET, SOCK_DGRAM)
addr = ("",3000)
gatewaySocket.bind(addr)

data, addr = gatewaySocket.recvfrom(1024)
print "IP addr, protocol port:",addr



gatewaySocket.close()
