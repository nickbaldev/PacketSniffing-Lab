#!/usr/bin/python3

import socket

# TODO: specify the IP address we want
#to send to (in this case localhost which
# maps to 127.0.0.1
IP = "10.9.0.6"

# TODO: Specify a port number between 9000 and 9090
# Since we aren't really speaking specific 
# application layer protocol, we can define our own custom 
# port number. 
PORT = 9090

# Encode our application layer data as bytes
data = b'Hello, World!'

# We are now ready to send our data out!
# We will use the socket API to do so. The 
# socket API is like our network mailbox.
# Just like mail comes in and goes out. 
# The socket API maintains two buffers, one
# for packets coming in and one for packets going out. 

# Each time we call socket.socket(), we're setting 
# up a new socket instance (i.e.,a new mailbox) 
# so that no two sockets interact. 

# With UDP, (socket.SOCK_DGRAM), we can reuse a 
# socket if we like. UDP offers "connectionless" 
# service which is the equivalent of chucking the 
# packet into the network and hoping for the best!

# With TCP, we setup state for the packet. I.e., we
# keep track of how many bytes were transferred 
# and acknowledged successfully, and so in this case, 
# we clearly need our socket mailbox to only be 
# responsible for one connection at a time. 

# In our socket instance, we are saying we want to use
# address family (AF) of the Internet Protocol (there's
# no other choice really) and the UDP or connectionless
# transport service (socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(data, (IP, PORT))

