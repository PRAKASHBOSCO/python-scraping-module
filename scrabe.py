#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 

#option = input("Choose Options 1 = Amazon Panthary, 2 = Amazon.in, 3 = youtube : ")
URL = "https://www.tractordata.com/farm-tractors/index.html"
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36'}
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

def getData(url):
    	URL = url
	headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36'}
	r = requests.get(URL, headers=headers)
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup

# print(soup)
# soup.encode("utf-8")
quotes=[]

if soup != "":

	content = soup.findAll('table', attrs = {'class':'tdMenu1'})
	content = soup.findAll('tr')
	i = 0
	f = {}
	for row in content: 
		f[i] = {}
		secondData = getData(row.a['href'])
		content2 = secondData.findAll('table', attrs = {'class':'tdMenu1'})
		content2 = secondData.findAll('tr')
		firstUrl = row.a['href']
		name = row.a.text
		e = {}
		j = 0
    		for row in content2: 
				e[j] = {}
				content3 = soup.findAll('table', attrs = {'class':'tdMenu1'})
				content3 = soup.findAll('tr')
				# e[j]['url'] = row.a['href']
				# e[j]['name'] = row.a.text
				# e[j]['power']
	
				j += 1

		# f[i]['url'] = row.a['href']
		# f[i]['name'] = row.a.text
		i += 1


	
	filename = 'document/inspirational_quotes.csv'
	# with open(filename, 'w', newline='') as f: 
	# 	# w = csv.DictWriter(f,['Make','Model','Power','Years','Type', 'Engine']) 
	# 	w = csv.DictWriter(f,['url','name']) 
	# 	w.writeheader() 
	for i in range(len(f)): 
			print(f[i])

				# for w in q:
				# 	w.writerow(q)



	


