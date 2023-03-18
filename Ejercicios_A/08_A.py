########################################################################################
#  Ejercicio 7A
########################################################################################
"""  Escribe una función que indique los aciertos de una combinación de loteria primitiva. Una vez introducidos los datos se genera la combinación ganadora utilizando siguiente código:

import random
n = random.randint(1, 49)

La combinación ganadora se compone de 6 números no iguales.

Entrada de datos:
Introduce 6 número distintos entre 1 y 49

Salida de datos:
Número de aciertos

"""

#########################################################################################
import random, time

def generar_primitiva():
    primitiva=[]
    primitiva.append(random.randint(1, 49))
    c=0
    while(c<5):
        randon_num=random.randint(1, 49)
        if(randon_num not in primitiva):
            primitiva.append(randon_num)
            c+=1
        
    return primitiva
        

def pedir_num():
    boleto=[]
    volver4=1
    while(volver4==1):
        num=int(input("Digame un numero del 1 al 49 sin repetir: "))
        if(num>=50):
            print("Fuera de rango")
        if(num<50):
            boleto.append(int(input("Digame un numero del 1 al 49 sin repetir: ")))
            volver4=0
    c=0
    while(c<5):
        num_sgte=int(input("Digame un numero del 1 al 49 sin repetir: "))
        if(num_sgte not in boleto and num_sgte<50):
            boleto.append(num_sgte)
            c+=1
        else:
            print("Numero repetido o fuera de rango")
                   
    return boleto





# Toma de datos
volver=1
while(volver==1):
    volver3=1
    while(volver3==1):
        try:
           print("Bienvenido a la primitiva: ")
           primitiva=generar_primitiva()
           print(primitiva)#Para comprobar q va bien
           boleto=pedir_num()
           print(f"\nTu boleto es : {boleto}")
           aciertos = set(primitiva).intersection(boleto)
           print("Has tenido ...")
           time.sleep(3)
           print(f"{len(aciertos)} aciertos en :\n {aciertos}")

        except ValueError:
            print("No se Introdujoun valor numérico")
            volver3=1
        else:
            volver3=00


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
            print("\nSigue programando vas bien")
            volver2=0
