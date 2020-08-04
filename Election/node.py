#node file
from message import Message
from membership import Membership
from membershiplist import Membershiplist
from net import Net
import random, copy
from config import Config
from logger import Logger
from gossiptracker import GossipTracker

class Node:
    def __init__(self, name, address,net):
        self.name=name
        self.address=address
        self.time=0
        self.networkmessagequeue=list()
        self.net=net
        self.messagestobeprocessed=list()
        self.processedmessages=list()
        self.membershiplist=Membershiplist()
        self.gossiptracker=GossipTracker()
        self.live=True
        self.lamporttime=0
        self.liveinterval=Config.nodeliveinterval
        self.heartbeat=0
        self.logger=Logger(Config.loggerlist)
        
        ##say hello to a random node
        if Config.gossipper==self.address:
            self.logger.info('Gossipper node is :'+str(self.address))
            self.preparemygossipmessage()
            self.tosendprocessedmessagestonet()

        return
    
    
    
    def getgossipmetric(self):
        '''
        return nodes gossip metric
        '''
        return self.gossiptracker.gossipmetric()
    
    def incrementheartbeat(self):
        self.heartbeat=self.heartbeat+1
    
    

    def printmessagestobeprocessed(self):
        for message in self.messagestobeprocessed:
            print (message)
    
    def printprocessedmessages(self):
        for message in self.processedmessages:
            print (message)
            
    def increaselamporttime(self):
        self.lamporttime=self.lamporttime+1
        #self.logger.debug('node '+str(self.address)+' lamport time :'+str(self.lamporttime))
        
    def flushprocessedmessagelist(self):
        self.processedmessages=list()
    
    def flushmessagestobeprocessed(self):
        self.messagestobeprocessed=list()
  
    def ismemberinlivestatus(self, nodeaddr):
        if nodeaddr in self.membershiplist.getlivenodes().keys():
            return True
        else:
            return False
    
    def preparemygossipmessage(self):
        nodelist=self.net.getfanoutmemberlist()
        
        if len(nodelist)>0:
            if self in nodelist:
                nodelist.remove(self)
            for node in nodelist:
                self.processedmessages.append(Message(self.address,node.address,Message.GOSSIPTYPE,'Hello from node '+str(self.address),self.lamporttime, self.membershiplist))

    def preparegossipmessages(self,gossipmessage):
        nodelist=self.net.getfanoutmemberlist()
        
        if len(nodelist)>0:
            if self in nodelist:
                nodelist.remove(self)
            for node in nodelist:
                self.processedmessages.append(Message(self.address,node.address,Message.GOSSIPTYPE,gossipmessage.text,self.lamporttime, self.membershiplist))

    def processgossips(self):
        for message in self.messagestobeprocessed:
            if message.type==message.GOSSIPTYPE:
                self.logger.debug(str(self.address)+' processing gossip message -> '+message.text)
                #if gossip message is received, then add/update node with live status
                #self.membershiplist.processgossipsfromothernodemessage(message,self.heartbeat, self.lamporttime)
                #send the gossip message to fanned out list
                self.preparegossipmessages(message)
        #evaluate dead nodes
        #self.membershiplist.processfordeadmembers(self.lamporttime,self.liveinterval)

        return
        
    def processmessagesfromnet(self):
        self.processgossips()
        #self.processleadermessages
        self.flushmessagestobeprocessed()
        
    def toreceive(self, message):
        self.logger.debug(str(self.address)+ ' received message '+str(message.text)+' from '+str(message.fromaddr))
        self.messagestobeprocessed.append(message)
        self.gossiptracker.track(message)
        self.incrementheartbeat()
        return
        
    def toprocess(self):
        
        self.logger.info('***************** '+str(self.address)+'- processing ******************')
        self.processmessagesfromnet()
        #increment heartbeat before sending a message out to the net
        self.incrementheartbeat()
        #self.tosendprocessedmessagestonet()
        return
    
    def tosendprocessedmessagestonet(self):
        #print '***************** ',self.address,'- sending ******************'
        if len(self.processedmessages)>0:
            tempprocessedmessagelist=copy.copy(self.processedmessages)
            self.net.addmessagelisttoqueue(tempprocessedmessagelist)
        self.flushprocessedmessagelist()
        self.incrementheartbeat()
        return 
    
    

