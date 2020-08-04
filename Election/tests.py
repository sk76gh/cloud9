#test class
from queue import Queue
from message import Message
from node import Node
from net import Net
from membership import Membership
from membershiplist import Membershiplist
from gossiptracker import GossipTracker
import app
from logger import Logger

def asserttest(testname, res, exp,showpass):
    if res==exp:
        if showpass:
           print "PASS : "+ testname+", response = "+str(res)+ ", expected = "+str(exp)
    else: 
        if not showpass:
            print "FAIL : "+ testname+", response = "+str(res)+ ", expected = "+str(exp)


def main():
    showpass=False
    q=Queue()
    n=Net(q)
    ml=Membershiplist()
    m1=Message('1','2','test','message1',23,ml)
    m2=Message('1','3','test','message2',44,ml)
    q.messagetoqueue(m1)
    q.messagetoqueue(m2)
    q.printqueue()
    
    #check node count
    q=Queue()
    n=Net(q)
    n1=Node('node',1,n)
    n.addmember(n1)
    asserttest('1 Node count check: ',n.getmembercount(),1,showpass)

    #check node count
    n2=Node('node',2,n)
    n.addmember(n2)
    asserttest('2 Node count check: ',n.getmembercount(),2,showpass)

    
    ### test node.py
    n3=Node('node',3,n)
    n.addmember(n3)
    #check initial message flush
    asserttest('3 Node test: check intial message flush : ',len(n3.messagestobeprocessed),0,showpass)
    
    #check message count in net
    asserttest('4 Node test: check messages in net : ',len(n.netmessagequeue.getqueuelist()),3,showpass)
    
    #***********test app.printmembershipsummary() method *************************
    #*****Node 1 list*****************
    m1=Membership(1,2,1,Membership.livestatus)
    m2=Membership(2,5,1,Membership.livestatus)
    m3=Membership(3,3,1,Membership.deadstatus)
    ms=Membershiplist()
    ms.toupdatestatusfor(m1)
    ms.toupdatestatusfor(m2)
    ms.toupdatestatusfor(m3)
    n1.membershiplist=ms
    
    #*****Node 2 list*****************
    m4=Membership(1,4,1,Membership.livestatus)
    m5=Membership(2,5,1,Membership.deadstatus)
    m6=Membership(3,6,1,Membership.livestatus)
    ms=Membershiplist()
    ms.toupdatestatusfor(m4)
    ms.toupdatestatusfor(m5)
    #ms.toupdatestatusfor(m6)
    n2.membershiplist=ms
    
    #*****Node 3 list*****************
    m7=Membership(1,3,1,Membership.livestatus)
    m8=Membership(2,6,1,Membership.livestatus)
    m9=Membership(3,3,1,Membership.livestatus)
    ms=Membershiplist()
    ms.toupdatestatusfor(m7)
    ms.toupdatestatusfor(m8)
    ms.toupdatestatusfor(m9)
    n3.membershiplist=ms
    
    app.printmembershipsummary(n) # expected answer is (1,3) (2,2) (3,0)
 
    #test logger
    loggerlist={'INFO':True,'DEBUG':True}
    logger=Logger(loggerlist)
    
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    
    #gossip tracker tests
    print '**********gossip tracker*************'
    ml=Membershiplist()
    m1=Message('1','2','test1','message1',23,ml)
    m2=Message('2','2','test1','message2',44,ml)
    m3=Message('1','2','test1','message1',47,ml)
    m4=Message('3','2','test1','message1',43,ml)
    m5=Message('3','2','test2','message2',43,ml)
    m6=Message('3','2','test2','message1',43,ml)
    gt=GossipTracker()
    gt.track(m1)
    gt.track(m2)
    gt.track(m3)
    gt.track(m4)
    gt.track(m5)
    gt.track(m6)
    print gt.gossipmetric()

    
if __name__=='__main__':
    main()