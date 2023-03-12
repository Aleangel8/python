########################################################################################
#  Ejercicio 3A
########################################################################################
"""  
Escribe una función que calcule los impuesto a pagar depediendo el salario.

Tabla: Menos de 10.000 5% Entre 10.000 y 20.000 15% Entre 20.000 y 35.000 20% Entre 35.000 y 60.000 30% Más de 60.000 45%

        En concepto de desempleo     4%
        En concepto de formación   1,2%


Entrada de datos:

Salario
Salida de datos:

Datos desglosados

"""
#########################################################################################



# Toma de datos
volver=1
while(volver==1):
    while(volver==1):
        try:
            print("Bienvenido")
            salary = float(input("Introduzca su salario:"))     
# Procesar datos
            if(salary<10000):
                base_tax = salary*0.05
            if(10000<=salary<=20000):
                base_tax = salary*0.15
            if(20000<salary<=35000):
                base_tax = salary*0.20
            if(35000<salary<=60000):
                base_tax = salary*0.30
            if(salary>60000):
                base_tax = salary*0.45
            print(f"Usted pagará los siguientes impuestos :\nImpuesto base: {base_tax}€\nImpuesto por desempleo: {salary*0.04}€\nImpuesto por formacion: {salary*0.012}€")
           
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