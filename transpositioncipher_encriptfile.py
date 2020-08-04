import transpositioncipher
import os,sys

filename='icaotomdm.csv'
filenamesplit=filename.split('.')
outputfilename=filenamesplit[0]+'.encripted.'+filenamesplit[1]
print outputfilename

if not os.path.exists(filename):
    print filename,' does not exist, please verify'
    sys.exit()
    
with open(filename,'r') as encriptfile:
    content=encriptfile.read()
    
crypticmessage=transpositioncipher.encript(5,content)
print crypticmessage
print transpositioncipher.decript(5,crypticmessage)