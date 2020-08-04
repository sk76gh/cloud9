import utils
import sys
import numpy as np
from itertools import product

sys.path.insert(0, '/home/ubuntu/workspace')
import detectEnglish, supportfunctions

def set1challenge3(encryptedstring):
    c=utils.charcodes()
    #print 'inside s1c3'
    string=c.getalphanumeric(encryptedstring)
    #string=encryptedstring
    for key in range(0,128): # only printable ascii characters
        hexkey=hex(key)[2:]
        if len(hexkey)<2:
            hexkey='0'+hexkey
        #print 'key = ',key,' hexkey = ', hexkey, 'decryted text = ', c.decript_hexstring_toascci(hexkey,string)
        decriptedstring=c.decript_hexstring_toascci_hexbytekey(hexkey,string)
        englishwordcount= detectEnglish.isEnglishstring(decriptedstring)[0]
        if englishwordcount>2:
            print encryptedstring
            print 'decimal key =',key,'ascii key = ',chr(key), 'hex key = ',hexkey, 'english word count = ', englishwordcount, 'decripted string = ',decriptedstring


def set1challenge4():
    with open('s1c4.txt','r') as crytotext:
        for hexline in crytotext:
            #print 'line = ',hexline
            set1challenge3(hexline)
    
def set1challenge5(plaintextstring):
    c=utils.charcodes()
    encryptedstring=c.encrypt_asciistring_tohexstring_wordkey('saravana',plaintextstring)
    print encryptedstring
    decriptedstring=c.decript_hexstring_toascci_hexwordkey(c.asciistring_2hexstring('saravana'),encryptedstring)
    print decriptedstring, decriptedstring==plaintextstring
    return 

def guesskeysize():
    c=utils.charcodes()
    keysizeguesslist=list()
    hexstr=''
    with open('guesskeysize.txt','r') as fd:
        for line in fd:
            hexstr=''
            #print 'processing... ' ,line
            asciistr=c.base64string_2binstring(line[:-1]) # remove the carriage return character at the line end
            hexstr+=c.binstring_2hexstring(asciistr)
            keysize=c.guesskeysize_frmencryptedhexstring(hexstr)
            print keysize
            keysizeguesslist.append(keysize)
        
        transposedlist=[list(i) for i in zip(*keysizeguesslist)]
        averagelist=list()
        for keylist in transposedlist:
            print np.average(keylist), np.var(keylist)
            averagelist.append(np.average(keylist))
        #print averagelist
        #print min(averagelist)
        #print "Key Size is probably",sum(keysizeguess)/len(keysizeguess), ' octals with variance',keysizevar
    return

def set1challenge6(filename):
    c=utils.charcodes()

    fullhexstring=''
    with open(filename,'r') as fd:
        for line in fd:
            asciistr=c.base64string_2binstring(line[:-1]) # remove the carriage return character at the line end
            
            #print 'processing...',line[:-1]
            hexstr=c.binstring_2hexstring(asciistr)
            #hexstr=line[:-1]
            #print hexstr,c.asciistring_2hexstring('sa')
            fullhexstring+=hexstr
    
    print len(fullhexstring)
    keysize=14
    keyblockfulllist=list()
    for blockindex in range(0,len(fullhexstring),keysize*2):
        keyblock= fullhexstring[blockindex:blockindex+keysize*2]
        #print keyblock
        keyblocklist=c.gethexlist_frm_hexstr(keyblock)
        
        keyblockfulllist.append(keyblocklist)
        #print keyblockfulllist

    transposedlist=[list(i) for i in zip(*keyblockfulllist)]
    print len(transposedlist)
    
    
    print 'Done.....'   
    
    return
def decryptSamlResponse(filename):
    c=utils.charcodes()
    with open(filename,'r') as fd:
        for line in fd:
            print c.hexstring_2base64string(line)
    return

def encryptfiletobase64(filename):
    c=utils.charcodes()
    with open(filename,'r') as fd:
        base64file=c.asciistring_2base64string(''.join(fd.read()))
        
    print base64file
    print c.base64string_2asciistring(base64file)   
            
            
    return

#set1challenge3('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736') 
#set1challenge4()
#set1challenge5("Bur")
#set1challenge5("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal")
#guesskeysize()
set1challenge6('guesskeysize.txt')
#decryptSamlResponse('modulus.txt')
#encryptfiletobase64('FinalServer.py')
