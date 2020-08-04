#network emulator
from queue import Queue
import random, copy
from config import Config
from logger import Logger

class Net:
    def __init__(self, queue):
        self.netmessagequeue=queue
        self.members=list()
        self.logger=Logger()
        
    def getmembercount(self):
        return len(self.members)
        
    def addmember(self,node):
        self.members.append(node)
        
        
    def addqueue(self,queue):
        self.netmessagequeue=queue
        
    def addmessagetoqueue(self,message):
        self.netmessagequeue.messagetoqueue(message)
        
    def addmessagelisttoqueue(self,messagelist):
        self.netmessagequeue.extendlist(messagelist)
    
    def printnetmessagequeue(self):
        for message in self.netmessagequeue.getqueuelist():
            print message.fromaddr,message.toaddr, message.text
    
    
    def getfanoutmemberlist(self):
        fanoutmembers=list()
        fanout=Config.fanouttype
        ### broadcast to all nodes
        if fanout==Config.unicast:
            if len(self.members)>0:
                fanoutmembers=random.sample(self.members,1)
        elif fanout==Config.broadcast:
            fanoutmembers=copy.copy(self.members)
            random.shuffle(fanoutmembers)
        elif fanout==Config.multicast:
            if len(self.members)>0:
                fanoutmembers=random.sample(self.members,random.randint(1,len(self.members)))
        elif fanout==Config.fixedmulticast:
            if len(self.members)>0 and Config.fixedmulticastvalue <= len(self.members):
                fanoutmembers=random.sample(self.members,Config.fixedmulticastvalue)
            elif len(self.members)>0 and Config.fixedmulticastvalue > len(self.members):
                fanoutmembers=random.sample(self.members,len(self.members))
        
        return fanoutmembers
            
    def sendmessagestonodes(self):
        ### implement different types of election algorithms , central leader, ring, bully, paxos
        #print 'inside communicate', len(self.members),self.netmessagequeue.getqueuelist()

        for node in self.members:
            for message in self.netmessagequeue.getmessagesfor(node):
                node.toreceive(message)
            self.netmessagequeue.removemessageof(node)
            node.increaselamporttime()
        return
            
    def nodestoprocess(self):
        for node in self.members:
            node.toprocess()
            node.increaselamporttime()
        return            
            
    def receivemessagesfromnodes(self):
        for node in self.members:
            node.tosendprocessedmessagestonet()
            node.increaselamporttime()
         
    
        ### Mesh topology
        
    def getgossipsummary(self):
        #
        gossipsummary=dict()
        othernodescount=len(self.members)-1 #to exclude self node during 
        for node in self.members:
            #self.logger.debug(str(node.address) +' '+ str(node.getgossipmetric()))
            gossipsummary.update({node.address:node.getgossipmetric()*100/othernodescount})
            
        return gossipsummary
