import requests, pprint

# Endpoint del microservicio
url="http://api.open-notify.org/iss-now.json"

# Utilizamos la funcion get() para realizar una llamada GET
# La funcion get retorna una respuesta
response= requests.get(url)

# Mostrar el codigo de estado HTTP (200)
print(f"\nCodigo de estado: ", response.status_code)
# Mostrar el codigo de estado HTTP en modo texto utilizando REASON (OK)
print(f"\nEstado: ", response.reason)

if(response.status_code == 200):
    print("\nCabeceras: ", response.headers)
    print("\nContent-Type:", response.headers['Content-Type'])
    print(f"\nContent-Length: {response.headers['Content-Length']} bytes")
    print("\nContenido: ", response.text)


    if(response.headers["Content-Type"]=="application/json"):
        data = response.json()
        print(f"\nMensaje: {data['message']}")
        print(f"Fecha: {data['timestamp']}")
        print(f"Longitud: {data['iss_position']['longitude']}")
        print(f"Longitud: {data['iss_position']['latitude']}")
    else:
        print("No se pueden procesar los datos.")

else:
    print(f"Error:", response.reason)


#####################################################

url = "https://postman-echo.com/post"

myHeaders = {"content-type": "application/json", "api-key": "jKHduyad5askfj8d$m8s"}

# Enviar datos en la URL
url = "https://dominio.com/api/customers/100/orders"

# Enviar datos como parametros incluidos en la url
url = "https://dominio.com/api/customers?id=100&process=orders"

#Enviar datos como cabecera
url = "https://dominio.com/api/customers"
myHeaders = {
    "content-type": "application/json",
    "api-key": "jKHduyad5askfj8d$m8s",
    "id": 100,
    "process" : "orders"}


# Enviar datos en el cuerpo del mensaje
url = "https://dominio.com/api/customers"
mydata = {
    "id": 100,
    "process": "orders"
}

url = "https://postman-echo.com/post"
myHeaders = {"content-type": "application/json", "api-key": "jKHduyad5askfj8d$m8s"}
myParams = {"id": 100, "process": "orders"}
mydata = {"id": 100,"process": "orders"}

#response = requests.post(url, params=myParams, headers=myHeaders, data=mydata)
reponse= requests.request(
    "POST", url, params=myParams, headers=myHeaders, data=mydata)

print(f"\nCodigo de estado: ", response.status_code)
print(f"\nEstado: ", response.reason)
print("\nCabeceras: ", response.headers)
print("\nContenido: ", response.text)
