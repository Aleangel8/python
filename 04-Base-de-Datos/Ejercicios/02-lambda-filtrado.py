from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

# Definir la conexion
client= MongoClient("mongodb://127.0.0.1:27017")
db= client.Northwind
collection = db.Products

# Cuantos productos tenemos 
# Mostramos el numero de productos y un listo

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

