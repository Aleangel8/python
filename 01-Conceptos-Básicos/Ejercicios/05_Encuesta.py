########################################################################################
#  Encuesta
########################################################################################
# Requerimientos
#  Visualizar la media de opinión
#  Visualizar el número total de encuestados
#   
#       Utilizar Listas
#       sin limites de entradas
#       ver media 
#       total de participantes
#       Opiniones entre 0-10
#       el resultado al poner fin
#       ver el promedio por edades Menor 18,18-55, Mayor q 55 
#########################################################################################

Nombre_List=[]
Edad_List=[]
Opinion_List=[]

# Toma de datos
volver=1
while(volver==1):
    while(volver==1):
        try:
            print("Bienvenido a la encuesta")
            nombre=input("Introduzca su nombre: ")
            edad=int(input("Introduzca su edad: "))
            opinion=int(input("Introduzca su opinion del 0-10: "))
            """if(opinion>10):
                print("Opinion Fuera de rango")
                volver=1  """  
        except ValueError:
            print("Datos Incorrectos")
            volver=1
        else:
            volver=0

# Añadir a Lista
    print("")
    Nombre_List.append(nombre)
    Edad_List.append(edad)
    Opinion_List.append(opinion)

# Calcular Media Opinion Total
    suma_opi=0
    for i in Opinion_List:
        suma_opi += i
    media_opi=suma_opi/len(Opinion_List)

# Calcular Media Edad Total
    suma_age=0
    for i in Edad_List:
        suma_age += i
    media_age=suma_age/len(Edad_List)

# Calcular Media Edad <18
    suma_age18=0
    c0=0
    for i in Edad_List:
        if(i<18):
            suma_age18 += i
            c0 += 1
    if(c0!=0):
        media_age18=suma_age18/c0

# Calcular Media Edad 18-55
    suma_age18_55=0
    c1=0
    for i in Edad_List:
        if(18<=i<=55):    
            suma_age18_55 += i
            c1 += 1
    if(c1!=0):        
        media_age18_55=suma_age18_55/c1

# Calcular Media Edad >55
    suma_age_55=0
    c2=0
    for i in Edad_List:
        if(i>55):
            suma_age_55 += i
            c2 += 1
    if(c2!=0):
        media_age_55=suma_age_55/c2

# Ver resultados
    if(len(Edad_List)!=0):
        print(f"El total de participantes es: {len(Edad_List)}")
        print("")
        print(f"La media de opinion es: {media_opi}")
        print("")
        print(f"La media Total de edad es: {media_age}")
    if(c0!=0):
        print(f"La media <18 de edad es: {media_age18}")
    if(c1!=0):    
        print(f"La media >18 y <55 de edad es: {media_age18_55}")
    if(c2!=0):
        print(f"La media >55 de edad es: {media_age_55}")

    print("")
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