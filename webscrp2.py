import requests
import bs4
import re

url = 'https://pythonprogramming.net/'

req = requests.get(url)
soup = bs4.BeautifulSoup(req.text, 'lxml')
#para = soup.findAll('p')
link = soup.findAll('a', href=True)
#print(link['href'])

# lst = []
# for i in link:
#     #print(i['href'])
#     #x = i['href']
#     #print(x)
#     lst.append(i['href'])
# #print(lst)

for a in soup.find_all('a', href=True):
    print("Found the URL:", a['href'])

regex = re.compile(r'^/')
pound_regex = re.compile(r'^#')
for a in soup.find_all('a', href=True):
    #print(i)
    if re.match(regex, a['href']):
        print('https://pythonprogramming.net' + a['href'])
    elif re.match(pound_regex, a['href']):
        pass
    else:
        print(a['href'])

