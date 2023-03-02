########################################################################################
#  Tabla de multiplicar
########################################################################################
# Requerimientos
#  Numero introducido por usuario
#  Resolver con for y con while
#  
#   
#      
#       Falta con el for y validar datos
#########################################################################################


#######       FOR

volver=1
while(volver==1):
    while(volver==1):
        try:
            Numero = int(input("Introduzca un numero: "))
        except:
            print("Datos Incorrectos")
            volver=1
        else:
            volver=0

    for i in range(0, 11, 1):
        print(int(Numero)*i)
        i +=1


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



"""
#######   WHILE
volver=1
while(volver==1):
    while(volver==1):
        try:
            Numero = int(input("Introduzca un numero: "))
        except:
            print("Datos Incorrectos")
            volver=1
        else:
            volver=0

    c=0
    while(c<=10):
        print(int(Numero)*c)
        c +=1


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


"""