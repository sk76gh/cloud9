import requests
import json
from requests.auth import HTTPBasicAuth

url='http://cinlowesb1i.corporate.ge.com:8202/services/portal/org/orgdoicaocode/'




diagcodes=''
#mdmcodes=['DAL','KLM','ACA','VIR','LAN','YXX']
mdmcodes=['ZZXK',
'ZZWL',
'ZZWG',
'ZZWF']
#mdmcodes=['xyz']
counter=0
errcounter=0
for code in mdmcodes:
    counter+=1
    wurl=url+code
    r= requests.get(wurl)
    print counter,"/",len(mdmcodes)
    #print r.status_code
    if r.status_code==200:
        temp=json.dumps(r.json())
        docode=temp[2:len(temp)-2]
    else:
        docode='No DO code'
        errcounter+=1
        
    diagcodes=diagcodes+code+"="+docode+"\n"
    #print r.status_code,code
print errcounter," MDM codes out of ",counter," does not have a DO code"
#print diagcodes


fo=open("icaotomdm.csv","w")
fo.write(diagcodes)
fo.close