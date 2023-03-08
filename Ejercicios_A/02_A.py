########################################################################################
#  Ejercicio 2A
########################################################################################
"""  Escribir funciones para tranformar grados Celsius en Fahrenheit y viciversa.

Formulas: Celsius = (5 ÷ 9) x (Fahrenheit - 32) Fahrenheit = (Celsius x (9 ÷ 5)) + 32

Entrada de datos:
    -Grados Celsius/Fahrenheit

Salida de datos:
    -Grados transformados
"""
#########################################################################################

Celsius =lambda Fa: (5/9)*(Fa - 32)
Fahrenheit =lambda Ce: (Ce*(9/5)) + 32


# Toma de datos
volver=1
while(volver==1):
    while(volver==1):
        try:
            print("Bienvenido")
# Elegir Opcion
            opt=float(input("Introduzca 0 si desea convertir de Celsius a Fahrenheit\nIntroduzca 1 si desea convertir de Fahrenheit a Celsius\n"))
            if(opt!=0 and opt!=1):
                raise ValueError     
# Procesar datos
            temp=float(input("Introduzca la temperatura a convertir: "))
            if(opt==0):
                print(f"La temperatura en grados Fahrenheit es: {Fahrenheit(temp)}")
            if(opt==1):
                print(f"La temperatura en grados Celsius es: {Celsius(temp)}")
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