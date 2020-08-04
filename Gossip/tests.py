from emulnet import EmulNet
from node import Node

    
def asserttest(testname, res, exp,showpass):
    if res==exp:
        if showpass:
           print "PASS : "+ testname+", response = "+str(res)+ ", expected = "+str(exp)
    else: 
        if not showpass:
            print "FAIL : "+ testname+", response = "+str(res)+ ", expected = "+str(exp)

def asserttestcond(testname,res,exp,equality, showpass):
    if res<exp and equality=="lt" and showpass:
        print "PASS : "+ testname+", response = "+str(res)+ ", expected to be less than "+str(exp)
    elif res>exp and equality=="gt" and showpass:
        print "PASS : "+ testname+", response = "+str(res)+ ", expected to be greater than "+str(exp)
    else:
        if not showpass:
            asserttest(testname,res,exp,showpass)
        
        
def runtests():
    showpass=False
    em=EmulNet('emul1')
    n1=Node('node 1')
    em.addNewNode(n1)
    asserttest('Node address test',n1.getaddress(),"1",showpass)
    
    n2=Node('node 2')
    em.addNewNode(n2)
    asserttest('Node address test',n2.getaddress(),"2",showpass)
    
    asserttest('Node add test',em.nodecount(),2,showpass)
    del em
    
    em=EmulNet('emul2')
    em.addmsg("node 1",['message 1',1],"node 2")
    em.addmsg("node 1",['message 2',14],"node 2")
    em.addmsg("node 1",['message 3',15],"node 2")
    em.addmsg("node 2",['message 13',21],"node 1")
    em.addmsg("node 2",['message 15',32],"node 1")
    em.addmsg("node 2",['message 16',52],"node 1")
    em.addmsg("node 2",['message 12',32],"node 1")
    asserttest('Message add test', em.buffersize(),7,showpass)
    
    asserttest("Get msg test 1",len(em.getmsg("node 1")),3,showpass)
    asserttest("Get msg test 2",len(em.getmsg("node 2")),4,showpass)
    em.removemsg("node 2")
    asserttest('Message remove test',em.buffersize(),3,showpass)
   
    em.removemsg("node 1")
    asserttest('Message remove test',em.buffersize(),0,showpass)
    
    em.addNewNode(n1)
    em.addNewNode(n2)
    n1.joingroup(em)
    n2.joingroup(em)
    asserttest("Join msg test 1",len(em.getmsg("1")),1,showpass)
    asserttest("Join msg test 2",len(em.getmsg("2")),1,showpass)
    asserttest("Join msg test 3",em.buffersize(),2,showpass)
    
    n1.processmessages(em)
    asserttest("Join msg test 2",len(em.getmsg("2")),1,showpass)
    asserttest("Msg type test 1",len(em.getmsgtype("2",'Welcome')),1,showpass)
    #print em.getallmsg()
    
    n2.processmessages(em)
    asserttest("Join msg test 3",len(em.getmsg("1")),1,showpass)
    asserttest("Msg type test 2",len(em.getmsgtype("1",'Welcome')),1,showpass)
    #print em.getallmsg()
    
    n1.processmessages(em)
    asserttest("Welcome msg test 1",len(em.getmsg("1")),0,showpass)
    asserttest("Welcome msg type test 1",len(em.getmsgtype("1",'Welcome')),0,showpass)
    #print em.getallmsg()
    
    n2.processmessages(em)
    asserttest("Welcome msg test 2",len(em.getmsg("2")),0,showpass)
    asserttest("Welcome msg type test 2",len(em.getmsgtype("2",'Welcome')),0,showpass)
    print em.getallmsg()
    
    #processat method test
    n3=Node('node 3')
    n4=Node('node 4')
    em.addNewNode(n3)
    em.addNewNode(n4)
    
    n3.processat(1,em)
    asserttest("join msg test",len(em.getmsgtype("3",'Join')),1,showpass)
    asserttest("welcome msg test",len(em.getmsgtype("3",'Welcome')),0,showpass)
    #print em.getallmsg()
    n4.processat(2,em)
    asserttest("join msg test",len(em.getmsgtype("4",'Join')),1,showpass)
    asserttest("welcome msg test",len(em.getmsgtype("4",'Welcome')),0,showpass)
    asserttest("join msg test",len(em.getmsgtype("3",'Join')),0,showpass)
    asserttest("welcome msg test",len(em.getmsgtype("3",'Welcome')),1,showpass)
    #print em.getallmsg()
    n3.processat(3,em)
    asserttest("join msg test",len(em.getmsgtype("3",'Join')),0,showpass)
    asserttest("welcome msg test",len(em.getmsgtype("3",'Welcome')),0,showpass)
    #print em.getallmsg()
    n4.processat(4,em)
    asserttest("join msg test",len(em.getmsgtype("4",'Join')),0,showpass)
    asserttest("welcome msg test",len(em.getmsgtype("4",'Welcome')),0,showpass)
    #print em.getallmsg()

    #send heartbeat to neighbours
    em.resetbuffer()
    n1.sendheartbeattoneighbours(em)
    asserttestcond("heartbeat msg test",len(em.getmsgtype("1","Heartbeat")),0,"gt",showpass)
    asserttestcond("heartbeat msg test",len(em.getmsgtype("1","Heartbeat")),3,"lt",showpass)

    #send heartbeat to neighbours
    em.resetbuffer()
    n2.sendheartbeattoneighbours(em)
    asserttestcond("heartbeat msg test",len(em.getmsgtype("1","Heartbeat")),0,"gt",showpass)
    asserttestcond("heartbeat msg test",len(em.getmsgtype("1","Heartbeat")),3,"lt",showpass)
    
    #*************************START: send heart beat test ****************
    em.resetbuffer()
    n1.getmember().resetmembershiplist()
    n2.getmember().resetmembershiplist()
    n3.getmember().resetmembershiplist()
    n4.getmember().resetmembershiplist()
    n2.sendheartbeattoneighbours(em)
    
    msgcount=0
    othermsgcount=0
    for item in em.getallmsg():
        if item[0]=='2':
            msgcount=msgcount+1
        if item[2]!='2':
            othermsgcount=othermsgcount+1
    asserttest("heartbeat count test", msgcount, len(em.getallmsg()),showpass)
    asserttest("msg sent to other node count test", othermsgcount, len(em.getallmsg()),showpass)
    #print em.getallmsg()
    #*************************END: send heart beat test ****************

if __name__=='__main__':
    runtests()