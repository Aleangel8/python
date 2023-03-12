from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys, json


"""

===================================================

 Listado de operadores relacionales

===================================================

$eq - equal - igual

$lt - low than - menor que

$lte - low than equal - menor o igual que

$gt - greater than - mayor que

$gte - greater than equal - mayor o igual que

$ne - not equal - distinto

$in - in - dentro de

$nin - not in - no dentro de

$and

$or

"""


client= MongoClient("mongodb://127.0.0.1:27017")
db= client.Northwind
collection = db.Customers

"""
cursor = collection.find({"Country":"Mexico"})

while(cursor.alive):
    d=cursor.next()
    pprint(d["CompanyName"])
    pprint(d["CustomerID"])

    cursor2 =db.Orders.find({"CustomerID":d["CustomerID"]})
    while(cursor2.alive):
        pedido= cursor2.next()
        print(pedido["OrderID"], pedido["OrderDate"])
    print("")
    
"""
# Los datos de ANATR y todos sus pedidos

cursor = db.Customers.aggregate([
   {"$match": {"CustomerID": "ANATR"}},
   {"$sort": {"City": 1}},
   {"$lookup": {
        "from": "Orders",
        "localField": "CustomerID",
        "foreignField": "CustomerID",
        "as": "Orders"
   }}
])

while(cursor.alive):
    customer = cursor.next()
    print(f"{customer['CustomerID']}# {customer['CompanyName']}")
    for order in customer["Orders"]:
        print(f">>> {order['OrderID']} {order['OrderDate']}")