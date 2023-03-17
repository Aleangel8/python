import requests, pprint


url= f"https://api.apilayer.com/exchangerates_data/convert"

#num=input("Introduzca cantidad")


#?to=USD&from=EUR
#############  Plantilla
headers={"to": "USD","from": "EUR", "amount":"90", "apikey": "WqVzJ6pWHbPkkil5ya8tzBYyBM2fKj1z"}


try:
    response = requests.get(url, headers=headers)
    if(response.status_code == 200):
        data = response.json()
        print(data)
        #Enviar datos como cabecera
        

    else:
        print(f"Error:", response.reason)

except Exception as err:
    print(f"Error: {err}")

#############  Plantilla








exit()
url = f"https://api.apilayer.com/exchangerates_data/symbols"


#############  Plantilla
headers = {"apikey": "WqVzJ6pWHbPkkil5ya8tzBYyBM2fKj1z"}

try:
    response = requests.get(url, headers=headers)
    if (response.status_code == 200):
        data = response.json()
        print(data)
        #Enviar datos como cabecera
        

    else:
        print(f"Error:", response.reason)

except Exception as err:
    print(f"Error: {err}")

#############  Plantilla






