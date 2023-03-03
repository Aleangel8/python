########################################################################################
#  Colecciones-Dictionario
########################################################################################
#
#  
#  
#
#   
#      
#       
#########################################################################################

vacio = {}
frutas = {"NA":"naranja", "LI":"limón", "PO":"pomelo", "LM":"líma", "MA":"mandarina"}

# Mostrar el diccionario entero
print(frutas)   

# Mostrar un valor utilizando la clave, de no existir produce una exception
print(frutas["NA"])

# Mostrar valor que no existe con metodo get para evitar exception
print(frutas.get("NA"))
print(frutas.get("NI"))

# Pintar el numero de valores en el dictionary
print(len(frutas))

# Modificar el valor de un elemento
frutas["NA"] = "Sandia"
frutas.update({"NA": "ciruela"})
print(">> "+ frutas["NA"])

# Añadir un nuevo valor al diccionario
frutas["ME"] = "melón"

# Eliminar un valor utilizando la clave
frutas.pop("NA")
del frutas["LM"]

# Recorremos y mostramos todos los valores con FOR
for key in frutas:
    print(f"Cave: {key} - Valor: {frutas[key]}")

print(frutas)