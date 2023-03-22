########################################################################################
#  Ejercicio 5
########################################################################################
"""  Consulta de plazaslibres de parquing EMT

freeParking: null no los quiero
freeParking: 131 por ejemplo 
Utilizamos filter() para crear una lista con los parking q tienen espacio libre

Utilizamos sum() y map() par calcular el total de plazas libres



"""
#########################################################################################
import requests

# 1ro la url apuntando a la pagina
url= "https://openapi.emtmadrid.es/v1/citymad/places/parkings/availability"

# 2do pasas parametro por las cabeceras
headers={"accessToken": "f5f9990e-c6f3-11ed-a34b-02dc46d0efe2"}

try:
# 3ro Hago request get pasando la url y la cabecera y la guardo en una variable
    response = requests.get(url, headers=headers)
# 4to pregunto si es ok pero es para mi mas q nada
    if (response.status_code == 200):
# 5to lo guardo en json pra acceder bien a el
        data = response.json()
# 6 Uso los datos q quiera

        #filtras en data['data'] los ['freeParking'] distintos de None y los enlista
        filter_data= filter(lambda x:x['freeParking'] is not None, data['data'])  
        # se mapea la lista y se suman los 
        free_parking = sum(map(lambda x:x['freeParking'],filter_data))              
        print(free_parking)
        #Prueba de acceso dentro de data
        print(data['data'][0]['name'])
    else:
        print(f"Error:", response.reason)

except Exception as err:
    print(f"Error: {err}")

#############  Plantilla