import affinecipher,cryptomath

def main():
    
    message="A computer would deserve to be called intelligent"
    
    encriptdict=dict()
    
    for keya in range(2,affinecipher.symlen*2):
        key=keya*affinecipher.symlen+1
        
        if cryptomath.gcd(keya,affinecipher.symlen)==1:
            #print "gcd is one for key",key, keya
            encriptmessage=affinecipher.encriptaffinechiper(key,message)
            if encriptdict.has_key(encriptmessage):
                encriptdict[encriptmessage]+=1
            else:
                encriptdict[encriptmessage]=1
                
    for key in encriptdict:
        if encriptdict[key]>1:
            print key,encriptdict[key]
            
if __name__=="__main__":
    main()