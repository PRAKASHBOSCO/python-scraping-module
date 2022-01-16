#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 

option = input("Choose Options 1 = Amazon Panthary, 2 = Amazon.in, 3 = youtube : ")
URL = input("Enter Url : ")
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36'}
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)
# soup.encode("utf-8")
quotes=[]

if option == "1":

	content = soup.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'})

	for row in content: 
		quote = {} 
		quote['theme'] = row.h5.text 
		quote['url'] = row.a['href'] 
		quote['img'] = row.img['src'] 
		quote['lines'] = row.img['alt'].split(" #")[0] 
		quote['author'] = row.img['alt'].split(" #")[1] 
		quotes.append(quote) 


	filename = 'document/inspirational_quotes.csv'
	with open(filename, 'w', newline='') as f: 
		w = csv.DictWriter(f,['Category','Sub Category Level 1','Sub Category  Level 2','lines','author']) 
		w.writeheader() 
		for quote in quotes: 
			w.writerow(quote) 

if option == "2":
	# print("here")
	content = soup.findAll('div', attrs = {'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
	# print(content)
	# print('cc')
	for row in content:
		quote = {} 
		quote['name'] = row.h2.text.split("\n")[1]
		print(quote)
		# quote['price'] = row.span.text 
		# quote['price'] = row.a['href']
		# quote['img'] = row.img['src'] 
		# quote['lines'] = row.img['alt'].split(" #")[0] 
		# quote['author'] = row.img['alt'].split(" #")[1] 
		quotes.append(quote)
	# print(quotes)
	filename = 'document/search.csv'
	with open(filename, 'w', newline='') as f: 
		w = csv.DictWriter(f,['name']) 
		w.writeheader() 
		for quote in quotes:
			print(quote)
			w.writerow(quote)

if option == "3":
	songs = soup.findAll("div",{"class":"ytd-video-renderer"})
	print(songs)
	# song = songs[0].a['href']
	# songurl = song
	# msg = ("Here's a matching video \nhttps://www.youtube.com"+songurl)
	# print(msg)
