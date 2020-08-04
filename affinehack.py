import affinecipher,detectEnglish,cryptomath,sys


    
def main():
    cryptictext="""U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG '<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""
    statlist=[]
    
    for key in range(1,affinecipher.symlen**2):
        keya=key//affinecipher.symlen

        if cryptomath.gcd(keya,affinecipher.symlen)!=1:
            continue
        
        decryptmessage=affinecipher.decriptaffinechipher(key,cryptictext)
        statlist=detectEnglish.isEnglishstring(affinecipher.decriptaffinechipher(key,cryptictext))
        #print key,statlist
        if float(statlist[0])/statlist[1]*100>60:
            print key, statlist, decryptmessage
            #sys.exit('50% match')

if __name__=='__main__':
    main()