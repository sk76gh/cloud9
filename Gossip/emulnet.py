# Emulnet responsibility
# keeps list of messages from all nodes
# 
# gives address to each node
# keeps list of all nodes in the network

class EmulNet():
    
    def __init__(self, name):
        print "Emulator Net instantiated.."
        self.nodelist=[]
        self.buffer=[]
        self.name = name
        self.addressid=1
        
    def addNewNode(self,node):
        node.setaddress(str(self.addressid))
        self.nodelist.append(node);
        self.addressid=self.addressid+1
        
    
    def shownodes(self):
        for node in self.nodelist:
            print node
   
    def nodecount(self):
        return len(self.nodelist)
        
    def getNodeList(self):
        return self.nodelist
     
    def addmsg(self, tonodeaddress, msg,fromaddress):
        self.buffer.append([tonodeaddress,msg,fromaddress])
       
    def removemsg(self,nodeaddress):
        for i in range(len(self.buffer)-1,-1,-1):
            if self.buffer[i][0]==nodeaddress:
                del self.buffer[i]
    
    def removethismsg(self,msg):
        for i in range(len(self.buffer)-1,-1,-1):
            if self.buffer[i][0]==msg[0] and self.buffer[i][1]==msg[1]:
                del self.buffer[i]
        
    
    def getmsg(self,nodeaddress):
        tempmsglist=[]
        for msg in self.buffer:
            if msg[0]==nodeaddress:
                tempmsglist.append(msg)
        
        return tempmsglist
    
    def getmsgtype(self, nodeaddress,msgqlf):
        tempmsglist=[]
        tempoutputlist=[]
        
        tempmsglist=self.getmsg(nodeaddress)
        for msg in tempmsglist:
            if msg[1][0]==msgqlf:
                tempoutputlist.append(msg)
                
        return tempoutputlist
    
    def getallmsg(self):
        return self.buffer
        
    def showmsgqueue(self):
        return self.buffer
        
    def buffersize(self):
        return len(self.buffer)
    
    def resetbuffer(self):
        self.buffer=[]
    