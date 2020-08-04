from emulnet import EmulNet
from node import Node

# responsibility
# intiates emulnet
# populates nodes in Emulnet
# gives node its name

#state
#populates nodes in emulnet
# emulnet allocates address for each node

def main():
    en=EmulNet('emul')
    globalNodeCount=100
    simulationtime=7
    for i in range(globalNodeCount):
        en.addNewNode(Node("node "+str(i)))

    #print en.shownodes()
    
    nodes=en.getNodeList()
    for timestamp in range(simulationtime):
        for node in nodes:
            node.processat(timestamp,en)
            
    #print en.showmsgqueue()
    nodecount=len(en.getNodeList())
    gossipcount=0.0
    gossipednodes=[]
    for node in en.getNodeList():
        livecount=0.0
        dictcount=0.0
        for value in node.getmember().getmembershiplist().values():
            dictcount=dictcount+1
            if value[1]=='LIVE':
                livecount=livecount+1
        if dictcount>0:
            print 'Node ',node.getaddress(),' : ', 'Accuracy' , "% 3.1f" % (livecount/dictcount*100), '(',livecount,'/',dictcount,')',\
            'Completeness' , "% 3.1f" % (dictcount/nodecount*100), '(',dictcount,'/',nodecount,')'            
        else:
            print 'Node ',node.getaddress(),' : ',  "% 3.1f" % (0), '(',livecount,'/',dictcount,')',\
            'Completeness' , "% 3.1f" % (dictcount/nodecount*100), '(',dictcount,'/',nodecount,')' 
        #print node.getaddress(), " => ",node.getmember().getmembershiplist()
        if node.getmember().getgossipmessage()['gossip']=='gossip!shhh!!':
            gossipcount=gossipcount+1
            gossipednodes.append(node.getaddress())
            
    print 'gossip message spread ratio',gossipcount, nodecount, gossipcount/nodecount
    print 'gossiped nodes', gossipednodes
    
if __name__=='__main__':
    main()