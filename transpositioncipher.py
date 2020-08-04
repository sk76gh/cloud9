def decript(key,cryptictext):
    dkey=len(cryptictext)//key
    if len(cryptictext)%key>0:
        dkey+=1
    
    #print dkey
    shadedrow=dkey*key - len(cryptictext)
    col=0
    row=0
    strarray=['' for x in range(dkey)]
    for text in cryptictext:
        
        strarray[col]+=text
        col+=1
        #print strarray, row, col
        if (col==dkey) or (col==dkey-1 and row>=key-shadedrow):
            col=0
            row+=1
            #print row, col
         
    decriptmessage=''.join(strarray)
    return decriptmessage

def encript(key,text):
    
    strarray=['' for x in range(key)]
    for textpos in range(len(text)):
        strarray[textpos % key]=strarray[textpos % key]+text[textpos]
        #print textpos, key, textpos % key, text[textpos % key],strarray[textpos % key]
    
    #print text
    encriptmessage=''.join(strarray)
    #print encriptmessage==''.join(strarray)
    return encriptmessage
    
#emessage=encript(8,'Common sense is not so common.')
#print emessage
#print decript(8,emessage)

myMessagetest = """Charles Babbage, FRS (26 December 1791 - 18 October 1871) was an English mathematician, 
philosopher, inventor and mechanical engineer who originated the concept of a programmable computer. 
Considered a "father of the computer", Babbage is credited with inventing the first mechanical computer
that eventually led to more complex designs. Parts of his uncompleted mechanisms are on display in the 
London Science Museum. In 1991, a perfectly functioning difference engine was constructed from Babbage's 
original plans. Built to tolerances achievable in the 19th century, the success of the finished engine 
indicated that Babbage's machine would have worked. Nine years later, the Science Museum completed the 
printer Babbage had designed for the difference engine."""
#emessage=encript(8,myMessagetest)
#print emessage
#print decript(8,emessage)

