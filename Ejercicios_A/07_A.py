########################################################################################
#  Ejercicio 7A
########################################################################################
"""  Escribe una función que calcule el interés de una inversion.

Entrada de datos:

Importe total
Interés anual
Salida de datos:

Importe invertido + beneficios a un día, un mes, un trimestre, un semestre y un año
"""
#########################################################################################
import random

def cal_interes_anual(monto, tasa):
    return monto*tasa


# Toma de datos
volver=1
while(volver==1):
    volver3=1
    while(volver3==1):
        try:
            monto=float(input("\nIndique la cantidad a invertir: "))
            tasa=float(input("Indique el interes anual: "))   
            ganancia_A=cal_interes_anual(monto, tasa)
            ganancia_6M=ganancia_A/2
            ganancia_3M=ganancia_A/4
            ganancia_M= ganancia_A/12
            ganancia_D= ganancia_M/30
            print(f"\nLa ganancia anual es: {ganancia_A:.2f}€")
            print(f"La ganancia semestral es: {ganancia_6M:.2f}€")
            print(f"La ganancia trimestral es: {ganancia_3M:.2f}€")
            print(f"La ganancia mensual es: {ganancia_M:.2f}€")
            print(f"La ganancia diaria: {ganancia_D:.2f}€")

        except ValueError:
            print(ValueError)
            volver3=1
        else:
            volver3=0

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