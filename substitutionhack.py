import makewordpattern,wordPatterns,pprint,random

#SYMBOLS=""" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+`1234567890-={}|[]\:";'<>?,./'"""
SYMBOLS=""" ABCDEFGHIJKLMNOPQRSTUVWXYZ"""

def getBlankCipherletterMapping():
    map=dict()
    for letter in SYMBOLS:
        map[letter]=set([])
    return map

def getallpatternwords(word):
    if wordPatterns.allPatterns.has_key(makewordpattern.getpattern(word)):
        return wordPatterns.allPatterns[makewordpattern.getpattern(word)]
    return []

def getCipherletterMapping(word):
    
    lettermapping=getBlankCipherletterMapping()
    
    for index in range(len(word)):
        mapset=set()
        for decriptword in getallpatternwords(word):
            print index,decriptword
            eachlettermap=lettermapping[word[index]]
            #print eachlettermap
            mapset.add(decriptword[index])
            #print "set:",mapset
            lettermapping[word[index]]=mapset
     
    return lettermapping    


def getmapintersection(mapa,mapb):
    
    for key in mapa:
        #print key,mapa[key],mapb[key],mapa[key]&mapb[key]
        intersect=mapa[key]&mapb[key]
        if len(intersect)==0:
            #print "nil intersection, so union"
            intersect=mapa[key]|mapb[key]
            #print key,mapa[key],mapb[key],mapa[key]|mapb[key]
        mapa[key]=intersect
    
    return mapa

def removeduplicates(mapa):
    for key1 in mapa:
        #print "length :----",mapa[key1], len(mapa[key1])
        if len(mapa[key1])==1:
            #print "inside length 1 :----",mapa[key1]
            for key2 in mapa:
                if len(mapa[key2])>1:
                    #print mapa[key1],mapa[key2],mapa[key2]-mapa[key1]
                    mapa[key2]=mapa[key2]-mapa[key1]
                    
    return mapa

def decryptWithCipherletterMapping(ciphertext, letterMapping):
    cipheredtext=[]
    for letter in ciphertext:
        letterinlist=list(letterMapping[letter])
        if len(letterinlist)==0:
            cipheredtext.append(' ')
        else:
            cipheredtext.append(letterinlist[0])
    
    print ''.join(cipheredtext)


def getkey_sc():
    key=dict()
    tempsymbols=list(SYMBOLS)
    print tempsymbols
    random.shuffle(tempsymbols)
    print tempsymbols
    for index in range(len(SYMBOLS)):
        key[SYMBOLS[index]]=tempsymbols[index]
    print key
    return key

def encriptmessage_sc(text):
    keymap=getkey_sc()
    encriptmessage=[]
    words=text.split()
    for word in words:
        for letter in word:
            encriptmessage.append(keymap[letter])
        encriptmessage.append(' ')
    return ''.join(encriptmessage)

def decriptmessage_sc(message):
    words=message.split()
    intersectedlettermapping=getBlankCipherletterMapping()
    #pprint.pprint(getCipherletterMapping('OLQIHXIRCKGNZ'))
    for word in words:
        print "mapping the word : ",word
        mapb=getCipherletterMapping(word)
        print "BEFORE intersection"
        #pprint.pprint(mapb)
        getmapintersection(intersectedlettermapping,mapb)
        #print "after intersection"
        #pprint.pprint(intersectedlettermapping)
    
    print"*******************************************"    
    removeduplicates(intersectedlettermapping)
    decryptWithCipherletterMapping(message,intersectedlettermapping)
    

def main():
    #message="OLQIHXIRCKGNZ  PLQRZKBZB  MPBKSSIPLC"
    message="Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm"
    decriptmessage_sc(message)

    
def main_tests():
    print getallpatternwords("HELLO")
    pprint.pprint(getCipherletterMapping("ORGANIZATION"))
    pprint.pprint(getmapintersection({"A":set(['a','b']),"B":set(['e','f'])},{"A":set(['a']),"B":set(['g'])}))
    pprint.pprint(removeduplicates({"A":set(['a','b']),"B":set(['a']),"C":set(['e','f']),"D":set(['f'])}))
  
def main_key():
    #getkey_sc()
    encripttext=encriptmessage_sc('CONGRATULATION BROOM BOMB')
    #print wordPatterns.allPatterns['0.1.2.3.4.5.6.7.5.5.6.11.1.2']
    print encripttext
    decriptmessage_sc(encripttext)
       
if __name__=="__main__":
    main()
    #main_tests()
    #main_key()