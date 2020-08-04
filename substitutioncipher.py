import random


SYMBOLS=""" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+`1234567890-={}|[]\:";'<>?,./'"""
symlen=len(SYMBOLS)

def encript_sc(key, text):
    encriptedtext=[]
    for letter in text:
        encriptedtext.append(key[SYMBOLS.find(letter)])
        
    return ''.join(encriptedtext)    
        
def decript_sc(key,text):
    return None
    
def getkey():
    listsymbols=list(SYMBOLS)
    random.shuffle(listsymbols)    
    return ''.join(listsymbols)
    
def checkkey(key):
    return list(key).sort()==list(SYMBOLS).sort()
    
def main():
    key=getkey()
    if checkkey(key):
        print "key is good"
    else:
        print "key check failed"
        
    message='how are you doing, XXXX RRRR'
    print message,encript_sc(key,message)
    
if __name__=='__main__':
    main()
