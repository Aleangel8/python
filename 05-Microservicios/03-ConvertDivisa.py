import requests, pprint


url= "https://api.apilayer.com/exchangerates_data/convert" #?to=USD&from=EUR

num=input("Introduzca cantidad: ")



#############  Plantilla
headers={"to": "USD","from": "EUR", "amount":num, "apikey": "WqVzJ6pWHbPkkil5ya8tzBYyBM2fKj1z"}


try:
    response = requests.get(url,headers)
    if(response.status_code == 200):
        data = response.json()
        print(data)
        print(data['success'])
        print(data['query'])
        print(data['query']['from'])
        print(data['date'])
        print(data['result'])
        

    else:
        print(f"Error:", response.reason)

except Exception as err:
    print(f"Error: {err}")

#############  Plantilla









