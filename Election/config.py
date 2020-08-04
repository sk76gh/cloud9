##
import random

class Config:
    broadcast='Broadcast'
    multicast='Multicast'
    unicast='Unicast'
    fixedmulticast='FixedMulticast'
    
    
    nodecount=50
    fixedmulticastvalue=nodecount/4
    fanouttype=fixedmulticast
    nodeliveinterval=3
    timeduration=8
    gossipper=random.randint(1,nodecount)
    
    #loggerlist={'INFO':True,'DEBUG':True}
    loggerlist={'INFO':True}
    