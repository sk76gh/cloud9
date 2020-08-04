#membershiplist class
from membership import Membership

class Membershiplist:
    
    def __init__(self):
        self.membershiplist=dict()
    
    def getmembershiplist(self):
        return self.membershiplist
        
    def has(self, membershipaddr):
        
        if membershipaddr in self.membershiplist.keys():
            return True
        else:
            return False
        
    def toupdatestatusfor(self, membership):
        self.membershiplist.update({membership.nodeaddr:membership})
    
    def getmembershipfor(self, message):
        return self.membershiplist.get(message.fromaddr)
        
    def processgossipsfromothernodemessage(self, othernodemessage,heartbeat,lamporttime):
        print '\n**********other list*********\n'
        print othernodemessage.membershiplist
        print '\n********self list***********\n'
        print self
        
        for nodeaddr in othernodemessage.membershiplist.membershiplist.keys():
            print nodeaddr, self.has(nodeaddr), othernodemessage.membershiplist.membershiplist[nodeaddr]
            othernodemembership=othernodemessage.membershiplist.membershiplist[nodeaddr]
            if self.has(nodeaddr):
                # verify time before adding
                print
            else:
                self.toupdatestatusfor(othernodemembership)
                
        print '\n*************after adding missing members**************\n'
        print self
        
        #include self message with my heartbeat
        newmembership=Membership(othernodemessage.fromaddr,heartbeat,lamporttime,Membership.livestatus)
        self.toupdatestatusfor(newmembership)
         
    def processfordeadmembers(self, nodelamporttime, liveinterval):
        #check each membership and update as 'Deadstatus' if interval exceeds liveinterval
        for membership in self.membershiplist.values():
            if (nodelamporttime-membership.nodetime)>liveinterval:
                membership.status=Membership.deadstatus
                self.toupdatestatusfor(membership)
    
    def getlivenodes(self):
        livenodelist=dict()
        for membership in self.getmembershiplist().values():
            if membership.status == Membership.livestatus:
                livenodelist.update({membership.nodeaddr:membership})
                
        return livenodelist        
            
    def __str__(self):
        outputstring=''
        for membership in self.membershiplist.values():
            outputstring=outputstring+membership.__str__()+'\n'
            
        return outputstring