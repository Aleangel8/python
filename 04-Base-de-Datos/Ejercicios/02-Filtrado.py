########################################################################################
#  Ejercicio de filtrado
########################################################################################
"""  
# Cuantos productos tenemos 
# Mostramos el numero de productos y un listado

# Filtrar los productos con UnitsInStock 0, utilizando filter()

# Valor del Stock= UntisInStock x UnitPrice
# Con un FOR y otra formula es realizarlo con MAP() SUM
# Con una funcion AGGREGATE de mongoDB y los operadores $sum y $multiply

# Con un identificador de pedido
# Listar dato---> ShipName, ShipAddress, ShipCity, ShipCountry, OrderDate, ShipDate
# Mostramos el detalle del pedido --> Producto, Cantidad, Precio Total, Total Pedido

# Alinea los caracteres para la presentacion
texto="Ejemplo"
print(f"{'Producto':30} {texto:>10}")

**************************
Preguntar a Borja:
Si se tiene q recorrer varias veces
es mejor ir extrallendo los datos par luego mostrarlos o recorrer dos veces, que es mas optimo


find_one()       Me da error

cursor = collection.find_one({'UnitsInStock': '0'})
while(cursor.alive):
    target=cursor.next()
    print(f"{target['ProductName']}")
**************************

"""


#########################################################################################



from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

# Definir la conexion y apuntar a Products
client= MongoClient("mongodb://127.0.0.1:27017")
db= client.Northwind
collection = db.Products

#Imprime la cantidad de Productos
print(f"\nTotal de productos: {collection.estimated_document_count():3}")


# Mostramos el numero de productos y un listado
print("\nListado de Productos:")
cursor = collection.find()
while(cursor.alive):
    target=cursor.next()
    print(f"{target['ProductID']}: {target['ProductName']}")
   

# Filtrar los productos con UnitsInStock 0,sin filter
print("\n(sin filter)Los Productos con 0 unidades en Stock son:")
cursor = collection.find({'UnitsInStock': '0'})
while(cursor.alive):
    target=cursor.next()
    print(f"{target['ProductName']}")

# Filtrar los productos con UnitsInStock 0 utilizando filter()


# Valor del Stock= UntisInStock x UnitPrice
print("\nValores de Stock:")
cursor = collection.find()
while(cursor.alive):
    target=cursor.next()
    print(f"Stock Value de {target['ProductName']:35}:{float(target['UnitsInStock'])*float(target['UnitPrice'])}€")

# Con un FOR y otra formula es realizarlo con MAP() SUM
# Con una funcion AGGREGATE de mongoDB y los operadores $sum y $multiply

# Con un identificador de pedido
# Listar dato---> ShipName, ShipAddress, ShipCity, ShipCountry, OrderDate, ShipDate
# Mostramos el detalle del pedido --> Producto, Cantidad, Precio Total, Total Pedido


