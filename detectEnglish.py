import urllib
import ssl,requests,supportfunctions





dictionary=supportfunctions.getdict()

def isEnglishfile(filename):
    
    count=0
    wordcount=0
    linecount=0
    
    
    with open(filename,'r') as messagefile:
        for line in messagefile:
            wordlist=line.split()
            for word in wordlist:
                if dictionary.has_key(word):
                    count+=1
                wordcount+=1
            linecount+=1
    return [count,wordcount,linecount]


def isEnglishstring(content):
    
    
    
    count=0
    wordcount=0
    linecount=0
    
    
    textmessage=supportfunctions.removesymbols(content)
    #print textmessage
    
    #print dictionary
    for line in textmessage.split():
        wordlist=line.split()
        #print wordlist
        for word in wordlist:
            #print word.upper()
            if dictionary.has_key(word.upper()):
                #print word
                count+=1
            wordcount+=1
        linecount+=1
    
    return [count,wordcount,linecount]
    
def main():
    
    #filename='storysidhartha.txt'
    #print isEnglishfile(filename)
    
    myMessage = """Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English mathematician, 
philosopher, inventor and mechanical engineer who originated the concept of a programmable computer. 
Considered a "father of the computer", Babbage is credited with inventing the first mechanical computer
that eventually led to more complex designs. Parts of his uncompleted mechanisms are on display in the 
London Science Museum. In 1991, a perfectly functioning difference engine was constructed from Babbage's 
original plans. Built to tolerances achievable in the 19th century, the success of the finished engine 
indicated that Babbage's machine would have worked. Nine years later, the Science Museum completed the 
printer Babbage had designed for the difference engine."""
    print isEnglishstring(myMessage)
    
    #url=urllib.urlopen('https://inventwithpython.com/siddhartha.txt')            
    #url=requests.get('https://inventwithpython.com/siddhartha.txt',verify=False)
    #content=url.read()
    #print isEnglishstring(content)

if __name__ == '__main__':
    main()