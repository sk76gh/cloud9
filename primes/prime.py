def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
    
def notinprimelist(newprime, prime):
    alreadyexistsflag=False
    for i in range(-1,-len(prime)):
        if newprime==prime[i]:
            alreadyexistsflag=True
            break
        else:
            alreadyexistsflag=False
    
    return not alreadyexistsflag
    
    
def addtoprimelist(newprime, prime):

    if notinprimelist(newprime,prime):
        prime.append(newprime)
        
            
def main():
    prime=[1,2,3,5,7]
    newprimelist=[]
    print(prime[-1])
    primeindex=-2
    while prime[-1]<100000:
        
        for i in range(-1,-len(prime),-1):
            newprimecandidate=prime[-1]+prime[i]-1
            if notinprimelist(newprimecandidate,prime):
                if isPrime(newprimecandidate):
                    newprimelist.append(newprimecandidate)
            else:
                break
        
 
        
        newprimelist.sort()
        print("new prime list ",newprimelist)
        prime.extend(newprimelist)
        #for i in range(len(newprimelist)):
        #    if isPrime(newprimelist[i]):
        #        print("latest prime found",newprimelist[i])
        #        addtoprimelist(newprimelist[i], prime)    
        
        newprimelist=[]
        #prime.sort()
                    
            
    print(prime)    




if __name__=='__main__':
    main()