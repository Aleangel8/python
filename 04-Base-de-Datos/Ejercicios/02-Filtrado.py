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

print(collection.find_one({'UnitsInStock': '0'})['ProductName'])


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
collection2= db.Orders


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
print("\n(con filter)Los Productos con 0 unidades en Stock son:")
products= list(collection.find())
stock0=list(filter(lambda x:x['UnitsInStock']=='0',products))
for i in stock0:
    print(i['ProductName'])



# Valor del Stock= UntisInStock x UnitPrice
print("\nValores de Stock:")
cursor = collection.find()
total_value=0
while(cursor.alive):
    target=cursor.next()
    print(f"Stock Value de {target['ProductName']:35}:{float(target['UnitsInStock'])*float(target['UnitPrice'])}€")
    total_value+=float(target['UnitsInStock'])*float(target['UnitPrice'])
print(f"\nValor total de Stock: {total_value}")

# Con un FOR y otra formula es realizarlo con MAP() SUM


#(avanzado) Con una funcion AGGREGATE de mongoDB y los operadores $sum y $multiply
print(f"\n(Con AGGREGATE)Valor total de Stock: ")
query= [
    {"$match":{"UnitsInStock": {"$ne":"0"}}},
    {"$addFields":{
        "Price":{"$toDouble": "$UnitPrice"},
        "Stock":{"$toInt": "$UnitsInStock"}
    }},
    {"$group": {
        "_id": "Valor del Stock",
        "Total": {"$sum": {"$multiply": ["$Price", "$Stock"]}},
        "Products":{"$sum":1}
    }}
        
]

cursor = db.Products.aggregate(query)
print(cursor.next())

# Con un identificador de pedido
    #ID_pedido= input("Introdusca el Id del pedido: ")
# Listar dato---> ShipName, ShipAddress, ShipCity, ShipCountry, OrderDate, ShipDate
    #print(collection2.find_one({'OrderId': '10248'})['ShipName'])
# Mostramos el detalle del pedido --> Producto, Cantidad, Precio Total, Total Pedido


