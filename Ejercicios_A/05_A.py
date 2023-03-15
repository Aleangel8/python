########################################################################################
#  Ejercicio 5A
########################################################################################
"""  Escribe un programa que genere un número aleatorio. El usuario escribe números y el programa le responde si acertado y no acertado.
 Al no acertar debe indicarle si el número es menor o mayar.

Entrada de datos:
Número

Salida de datos:
Mensajes: has acertado; no has acertado, es menor; no has acertado es mayor


import random

num_rand = random.randint(1, 20)
"""
#########################################################################################
import random

# Toma de datos
volver=1
while(volver==1):
    num_rand = random.randint(1, 10)
    print(f"(Para probar)El numero randon es este: {num_rand}")
    while(volver==1):
        try:
            num=int(input("Introduzca un numemero a ver si aciertas: "))
            while(num_rand!=num):
                if(num_rand>num):
                    print("No has acertado tu numero es menor")         
                    raise ValueError
                if(num_rand<num):
                    print("No has acertado tu numero es mayor")         
                    raise ValueError      
            print("CONGRATS has acertado")   
        except ValueError:
            print("Vuelva a intentar")
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