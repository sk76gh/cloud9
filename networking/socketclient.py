from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",50001))
#print "sock name",s.getsockname()
s.send("save")
for x in range(10):
    s.send("string C")
data=s.recv(20000)
print data
s.close
