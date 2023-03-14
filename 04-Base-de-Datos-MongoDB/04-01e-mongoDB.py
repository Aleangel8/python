from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client= MongoClient("mongodb://127.0.0.1:27017")
db= client.Northwind
collection = db.Customers





exit()

# Buscar y Eliminar
result = collection.delete_one({"CustomerID":"Demo1"})
print(f"{result.deleted_count} documentos eliminados")

# Buscar y Modificar
query= {"CustomerID": "DEM10"}
documento = collection.find_one(query)
pprint(documento)

newValues = {"$set": {"Address": "Callle Serrano, 81", 
                      "PostalCode": "28016",
                      "Phone": "914592525"}}

result = collection.update_one(query, newValues)
print(result.matched_count,"documentos encontrados")
print(result.modified_count, "documentos modificados")
print(result)
pprint(collection.find_one(query))


result = collection.delete_many({"CustomerID": {"$regex": "DEMO"}})
print(f"{result.deleted_count} documentos eliminados")
print(f"{collection.count_documents({'CustomerID': {'$regex': 'DEMO'}})} clientes DEMO")