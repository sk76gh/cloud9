#main class
from queue import Queue
from node import Node
from net import Net 
from config import Config
from logger import Logger




def printmembershipsummary(net):
    memberlistsummary=dict()
    logger=Logger()
    for node in net.members:
        membershiplist=node.membershiplist
        #print node.address, membershiplist
        #loop through each node
        for nodeaddr in membershiplist.membershiplist.keys():
            #check of nodes that are in live status
            if node.ismemberinlivestatus(nodeaddr):
                #check if live nodes are already listed in livememberlistsummary list
                if nodeaddr in memberlistsummary.keys():
                    memberlistsummary.update({nodeaddr:memberlistsummary.get(nodeaddr)+1})
                    #print 'increasing node count', nodeaddr, memberlistsummary.get(nodeaddr)
                else:
                    memberlistsummary.update({nodeaddr:1})
                    #print 'add new node', nodeaddr, memberlistsummary.get(nodeaddr)

    
    logger.info('***************node summary*************')
    for items in memberlistsummary.items():
        logger.info(items)
    
def main():
    ###initialize network
    logger=Logger()
    logger.info('..................initializing network...............')
    nodecount=Config.nodecount
    q=Queue()
    n=Net(q)
    logger=Logger(Config.loggerlist)

    for i in range(nodecount):
        n.addmember(Node('node',i,n))
        
    logger.debug(len(n.members))
    for node in n.members:
        logger.debug(str(node.name)+str(node.address))
        
    logger.info('initialized messages in queue')
    logger.debug(n.printnetmessagequeue())
    logger.info('.....................processing network messages...........')
    # process each node
    timeinterval=Config.timeduration
    for tick in range(timeinterval*3):
        if(tick%3==0):
            logger.debug('time tick'+str(tick)+' sending messages to node')
            n.sendmessagestonodes()
        
        if((tick-1)%3==0):
            logger.debug('time tick'+str(tick)+' nodes processing')
            n.nodestoprocess()
            
        if((tick-2)%3==0):
            logger.debug('time tick'+str(tick)+' nodes sending processed messages')
            n.receivemessagesfromnodes()
    
    printmembershipsummary(n)
    print (n.getgossipsummary())
    
    
if __name__=='__main__':
    main()