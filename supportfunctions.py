

alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols=alphabets+alphabets.lower()+' '

def getdict():
    dictionary=dict()
    with open('/home/ubuntu/workspace/dictionary.txt','r') as dic:
        for line in dic:
            dictionary[removesymbols(line)]=''
    return dictionary

def removesymbols(content):
    onlyletters=[]
    for letter in content:
        if letter in symbols:
            onlyletters.append(letter)
    return ''.join(onlyletters)
