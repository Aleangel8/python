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
"""


# Crear el objeto que representa el cliente para trabajar con la DB
# Se requiere la cadena de conexion

client= MongoClient("127.0.1¡0.1", 27017)
client= MongoClient("localhost", 27017)
client= MongoClient("mongodb://127.0.0.1:27017")

client= MongoClient("mongodb://localhost:27017")


# Mostrar el estado del servidor
# Nos posicionamos en una base de datos utilizando el objetp cliente
db = client.admin

# Ejecutamos un comando sobre las bases de datos
# Los comandos nos permiten INSERTAR, ACTUALIZAR, ELIMINAR y LEER informacion de la DB

# El comando serverStatus nos retorna el estado del servidor en JSON
status = db.command("serverStatus")
pprint (status)

