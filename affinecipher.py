import cryptomath , sys


#SYMBOLES="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=|}{[]\":;'?><,./~`"
SYMBOLES =""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front
symlen=len(SYMBOLES)

def encriptaffinechiper(key,strmessage):
    cryptic=[]
    keya=key//symlen
    keyb=key%symlen
    
    if cryptomath.gcd(keya,symlen)!=1:
        sys.exit('choose another key')
        
    for letter in strmessage:
        crypticindex=(keyb+SYMBOLES.find(letter)*keya)%symlen
        cryptic.append(SYMBOLES[crypticindex])
        
        
    return ''.join(cryptic)
    
    
def decriptaffinechipher(key,strmessage):
    decrypted=[]
    
    keya=key//symlen
    keyb=key%symlen
    
    keya=key//symlen
    keyb=key%symlen
    
    if cryptomath.gcd(keya,symlen)!=1:
        sys.exit('choose another key')
    
    
    inversekey=cryptomath.findModInverse(keya,symlen)
        
    for letter in strmessage:
        decryptindex=(SYMBOLES.find(letter)-keyb)*inversekey%symlen
        decrypted.append(SYMBOLES[decryptindex])
        
        
    return ''.join(decrypted)



def main():
    message='A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing'
    key=2023
    keya=key//symlen
    keyb=key%symlen
    print keya, keyb, symlen
    if cryptomath.gcd(keya,symlen)!=1:
        sys.exit('choose another key')
        
    crypticmessage=encriptaffinechiper(key,message)
    print crypticmessage
    crypticmessage="""fX<*h>}(rTH<Rh()?<?T]TH=T<rh<tT<*_))T?<ISrT))I~TSr<Ii<Ir<*h()?<?T*TI=T<_<4(>_S<ISrh<tT)IT=IS~<r4_r<Ir<R_]<4(>_SEf<0X)_S<
k(HIS~"""
    decryptedmessage=decriptaffinechipher(key,crypticmessage)
    print decryptedmessage
    

if __name__=='__main__':
    main()