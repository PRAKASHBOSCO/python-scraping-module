#Python program to scrape website 
#and save quotes from website 
import requests 
import csv 
import json
import pandas as pd
import datetime

URL = "https://pflegefinder.bkk-dachverband.de/api/standard-search/count?keyword=&zip=&location=&maxDistance=0&type%5B%5D=nursing_service&type%5B%5D=nursing_home&order=%2Bdistance"
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36', 'Referer' : 'https://pflegefinder.bkk-dachverband.de/suche/searchresult.php?searchdata%5BmaxDistance%5D=0&searchdata%5Btype%5D%5B%5D=nursing_service&searchdata%5Btype%5D%5B%5D=nursing_home&searchdata%5Border%5D=%2Bdistance'}
r = requests.get(URL, headers=headers)
off = json.loads(r.content)
x = datetime.datetime.now()
filename = str(x.year)+'-'+str(x.month)+'-'+str(x.day)+'-emails.csv'
exception = False
try :
    df_old = pd.read_csv(filename)
except:
    exception = True
    
if exception == True:
    with open(filename, 'w', newline='') as f: 
        w = csv.DictWriter(f,['email'])
        w.writeheader()

offset = int(off['totalRecords'])

i = 20
quotes=[]
for i in range(offset):

    URL = "https://pflegefinder.bkk-dachverband.de/api/standard-search?maxDistance=0&type%5B%5D=nursing_service&type%5B%5D=nursing_home&order=%2Bdistance&offset={i}"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36', 'Referer' : 'https://pflegefinder.bkk-dachverband.de/suche/searchresult.php?searchdata%5BmaxDistance%5D=0&searchdata%5Btype%5D%5B%5D=nursing_service&searchdata%5Btype%5D%5B%5D=nursing_home&searchdata%5Border%5D=%2Bdistance'}
    r = requests.get(URL, headers=headers)

    data1 = json.loads(r.content)

    data = data1['data']
    j = 0 
    for row in data: 
        quote = [] 
        quote.append(row['email'])
        quotes.append(quote)
        j = j+1  
        
    i = i + 20  
    

    df_old = pd.read_csv(filename)
    newData = quotes
    # get column names of your existing data
    colNames = df_old.columns
    # make dataframe of new data that can be
    # easily appended to your old data
    df_new = pd.DataFrame(data=newData, columns=colNames)

    # concatenate old and new
    df_complete = pd.concat([df_old, df_new], axis = 0)

    # write your complete dataset to a new csv.
    df_complete.to_csv(filename, index=False)
            
    
  



	


