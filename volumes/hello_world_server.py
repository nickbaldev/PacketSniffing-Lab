#!/usr/bin/python3

import socket

# Bind to an IP address to listen to
# Binding to 0.0.0.0 indicates that 
# we want to listen on all incoming
# IP addresses. 
IP = "0.0.0.0"

# TODO: Bind to the port number that the  
# server is listening on. This should 
# match what the client is sending to. 
PORT = 9090 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP,PORT))

while True:
    #TODO: retrieve the data, and ip and port numbers
    #      from the incoming data on the socket
    data, ip = sock.recvfrom(1024)
    
    print("Sender: {} and Port: {}".format(ip, port))
    print("Received message: {}".format(data))
