########################################################################################
#  Ejercicio 4A
########################################################################################
"""  Escribe una función que cuente las vocales de una frase.

Entrada de datos:

Una frase
Salida de datos:

Número de vocales desglosado
"""
#########################################################################################
#Con funcion
def vocal(frase):
    ca=0
    ce=0
    ci=0
    co=0
    cu=0
    deletrear=list(frase)
    for i in deletrear:
        if(i=='a'):
            ca+=1
        elif(i=='e'):
            ce+=1            
        elif(i=='i'):
            ci+=1
        elif(i=='o'):
            co+=1
        elif(i=='u'):
            cu+=1 
    return ca, ce , ci, co, cu   



# Toma de datos
volver=1
while(volver==1):
    while(volver==1):
        try:
            print("Bienvenido")
            frase=(input("Introduzca una frase: ")).lower()
            cvocal=vocal(frase)
            print(f"A: {cvocal[0]} \nE: {cvocal[1]} \nI: {cvocal[2]} \nO: {cvocal[3]} \nU: {cvocal[4]}")             
        except ValueError:
            print("Datos Incorrectos")
            volver=1
        else:
            volver=0





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