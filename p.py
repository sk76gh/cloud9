from bs4 import BeautifulSoup
import requests

url='http://eciresults.nic.in/'
r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for tr in soup.find_all('tr'):
    if tr.find_all('td')!=None:
        if tr.find_all('td')[0].text=='All India Anna Dravida Munnetra Kazhagam' :
            for td in tr.find_all('td'):
                print(td.text)
                
    