#
from logger import Logger

class GossipTracker:
    
    def __init__(self):
        self.nodemessagecount=dict()
        self.gossiptext=''
        self.logger=Logger()
        
    def track(self, message):
        
        if len(self.nodemessagecount)==0:
            self.gossiptext=message.text
            
        
        if self.gossiptext==message.text:
            if message.fromaddr in self.nodemessagecount.keys():
                self.nodemessagecount.update({message.fromaddr:self.nodemessagecount[message.fromaddr]+1})
            elif message.fromaddr not in self.nodemessagecount.keys():
                self.nodemessagecount.update({message.fromaddr:1})
            
    def gossipmetric(self):
        ''' 
        calculate the gossip metric
        '''
        #self.logger.debug(self.nodemessagecount)
        return len(self.nodemessagecount)
        
