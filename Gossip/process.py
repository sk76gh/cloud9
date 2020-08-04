# process responsibility
# hold process info that potentially needs to be distributed to entire emulnet
# holds heatbeat
# holds fail detection info
#membershiplist structure: {'nodeaddress1': (heartbeat, 'LIVE/DEAD'),'nodeaddress2':....}

class Process:
    
    def __init__(self):
        self.heartbeat=0
        self.livetimedelta=2
        self.mynodeaddress=''
        self.membershiplist=dict()
        self.gossipmessage=dict()
        
    def setmynodeaddress(self,mynodeaddress):
        self.mynodeaddress=mynodeaddress
        if mynodeaddress=='2':
            self.setgossipmessage({'gossip':'gossip!shhh!!'})
        
    def getHeartBeat(self):
        self.heartbeat=self.heartbeat+1
        return self.heartbeat
        
    def resetmembershiplist(self):
        self.membershiplist=dict()
        
    def getmembershiplist(self):
        return self.membershiplist
        
    def getmember(self,nodeaddress):
        for member in self.membershiplist:
            if member.key==nodeaddress:
                return member
        return
    
    def getgossipmessage(self):
        return self.gossipmessage
    
    def setgossipmessage(self,message):
        self.gossipmessage.update(message)
        
    
    def updatemembership(self,msg):
        nodeaddress=msg[0]
        nodeheartbeat=msg[1][1]
        nodegossipmessage=msg[1][2]
        neighbourmembershiplist=msg[1][3]
        #if recevied any gossip, then process and save it
        if nodegossipmessage!="":                
            self.setgossipmessage(nodegossipmessage)


        for nodeaddress in neighbourmembershiplist:
            nodeheartbeattuple=neighbourmembershiplist[nodeaddress]
            nodeheartbeat=nodeheartbeattuple[0]
            if nodeaddress in self.membershiplist:
                #print nodeheartbeat,self.heartbeat,self.livetimedelta
                if nodeheartbeat<self.heartbeat-self.livetimedelta:
                    self.membershiplist[nodeaddress]=(nodeheartbeat,'DEAD')
                elif self.membershiplist[nodeaddress][0]<nodeheartbeat:
                    self.membershiplist[nodeaddress]=(nodeheartbeat,'LIVE')
            else:
                #self.membershiplist[nodeaddress]=(nodeheartbeat,'LIVE')
                self.membershiplist[nodeaddress]=nodeheartbeattuple
        #update self heartbeat to the membership list
        self.membershiplist[self.mynodeaddress]=(self.heartbeat,'LIVE')