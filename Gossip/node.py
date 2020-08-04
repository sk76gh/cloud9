import random
from process import Process 

# node responsibility
# interacts between emulnet and process member
# manages gossip protocol for the process member
# ensures info from its process member is distributed to processes in entire emulnet nodes

class Node:
    
    def __init__(self, name):
        self.name=name
        self.address="Null"
        self.ingroup=False
        self.failed=False
        self.member=Process()
        self.neighbourcount=4
        
        print self.name + " instantiated"
        
    def __str__(self):
        return self.name + ", address : "+self.address
    
    def getmember(self):
        return self.member
        
    def setaddress(self,addr):
        self.address=addr
        self.member.setmynodeaddress(addr)
        
    def getaddress(self):
        return self.address
        
    def processat(self,timestamp,emulnet):
        if self.failed:
            return
        if not self.ingroup:
            self.joingroup(emulnet)
        else:
            self.sendheartbeattoneighbours(emulnet)
        
        self.processmessages(emulnet)
            
    
    def registrationinprogress(self,emulnet):
        if len(emulnet.getmsgtype(self.address,"Welcome"))>0 or len(emulnet.getmsgtype(self.address,"Join"))>0:
            return True
        
        return False
        
    def joingroup(self,emulnet):
        # send join request to neighbours
        if not self.registrationinprogress(emulnet):
            emulnet.addmsg(self.address,["Join",self.member.getHeartBeat()],"Broadcast")
        return
        
    def processmessages(self,emulnet):
        #process join request and send ack back
        #received ack back to self, then join flag=true
        #process other request
        mymsg=[]
        mymsg=list(emulnet.getallmsg())
        #print "Inside processmessage for node "+self.address
        
        for msg in mymsg:
            #send welcome message to other node and delete join message from buffer
            if msg[0]!=self.address:
                if msg[1][0]=="Join":
                    emulnet.removethismsg(msg)
                    emulnet.addmsg(msg[0],["Welcome",msg[1][1]],msg[2])
                    print "send welcome message for node "+msg[0]
                    
            #if welcome message received from other node, then set ingroup flag to true and delete welcome message from buffer
            if msg[0]==self.address and not self.ingroup:
                if msg[1][0]=="Welcome":
                    self.ingroup=True
                    emulnet.removethismsg(msg)
                    print "node "+msg[0]+" joined group"
            elif msg[2]==self.address and self.ingroup:
                self.handlemessagetype(msg)
                
        
                
    
    def handlemessagetype(self,msg):
        #handle each message
        #print 'node ',self.address,' message send to me ',msg
        #print 'message before updatemembership ',msg,msg[2], msg[1][1]
        self.member.updatemembership(msg)    
        return
        
    def sendheartbeattoneighbours(self,emulnet):
        #send heartbeat to neighbours
        myheartbeat=self.member.getHeartBeat()
        allnodelist=emulnet.getNodeList()
        #print neighbours
       
        #select neighbour nodes from allnodes list
        randomindexlist=[x for x in range(len(allnodelist))]
        random.shuffle(randomindexlist)
        
        for neighbourindex in randomindexlist[:self.neighbourcount]:
            #print neighbourindex
            neighbournode=allnodelist[neighbourindex]
            neighbouraddress=neighbournode.getaddress()
            #print "neighbour address ",neighbouraddress
            if neighbouraddress!=self.address:
                emulnet.addmsg(self.address,["Heartbeat",myheartbeat,self.getmember().getgossipmessage(), self.getmember().getmembershiplist()],neighbouraddress)
                print neighbourindex," node ",self.address , " sent heart beat to ",neighbouraddress,self.getmember().getgossipmessage()
        return
        
                
