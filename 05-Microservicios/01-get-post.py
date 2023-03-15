import requests, pprint

# Endpoint del microservicio
url="http://api.open-notify.org/iss-now.json"

# Utilizamos la funcion get() para realizar una llamada GET
# La funcion ge( retorna una respuesta
response= requests.get(url)

# Mostrar el codigo de estado HTTP
print(f"Codigo de estado: ", response.status_code)
# Mostrar el codigo de estado HTTP en modo texto utilizando REASON
print(f"Estado: ", response.reason)
