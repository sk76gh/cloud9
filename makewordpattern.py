import supportfunctions, pprint


def getpattern(word):
    word=word.upper()
    patterndict=dict()
    pattern=[]
    for index in range(len(word)):
        letter=word[index]
        if patterndict.has_key(letter):
            if len(pattern)>0:
                pattern.append('.')
            pattern.append(patterndict[letter])
        else:
            patterndict[letter]=str(index)
            if len(pattern)>0:
                pattern.append('.')
            pattern.append(str(index))
          
    return ''.join(pattern)
    

def main():
    allpatterns=dict()
    for word in supportfunctions.getdict():
        pattern=getpattern(word)
        if pattern not in allpatterns:
            allpatterns[pattern]=[word.upper()]
        else:
            allpatterns[pattern].append(word.upper())
    
    print allpatterns['0.1.2.3.1.5.6.7.8']
    
    with open('wordPatterns.py','w') as wp:
        wp.write('allPatterns = ')
        wp.write(pprint.pformat(allpatterns))
    
if __name__=='__main__':
    main()
