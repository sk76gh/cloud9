#message class

class Message:
    
    GOSSIPTYPE='Gossip'
    
    def __init__(self, fromaddr,toaddr,type, text,time,membershiplist):
        self.fromaddr=fromaddr
        self.toaddr=toaddr
        self.text=text
        self.type=type
        self.nodelamporttime=time
        self.membershiplist=membershiplist
        
    def __str__(self):
        return 'Message ['+str(self.fromaddr)+'->'+str(self.toaddr)+','+self.type+','+self.text+', '+str(self.nodelamporttime)+','+str(self.membershiplist)+']'