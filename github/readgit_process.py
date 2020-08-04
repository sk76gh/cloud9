import json
import io
import requests
from pprint import pprint

giturl='https://github.build.ge.com/raw/mygea/nfs-data/master/portal/mycfm_SAAppRoleMap.json'
req=requests.get(giturl)

if req.status_code==requests.codes.ok:
    print req.json()
