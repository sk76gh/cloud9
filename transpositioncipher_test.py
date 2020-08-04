import transpositioncipher
import random,sys


for i in range(10):
    alphabets='ABCDEFGHIJKLMOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz !@$%^&*()_+'*random.randint(1,5)
    message=list(alphabets)
    random.shuffle(message)
    #print ''.join(message)
    message=''.join(message)
    #print message
    encriptmessage=transpositioncipher.encript(8,message)
    #print encriptmessage
    decriptmessage=transpositioncipher.decript(8,encriptmessage)
    #print decriptmessage
    if message!=decriptmessage:
        print i,' failed :',decriptmessage
        sys.exit()

print "SUCCESS, all",i+1," test cases passed!!"   
    
    
    
