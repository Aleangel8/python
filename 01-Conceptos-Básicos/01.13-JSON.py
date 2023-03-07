import json   #Para el intercambio y almacenamiento de datos

frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]
frutasJSON = json.dumps(frutas)

print(frutas)
print(type(frutas))

print(frutasJSON)# Las tildes las imprime mal en JSON
print(type(frutasJSON))

print(frutas[2])
print(frutasJSON[2])#Pinta la n de naranja ya que es una cadena de caracteres

frutas2= json.loads(frutasJSON)
print(frutas2)
print(type(frutas2))
print(f"Posicion 2 fruta2: {frutas2[2]}")