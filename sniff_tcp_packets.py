#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

#TODO: sniff on the interface for net-10.9.0.0
pkt = sniff(iface=['enp0s3', 'net-10.9.0.0'], filter='tcp and port 80', prn=print_pkt)
