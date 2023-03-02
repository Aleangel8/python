########################################################################################
#  Calcular la edad
########################################################################################
# Requerimientos
#  Calc edad
#  Mostrar si es mayor
#  Si no es mayor mostrar cuanto le falta en años
#   
#      
#       Falta validar datos
#########################################################################################
from datetime import datetime
import time
volver=1
while(volver==1):

    Fecha_Nacim=input("Escribe tu fecha de Nacimiento: ")
    dt_actual = datetime.strptime(Fecha_Nacim, "%d-%m-%Y").date()

    t1 = time.time()
    t_local = time.localtime(t1)
    edad = t_local.tm_year-dt_actual.year

    
    print(f"La edad del usuario es: {edad}")
    if(edad<18):
        print(f"Es menor de edad, le faltan: {18-edad} años para ser mayor")
    else:
        print("Es mayor de edad")
    volver=int(input("Desea volver a intentar 1:Si  0:NO : "))


