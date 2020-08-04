#queue class

class Queue:
    def __init__(self):
        self.queue=list()
        
    def getqueuelist(self):
        return self.queue
        
    def messagetoqueue(self,message):
        self.queue.append(message)
        
    def extendlist(self,messagelist):
        self.queue.extend(messagelist)
        
    def removemessage(self,message):
        self.queue.remove(message)
        
    def getmessagesfor(self,node):
        messagesfornode=list()
        for message in self.queue:
            if message.toaddr==node.address:
                messagesfornode.append(message)
                
        return messagesfornode
                
    def removemessageof(self,node):
        updatedqueue=list()
        for message in self.queue:
            if message.toaddr!=node.address:
                updatedqueue.append(message)
                
        self.queue=updatedqueue        
                
    def printqueue(self):
        print "queue size ", len(self.queue)
        for message in self.queue:
            print message
    