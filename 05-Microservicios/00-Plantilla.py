"""
#############  Plantilla

# 1ro la url apuntando a la pagina
url= "https://api.apilayer.com/exchangerates_data/convert"

# 2do pasas parametro por las cabeceras
headers={"to": "USD","from": "EUR", "amount":num, "apikey": "WqVzJ6pWHbPkkil5ya8tzBYyBM2fKj1z"}

try:
# 3ro Hago request get pasando la url y la cabecera y la guardo en una variable
    response = requests.get(url, headers)
# 4to pregunto si es ok pero es para mi mas q nada
    if (response.status_code == 200):
# 5to lo guardo en json pra acceder bien a el
        data = response.json()
# 6 Uso los datos q quiera
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

"""




