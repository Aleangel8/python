from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client= MongoClient("mongodb://127.0.0.1:27017")

# Listar los nombres de las bases de datos en mongoDB
print(client.list_database_names(),"\n")

# Seleccionamos una base de datos con la q vamos a trabajar de dos vias
    # Sintaxis de objeto
db= client.Northwind
    # Sintaxis de objeto de colección
db2= client["Northwind"]


# Listar los nombres de las colecciones de la base de datos
print(db.list_collection_names(), "\n")
print(db2.list_collection_names(),"\n")#print(client.Northwind.list_collection_names())

# Seleccionar una coleccion 2 vias igualmente
collection = db.Customers
collection = db2["Customers"]

# Mostrar el número de documentos(registros) en la colección
print(f"{collection.estimated_document_count()} documentos en {collection.name} \n")

# LEER DATOS
result = collection.find_one({"Country": "USA"})
pprint(result)
print("")
"""#Da un cursor
result2 = collection.find({"Country": "USA"})
pprint(result2)"""

# No se suele Buscar por ID
id = ObjectId("6409a708863c6f666759e8c1")
result2 = collection.find_one({"_id":id})
pprint(result2)