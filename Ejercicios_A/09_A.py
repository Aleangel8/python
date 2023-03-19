########################################################################################
#  Ejercicio 9A
########################################################################################
"""  Escribe un programa que muestre el nombre del día de la semana del cumpleaños del usuario desde su nacimiento hasta hoy.

Entrada de datos:

Fecha de nacimiento
Salida de datos:

Nombre del día de la semana de cada año
"""
#########################################################################################
from datetime import datetime

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']


# Toma de datos
volver=1
while(volver==1):
    volver3=1
    while(volver3==1):
        try:
            today = datetime.now()
            d=int(input("Indique el dia de su nacimiento: "))
            m=int(input("Indique el mes de su nacimiento: "))
            y=int(input("Indique el año de su nacimiento: "))
            while(y<=today.year):    
                fecha = datetime(y, m, d) # crea un objeto datetime con la fecha deseada
                dia_semana = fecha.weekday() # obtiene el número del día de la semana un valor entre 0 y 6
                print(f"\nLa fecha {fecha.strftime('%d/%m/%Y')} corresponde al día {dias_semana[dia_semana]}") 
                y+=1
        except ValueError:
            print("Fecha introducida incorrecta")
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



