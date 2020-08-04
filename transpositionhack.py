from transpositioncipher import decript, encript
from detectEnglish import isEnglishstring
import random

myMessagetest = """Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English mathematician, 
philosopher, inventor and mechanical engineer who originated the concept of a programmable computer. 
Considered a "father of the computer", Babbage is credited with inventing the first mechanical computer
that eventually led to more complex designs. Parts of his uncompleted mechanisms are on display in the 
London Science Museum. In 1991, a perfectly functioning difference engine was constructed from Babbage's 
original plans. Built to tolerances achievable in the 19th century, the success of the finished engine 
indicated that Babbage's machine would have worked. Nine years later, the Science Museum completed the 
printer Babbage had designed for the difference engine."""


def main():

    ekey=random.randint(1,len(myMessagetest))
    myMessage=encript(ekey,myMessagetest)
    print ekey, myMessage
    print "decripting ......."
    #print decript(8,emessage)     
    #print len(myMessage)
    for key in range(1,len(myMessage)):
        decriptedmessage=decript(key,myMessage)
        #print decriptedmessage
        triplelist=isEnglishstring(decriptedmessage)
        percent=(float(triplelist[0])/triplelist[1])*100
        #print key,triplelist[0],triplelist[1],percent
        if percent>=80:
            print "percent > 80%"
            print key,isEnglishstring(decriptedmessage),percent
            print decriptedmessage
        
        #if key==ekey:
        #    print "key match"
        #    print key,isEnglishstring(decriptedmessage),percent
        #    print decriptedmessage
        
if __name__=='__main__':
    main()