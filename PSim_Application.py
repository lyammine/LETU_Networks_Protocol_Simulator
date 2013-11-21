from socket import *

host = "localhost"
port = 3000
addr = (host,port)

message = 'Hi! This is a test'
clientSocket = socket(AF_INET, SOCK_DGRAM)
while(1):
    clientSocket.sendto(message,addr)
    print "Sending message...",message

clientSocket.close()
