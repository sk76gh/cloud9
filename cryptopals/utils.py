import numpy as np

class charcodes:
    ascii_len=8
    base64_len=6
    hex_len=4
    hex_codelen=2
    ascii_code2char={i:chr(i)  for i in range(256) }
    ascii_char2code={chr(i):i for i in range(256)}
    base64_code2char={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:'a',27:'b',28:'c',29:'d',30:'e',31:'f',32:'g',33:'h',34:'i',35:'j',36:'k',37:'l',38:'m',39:'n',40:'o',41:'p',42:'q',43:'r',44:'s',45:'t',46:'u',47:'v',48:'w',49:'x',50:'y',51:'z',52:'0',53:'1',54:'2',55:'3',56:'4',57:'5',58:'6',59:'7',60:'8',61:'9',62:'+',63:'/'}
    base64_char2code=dict()

    def __init__(self):
        self.base64_char2code={ self.base64_code2char[i]:i for i in range(64)}
        
    def charmap(self):
        print self.ascii_code2char
        print self.ascii_char2code
        print self.base64_code2char
        
    def codeto8bit(self,code):
        return (self.ascii_len-len(bin(code)[2:]))*'0'+bin(code)[2:]
        
    def codeto6bit(self,code):
        return (self.base64_len-len(bin(code)[2:]))*'0'+bin(code)[2:]

    def codeto4bit(self,code):
        return (self.hex_len-len(bin(code)[2:]))*'0'+bin(code)[2:]

    def charto8bitascii(self,char):
        code=self.ascii_char2code[char]
        return self.codeto8bit(code)
    
    def hexchar_2code(self,hexchar):
        return int(hexchar,base=16)
        
    def hexcharto8bit(self,hexchar):
        code=self.hexchar_2code(hexchar)
        return self.codeto8bit(code)
        
 
    #this method does not make sense; no test scripts written
    def charto6bitascii(self,char):
        code=self.ascii_char2code[char]
        return self.codeto6bit(code)
    
    def charto8bitbase64(self,char):
        code=self.base64_char2code[char]
        return self.codeto8bit(code)
        
    def charto6bitbase64(self,char):
        code=self.base64_char2code[char]
        return self.codeto6bit(code)
     
    def hexstring_2binstring(self, string):
        binary_string=''
        if len(string)%2==0:
            for charindex in range(0,len(string),2):
                binary_string+=self.hexcharto8bit(string[charindex:charindex+self.hex_codelen])
        elif len(string)%2==1:
            for c in string:
                binary_string+=self.hexcharto8bit(c)
        
        return binary_string
    
            
    def base64string_2binstring(self, string):
        binary_string=''
        for c in string:
            if c=='=':
                binary_string+='0'*self.base64_len
            else:
                binary_string+=self.charto6bitbase64(c)
        return binary_string
        
    def asciistring_2binstring(self, string):
        binary_string=''
        for c in string:
            binary_string+=self.charto8bitascii(c)
        return binary_string
        
    
    def binstring_2asciistring(self,binary_string):
        asciistring=''
        bytes=[binary_string[i:i+self.ascii_len] for i in range(0,len(binary_string),self.ascii_len)]
        #print bytes
        
        for byte in bytes:
            if len(byte)==self.ascii_len and byte!='00000000':
                asciicode=int(byte,base=2)
                char=self.ascii_code2char[asciicode]
                asciistring+=char
            elif len(byte)<self.ascii_len:
                print 'dont know about binary byte:'+ byte
        return asciistring

    def binstring_2base64string(self,binary_string):
        base64string=''
        bytes=[binary_string[i:i+self.base64_len] for i in range(0,len(binary_string),self.base64_len)]
        #print bytes
        
        for byte in bytes:
            if len(byte)==self.base64_len:
                base64code=int(byte,base=2)
                char=self.base64_code2char[base64code]
                base64string+=char
            elif len(byte)<self.base64_len:
                if len(byte)==2:
                    byte+='0000'
                    base64code=int(byte,base=2)
                    char=self.base64_code2char[base64code]
                    base64string+=char
                    base64string+='=='
                if len(byte)==4:
                    byte+='00'
                    base64code=int(byte,base=2)
                    char=self.base64_code2char[base64code]
                    base64string+=char
                    base64string+='='
                
        return base64string
    
    
    def binstring_2hexstring(self, binary_string):
        hexstring=''
        bytes=[binary_string[i:i+self.ascii_len] for i in range(0,len(binary_string),self.ascii_len)]
        
        for byte in bytes:
            base10=int(byte,base=2)
            base16=hex(base10)[2:]
            hexstring+=base16
        
        return hexstring
        
    
    def base64string_2asciistring(self,base64string):
        return self.binstring_2asciistring(self.base64string_2binstring(base64string))
        
    def asciistring_2base64string(self,asciistring):
        return self.binstring_2base64string(self.asciistring_2binstring(asciistring))
        
    def asciistring_2hexstring(self,asciistring):
        return self.binstring_2hexstring(self.asciistring_2binstring(asciistring))
        
    def hexstring_2base64string(self, hexstring):
        return self.binstring_2base64string(self.hexstring_2binstring(hexstring))
        
    def hexstring_2asciistring(self,hexstring):
        return self.binstring_2asciistring(self.hexstring_2binstring(hexstring))
        
# print hextobase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

    def xor(self, hex1,hex2):
        xoredstring=''
        if len(hex1)==len(hex2):
            base10_num1=int(hex1,base=16)
            base10_num2=int(hex2,base=16)
            xoredstring=hex(base10_num1^base10_num2)[2:]

            if xoredstring[-1]=='L':
                xoredstring=xoredstring[:-1]
        else:
            return 'hex strings not same length'
        return xoredstring

    def getbyte_frm_hexstring(self,string):
        for c in range(0,len(string),2):
            yield string[c:c+2]
           
    def getkeysizebytes_frm_hexstring(self, key,string):
        for c in range(0,len(string),len(key)):
            #print c, string[c:c+len(key)]
            yield string[c:c+len(key)]

    def getpadded_hexstring(self, hexkey, hexstring):
        #print len(hexkey)-len(hexstring)%len(hexkey)
        hexstring+='0'*(len(hexkey)-len(hexstring)%len(hexkey))
        return hexstring
    
    def pad_hexbyte(self, hexbyte):
        if len(hexbyte)%2==1:
            return '0'+hexbyte
        return hexbyte
        
    def decript_hexstring_toascci_hexbytekey(self,hexkey,hexstring):
        ascii_string=[]
        #hexstring=self.getpadded_hexstring(hexkey,hexstring)
        #print c.hexstring_2binstring(string)
        for hexbyte in self.getbyte_frm_hexstring(hexstring):
            #print 'hexkey ',hexkey,' hex byte ',hexbyte
            xoredbyte=self.xor(hexkey,hexbyte)
            xoreddecimal=int(xoredbyte,base=16)
            if xoreddecimal>31 and xoreddecimal<127: # decipher only ascii printable characters
                asciichar=self.hexstring_2asciistring(xoredbyte)
                ascii_string.append(asciichar)
            else:
                ascii_string.append('.')
            #print hexbyte, hexkey, self.xor(hexkey,hexbyte), asciichar
            
        return ''.join(ascii_string)
        
    def decript_hexstring_toascci_hexwordkey(self,hexwordkey,hexstring):
        ascii_string=[]
        hexstring=self.getpadded_hexstring(hexwordkey,hexstring)
        #print c.hexstring_2binstring(string)
        for hexbyte in self.getkeysizebytes_frm_hexstring(hexwordkey,hexstring):
            #print 'hexkey ',hexwordkey,' hex byte ',hexbyte
            xoredbyte=self.xor(hexwordkey,hexbyte)
            
            asciichar=self.hexstring_2asciistring(xoredbyte)
            ascii_string.append(asciichar)
            #print hexbyte, hexwordkey, self.xor(hexwordkey,hexbyte), asciichar
            
        return ''.join(ascii_string)  
        
        
    def encrypt_asciistring_tohexstring_wordkey(self, asciiwordkey, asciistring):
        hex_string=[]
        
        hexkey=self.asciistring_2hexstring(asciiwordkey)
        hexstring=self.asciistring_2hexstring(asciistring)
        #pad hexstring with trailing 000...s
        hexstring=self.getpadded_hexstring(hexkey, hexstring)
        for hexbyte in self.getkeysizebytes_frm_hexstring(hexkey,hexstring):    
            #print hexkey, hexbyte
            xoredbyte=self.xor(hexkey,hexbyte)
            #print hexkey, hexbyte,xoredbyte
            hex_string.append(self.pad_hexbyte(xoredbyte))
            #print hex_string

                
        return ''.join(hex_string)
       
    def geteditdistance_frmhexstring(self, hexstr1,hexstr2):
        editdistance=0
        if len(hexstr1)==len(hexstr2):
            xoredstring=self.xor(hexstr1,hexstr2)
            #print hexstr1, hexstr2,xoredstring
            for c in self.hexstring_2binstring(xoredstring):
                if c=='1':
                    editdistance+=1
        return editdistance
            
    def geteditdistance_frmasciistring(self, asciistr1,asciistr2):
      
        hexstr1=self.asciistring_2hexstring(asciistr1)
        hexstr2=self.asciistring_2hexstring(asciistr2)
        #print hexstr1, hexstr2
        editdistance= self.geteditdistance_frmhexstring(hexstr1,hexstr2)
        return editdistance
    
    def guesskeysize_frmencryptedhexstring(self,hexstring):
        editdistance=list()
        #asciistr=self.hexstring_2asciistring(hexstring)
        #print hexstring
        for blocksize in range(2,len(hexstring)/2,2):
            string1=hexstring[0:blocksize]
            string2=hexstring[blocksize:2*blocksize]
            #print blocksize, '##',string1, '##',string2, len(string2)
            editdistance.append(self.geteditdistance_frmhexstring(string1,string2)/blocksize)
            #print string1, string2
        #print editdistance
        return editdistance
    
    def gethexkeytokens(self,keysize):
        
        hexcodes=[hex(i) for i in range(16)]
        print hexcodes
        return
    
    def getalphanumeric(self, string):
        return ''.join(e for e in string if e.isalnum())
        
    def gethexstringblock(self,charjumpsize,hexstring):
        blockstring=''
        for c in range(0,len(hexstring),2*charjumpsize):
            blockstring+=hexstring[c:c+2]
        return blockstring
        
    def gethexlist_frm_hexstr(self, hexstring):
        hexlist=list()
        hexlist=[hexstring[index:index+self.hex_codelen] for index in range(0,len(hexstring),2)]
        return hexlist
    
    def get_etaoin_shrdlu(self,asciistr):
        lowerasciistr=asciistr.lower()
        strfrqlist=list()
        etaoinfrq=[12.70,9.05,8.16,7.50,6.96,6.75]
        for char in 'etaoin':
            strfrqlist.append(lowerasciistr.count(char))

        #print strfrqlist
        normlist=[i*100/sum(strfrqlist) for i in strfrqlist]
        #print normlist
        scaledbyfrqlist=list()
        for index in range(len(normlist)):
            scaledbyfrqlist.append(normlist[index]/etaoinfrq[index])
        
        #print scaledbyfrqlist
        
        return sum(scaledbyfrqlist)/len(etaoinfrq)
    
    
def hextobase64(s=''):
    return s.decode("hex").encode('base64')
    
def main():
    c=charcodes()
    #c.charmap()
    
    print 'test codeto8bit : ' , c.codeto8bit(65)=='01000001'
    print 'test codeto6bit : ' , c.codeto6bit(1)=='000001'
    print 'test charto8bit_ascii : ' , c.charto8bitascii('A')=='01000001'
    print 'test charto8bit_ascii : ' , c.charto8bitascii('B')=='01000010'
    print 'test charto8bit_base64 : ' , c.charto8bitbase64('A')=='00000000'
    print 'test charto8bit_base64 : ' , c.charto8bitbase64('B')=='00000001'
    print 'test charto6bit_base64 : ' , c.charto6bitbase64('A')=='000000'
    print 'test charto6bit_base64 : ' , c.charto6bitbase64('B')=='000001'
    print 'test ascii_binstring : ' , c.asciistring_2binstring('abideidlxADC')=='011000010110001001101001011001000110010101101001011001000110110001111000010000010100010001000011'
    print 'test base64_binstring : ' , c.base64string_2binstring('abideidlxADC')=='011010011011100010011101011110100010011101100101110001000000000011000010'
    #print 'test base64_binstring : ' , c.base64string_2binstring('Jk8DCkkcC3hFMQIEC0EbAVIqCFZBO1IdBgZUVA4QTgUWSR4QJwwRTWM=')
    print 'test binstring_2asciistring : ' , c.binstring_2asciistring(c.asciistring_2binstring('abideidlxADC'))=='abideidlxADC'
    print 'test binstring_2base64string : ' , c.binstring_2base64string(c.base64string_2binstring('abideidlxADC'))=='abideidlxADC'
    print 'test ascii to base64 : ', c.binstring_2base64string(c.asciistring_2binstring('A'))=='QQ=='
    print 'test ascii to base64 : ', c.binstring_2base64string(c.asciistring_2binstring('M'))=='TQ=='
    print 'test ascii to base64 : ', c.binstring_2base64string(c.asciistring_2binstring('Man'))=='TWFu'
    print 'test ascii to base64 : ', c.binstring_2base64string(c.asciistring_2binstring('Ma'))=='TWE='
    print 'test ascii to base64 : ', c.binstring_2base64string(c.asciistring_2binstring('leasure.'))=='bGVhc3VyZS4='
    print 'test base64 to ascii : ',c.binstring_2asciistring(c.base64string_2binstring('bGVhc3VyZS4='))=='leasure.'
    print 'test base64 to ascii : ',c.binstring_2asciistring(c.base64string_2binstring('YW55IGNhcm5hbCBwbGVhc3U='))=='any carnal pleasu'
    print 'test base64 to ascii : ',c.binstring_2asciistring(c.base64string_2binstring('YW55IGNhcm5hbCBwbGVhc3Vy'))=='any carnal pleasur'
    print 'test base64 to ascii : ',c.binstring_2asciistring(c.base64string_2binstring('YW55IGNhcm5hbCBwbGVhcw=='))=='any carnal pleas'
    print 'test ascii to base64 : ', c.asciistring_2base64string('Ma')=='TWE='
    print 'test ascii to base64 : ', c.asciistring_2base64string('any carnal pleas')=='YW55IGNhcm5hbCBwbGVhcw=='
    print 'test ascii to base64 : ', c.asciistring_2base64string('any carnal pleasu')=='YW55IGNhcm5hbCBwbGVhc3U='
    print 'test ascii to base64 : ', c.asciistring_2base64string('any carnal pleasur')=='YW55IGNhcm5hbCBwbGVhc3Vy'
    print 'test base64 to ascii : ',c.base64string_2asciistring('YW55IGNhcm5hbCBwbGVhc3Vy')=='any carnal pleasur'
    print 'test base64 to ascii : ',c.base64string_2asciistring('YW55IGNhcm5hbCBwbGVhcw==')=='any carnal pleas'
    print 'test base64 to ascii : ',c.base64string_2asciistring('YW55IGNhcm5hbCBwbGVhc3U=')=='any carnal pleasu'  
    #print 'test base64 to ascii : ' , c.base64string_2asciistring('Jk8DCkkcC3hFMQIEC0EbAVIqCFZBO1IdBgZUVA4QTgUWSR4QJwwRTWM=')
    #print 'test base64 to ascii : ' , c.base64string_2asciistring('FlRlIkw5QwA2GggaR0YBBg5ZTgIcAAw3SVIaAQcVEU8QTyEaYy0fDE4ITlhI')
    
    print 'test hex to binary : ', c.hexstring_2binstring('A')=='00001010'
    print 'test hex to base64 : ', c.binstring_2base64string(c.hexstring_2binstring('A'))=='Cg=='
    print 'test hex to base64 : ', c.binstring_2base64string(c.hexstring_2binstring('33206c617a7920646f67732e'))=='MyBsYXp5IGRvZ3Mu'
    print 'test hex to base64 : ', c.binstring_2base64string(c.hexstring_2binstring('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))=='SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    print 'test hex to base64 : ', c.binstring_2base64string(c.hexstring_2binstring('65E5672C8A9E'))=='ZeVnLIqe'
    print 'test hex to base64 : ', c.binstring_2base64string(c.hexstring_2binstring('004122620391002E'))=='AEEiYgORAC4='
    
    print 'test bin to hex : ',c.binstring_2hexstring('00001010')=='a'
    print 'text ascii to hex : ', c.asciistring_2hexstring('The quick brown fox jumps over 13 lazy dogs.')=='54686520717569636b2062726f776e20666f78206a756d7073206f766572203133206c617a7920646f67732e'
    
    print 'test xor of hex string : ',c.xor('a','b')=='1'
    print 'test xor of hex string : ',c.xor('42','49')=='b'
    print 'test xor of hex string : ',c.xor(hex(ord('B')),hex(ord('I')))=='b'
    print 'test xor of hex string : ',c.xor('ab','bc')=='17'
    print 'test xor of hex string : ',c.xor('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')=='746865206b696420646f6e277420706c6179'
    print 'test hex to ascii string : ', c.hexstring_2asciistring('7361726176616e61')=='saravana'
    print 'test decript_hexstring_toascci_hexbytekey : ',c.decript_hexstring_toascci_hexbytekey('58','1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')=="Cooking MC's like a pound of bacon"
    
    print 'test pad hex byte : ',c.pad_hexbyte('b')=='0b'
    print 'test editdistance : ',c.geteditdistance_frmhexstring('1','2')==2
    print 'test editdistance : ',c.geteditdistance_frmasciistring('this is a test','wokka wokka!!!')==37
    for e in c.getkeysizebytes_frm_hexstring('4914','0b3c3b456fefe'):
        print 'test keysizebytes for :%s'%e, len(e)==len('4914')

    print 'test guess key size (size = 1, asciiKey = X) : ',c.guesskeysize_frmencryptedhexstring('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print 'test guess key size (size = 1 asciiKey = 5): ',c.guesskeysize_frmencryptedhexstring('7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f')
    print 'test guess key size (size = 3 asciiKey = ICE): ',c.guesskeysize_frmencryptedhexstring('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
    #print 'test guess key size : ' ,c.guesskeysize_frmencryptedhexstring(c.asciistring_2hexstring(c.base64string_2asciistring('HUIfTQsPAh9PE048GmllH0kcDk4TAQsHThsBFkU2AB4BSWQgVB0dQzNTTmVS')))==2
    print 'test base64 to ascii : ',c.asciistring_2hexstring(c.base64string_2asciistring('HQdJEwATARNFTg5JFwQ5C15NHQYEGk94dzBDADsdHE4UVBUaDE5JTwgHRTkA'))
    print 'test guess key size : ' ,c.guesskeysize_frmencryptedhexstring('1d7491313113454ee4917439b5e4d1d641a4f787730433b1d1c4e1454151ac4e494f874539')
    print 'test hex string block : ',c.gethexstringblock(3,'1d7491313113454')
    #print 'test hex key tokens : ', c.gethexkeytokens(0)
    print 'test hexlist from hex string',c.gethexlist_frm_hexstr('1d421f4dbf21f4f134e3c1a69651')==list(['1d', '42', '1f', '4d', 'bf', '21', 'f4', 'f1', '34', 'e3', 'c1', 'a6', '96', '51'])
    print 'test etaoin_shrdlu',c.get_etaoin_shrdlu('idiosyncratic letter frequency if the essay is about the frequent use of x-rays to treat zebras in Qatar')
    print 'test etaoin_shrdlu',c.get_etaoin_shrdlu("India, officially the Republic of India (Bharat Ga?arajya),[e] is a country in South Asia. It is the seventh-largest country by area, the second-most populous country (with over 1.2 billion people), and the most populous democracy in the world. It is bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast. It shares land borders with Pakistan to the west;[f] China, Nepal, and Bhutan to the northeast; and Myanmar (Burma) and Bangladesh to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives. India's Andaman and Nicobar Islands share a maritime border with Thailand and Indonesia.")

if __name__ == '__main__':
    main()