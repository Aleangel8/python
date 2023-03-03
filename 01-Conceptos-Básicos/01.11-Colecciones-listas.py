########################################################################################
#  Colecciones-listas
########################################################################################
#
#  
#  
#
#   
#      
#       
#########################################################################################
volver=1
while(volver==1):



# Utilizamos los [] para crear listas
    vacia = []
    frutas = ["naranja", "limon", "pomelo", "lima", "mandarina"]

# Mostramos el contenido de una lista
    print(frutas)

# Mostrar el valor contenido en una posicion ( 2 = pomelo)
    print(frutas[2])

# Mostrar el numero de valores que contiene la lista
    print(len(frutas))

# Mostrar el numero de veces que se repite el mismo valor
    print(frutas.count("sandia"))

#Modificar el valor de una posición( Modificar pomelo 2 por fresa)
    frutas[2] = "fresa"
    print(frutas[2])

# Añadir nuevo valores utilizando la funcion APPEND
    frutas.append("manzana")
    frutas.append("melón")
    print(frutas)


# Añadir un nuevo valor en posicion con la funcion INSERT(index, value)
    frutas.insert(1, "sandia")
    print(frutas)


# Añadir un nuevo valor con la funcion Append si el valor no existe
    if("platano" not in frutas):
        frutas.append("platano")
    print(frutas)


# Añadir varios elementos procedentes de otra lista con extend
    nuevasFrutas=["maracuya", "kiwi", "frambuesa"]
    frutas.extend(nuevasFrutas)
    print(frutas)


# Eliminar un valor en base a la posicion utilizando POP(index)
    frutas.pop(5)
    print(frutas)


# Eliminar un valor en base al valor utilizando REMOVE(value)
    frutas.remove("naranja")
    print(frutas)


# Eliminar un valor si existe
    if("sandia" in frutas):
        frutas.remove("sandia")
    print(frutas)


# Invertir el orden de los valores utilizando REVERSE
    frutas.reverse()
    print(frutas)

# Ordenar los valores utilizando Sort
    frutas.sort()
    frutas.sort(reverse = True)
    print(frutas)


# Recorremos la lista y mostramos los valores
    for i in frutas:
        print(i)

# Copiar todos los valores de la lista
    vacia = frutas.copy()
    print(vacia)

# Eliminar todos los valores de la lista
    frutas.clear()
    print(frutas)


#   Check volver a intentar y validar entrada
    volver2=1
    while(volver2==1):   
        try:
            volver=(input("Pulse 0 para Salir, Cualquier otro numero volver a intentar : "))
            if(int(volver)!=0):
                volver=1   
        except ValueError:
            print("No se introdujo un numero")
            volver2=1
        else:
            volver2=0