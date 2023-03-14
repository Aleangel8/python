from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json


class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Country = None
    PostalCode = None
    Region = None
    Phone = None
    Fax = None



client= MongoClient("mongodb://127.0.0.1:27017")
db= client.Northwind
collection = db.Customers

cliente = Customer()
cliente.CustomerID= "DEM10"
cliente.CompanyName= "Un Dos Tres Bebidas, SL"
cliente.ContactName="Borja"
cliente.ContactTitle= "Propietario"
cliente.Address= "Gran Via 44"
cliente.City= "Madrid"
cliente.Country= "Spain"
cliente.PostalCode= "08390"
cliente.Region= "Logroño"
cliente.Phone= "600982110"
cliente.Fax= "1287381279"

print(cliente.__dict__)

resultado = collection.insert_one(cliente.__dict__).inserted_id
print(f"ID: {resultado}")
exit()

#$regex se usa para ver si contiene
cursor = collection.find({"CustomerID": {"$regex": "Demo2"}})
while(cursor.alive):
    doc= cursor.next()
    print(f"{doc['CustomerID']}# {doc['CompanyName']}")




cliente = {"CustomerID": "Demo2",
        "CompanyName": "Uno Comunidad SL",
        "ContactName": "Angel Alejandro",
        "ContactTitle": "Propietario",
        "Address": "Calle Industria, 62",
        "City": "Barcelona",
        "Country": "Spain",
        "PostalCode": "08380",
        "Region": "Malgrat de Mar",
        "Phone":"600982110",
        "Fax":"912002021"
        }

resultado = collection.insert_one(cliente)
print(f"Resultado: {resultado}")
print(f"Object ID: {resultado.inserted_id}")
print(f"Acknowledged: {resultado.acknowledged}")


