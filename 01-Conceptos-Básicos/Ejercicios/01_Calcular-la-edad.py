########################################################################################
#  Calcular la edad
########################################################################################
# Requerimientos
#  Calc edad
#  Mostrar si es mayor
#  Si no es mayor mostrar cuanto le falta en años
#   
#      
#       
#########################################################################################
from datetime import datetime
import time

volver=1
while(volver==1):
#  Coge la fecha de nacimiento dt_bird y la valida
    while(volver==1):
        try:
            Fecha_Nacim=input("Escribe tu fecha de Nacimiento: ")
            dt_bird = datetime.strptime(Fecha_Nacim, "%d-%m-%Y").date()
        except ValueError:
            print("Fecha incorrecta")
            volver=1
        else:
            volver=0
#   Coge la fecha local today
    t1 = time.time()
    t_local = time.localtime(t1)
#   Calcula edad precisa
    edad = t_local.tm_year-dt_bird.year
    if(dt_bird.month>t_local.tm_mon):
        edad -=1
#   Print resultado
    print(f"La edad del usuario es: {edad}")
    if(edad<18):
        print(f"Es menor de edad, le faltan: {18-edad} años para ser mayor")
    else:
        print("Es mayor de edad")
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




