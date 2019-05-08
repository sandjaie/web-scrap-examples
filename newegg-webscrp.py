import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

req = requests.get(url)
soup = bs(req.text, 'lxml')

containers = soup.find_all("div", class_="item-container")

#print(containers[0].find("div", class_="item-info"))

#item_title = containers[0].find('a', 'item-title').text
#br_container =  containers[0].find_all("div", class_="item-info")
#item_brand_name = br_container[0].div.a.img["title"]

#br_container.find('div', 'item-branding').find('a', 'item-brand').img["title"]
#print(item_brand_name)

filename = "products.csv"

f = open(filename, 'w')
headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:

    title_container = container.find_all('a', 'item-title')
    item_title = title_container[0].text

    br_container =  container.find_all('div', 'item-info')
    item_brand_name = br_container[0].div.a.img["title"]

    shipping_container = container.find_all('li', 'price-ship')
    item_shipping_price = shipping_container[0].text.strip()

    print("product_name: " + item_title)
    print("brand: " + item_brand_name)
    print("item_shipping_price :" + item_shipping_price)

    f.write(item_brand_name + ", " + item_title.replace(",", "|") + ", " + item_shipping_price + "\n")

f.close()




