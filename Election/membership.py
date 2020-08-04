#membership class

class Membership:
    
    livestatus='LIVE'
    deadstatus='DEAD'
    leaderstatus='LEADER'
    
    def __init__(self,nodeaddr,heartbeat,nodetime,status):
        self.nodeaddr=nodeaddr
        self.nodetime=nodetime
        self.nodeheartbeat=heartbeat
        self.status=status
        
    def __str__(self):
        return 'Memmbership->{'+str(self.nodeaddr)+', '+', '+str(self.nodeheartbeat)+', '+str(self.nodetime)+', '+self.status+'}'