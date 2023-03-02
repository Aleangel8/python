#Cadena de caracteres
print("")
cadena="j   Hola Mundo  !!!"
print(cadena)
print(cadena[2])
print(cadena[2:])
print(cadena[2:6])
print(cadena[-2])
print(len(cadena))
print(cadena[-5:-2])
print(cadena[-5:])

print("")

print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.strip())
print(cadena.replace("o","0"))
print(cadena.isdigit())
print("57".isdigit()) 

######## Formatear Cadenas ##########
print("")
mensaje= input()

print("Hola "+ mensaje + " !!!")
print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))

print(f"Hola {mensaje} {mensaje} !!!")#Este es el mas bueno con formato

resultado ="Hola {s} !!!".format(s=mensaje)
print(resultado)
numero = 10/3
print(numero)
print(f"{numero}")
print("{:.2f}".format(numero))# sacar el numero con dos cifras decimales
print("Hola")

############ Falta la division formateada
