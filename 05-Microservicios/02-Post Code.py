import requests, pprint

# api.zippopotam.us/country/postal-code
codigo = input("Codigo Postal: ")
url = "http://api.zippopotam.us/es/"+codigo
#url = f"http://api.zippopotam.us/es/{codigo}"


# Utilizamos la funcion get() para realizar una llamada GET
# La funcion ge( retorna una respuesta
response= requests.get(url)

# Mostrar el codigo de estado HTTP
print(f"\nCodigo de estado: ", response.status_code)
# Mostrar el codigo de estado HTTP en modo texto utilizando REASON
print(f"\nEstado: ", response.reason)


if(response.status_code == 200):
    print("\nContenido: ", response.text)
    if(response.headers["Content-Type"]=="application/json"):
        data = response.json()
        print(f"\nCodigo Postal: {data['post code']}")
        print(f"\nPais: {data['country']}")
        for i in data["places"]:
            print(i['place name'], i['state'])
        
        # Acceder sin for directamente data['places'] es una lista con un unico elemento q es un diccionario
        print(type(data["places"]))    
        print(data['places'][0]['latitude'])   
        
        
        
    else:
        print("No se pueden procesar los datos.")

else:
    print(f"Error:", response.reason)










