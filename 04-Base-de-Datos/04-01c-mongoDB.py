from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

client= MongoClient("mongodb://127.0.0.1:27017")
db= client.Northwind
collection = db.Customers
"""
cursor = collection.find({"Country":"USA"})
cursor = collection.find({"Country":"USA"}).limit(3)
cursor = collection.find({"Country":"USA"}).skip(5)

cursor = collection.find({"Country":"USA"}).limit(10)
cursor = collection.find({"Country":"USA"}).skip(10).limit(10)
cursor = collection.find({"Country":"USA"}).skip(20).limit(10)
cursor = collection.find({"Country":"USA"}).skip(30).limit(10)

cursor = collection.find({"Country":"USA"}).sort("City")#Ascendente A a W
cursor = collection.find({"Country":"USA"}).sort("City", 1)#Ascendente A a W
cursor = collection.find({"Country":"USA"}).sort("City", -1)#Descendente W a A

print("")
while(cursor.alive):
    d = cursor.next()
    print(d["CompanyName"], d["Country"],d["City"])
    print("")
"""




#cursor = collection.find({"Country":"USA"})
#cursor = collection.find({"Country":{"$eq":"USA"}})

#Todos los clientes que no son de USA
#cursor = collection.find({"Country":{"$ne":"USA"}})

#Todos los clientes que son de USA y Mexico
#cursor = collection.find({"Country":{"$in":["USA","Mexico"]}}).sort("Country")

#Clientes de San Fracncisco en USA
cursor = collection.find({"Country":"USA","City":"San Francisco"})

#print(f"Numero de documentos: {cursor.count()}")
#print(f"Numero de documentos filtrados con lista: {len(list(cursor))}")

#print("Numero de documentos  filtrados:", collection.count_documents({"Country":"USA"}))
#print(f"Numero de documentos sin filtrar: {collection.estimated_document_count()}")

#print("Datos pendiente de leer: ", cursor.alive)


while(cursor.alive):
    pprint(cursor.next())
    print("")
print("Datos pendientes de leeer: ", cursor.alive)

print("==================================================================================================================================")
"""
cursor = collection.find({"Country":"USA"})
for document in list(cursor):
    pprint(document)
    print("")

"""
