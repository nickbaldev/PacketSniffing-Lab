#!/usr/bin/env python3
from scapy.all import *

a = IP()
a.dst = '1.2.3.4'
b = ICMP()
pkt = a/b
send(pkt)
