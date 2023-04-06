import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/es/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

#print(trs[0].next_sibling)
#print(list(trs[0].children))

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price= price.a.string
    print(fixed_name, fixed_price, sep=": ")
    # Lo guardo todo en un dictionary
    prices[fixed_name]=fixed_price
    
    