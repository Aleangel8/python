########################################################################################
#  Calcular velocidad
########################################################################################
# Requerimientos
#  Calc velocidad en km/h
#  La info la tenemos en metros y minutos
#  Mostrar si es alta o Moderada
#  Alta por encima de 75 km/h. baja <30 y moderada el resto 
#      
#       Faltaria validar datos añadir try
#########################################################################################

metros=input("Introduzca los metros: ")
minutos=input("Introduzca los minutos: ")

Km=int(metros)/1000
h=int(minutos)/60
Km_h=Km/h

print(f"Usted va a {Km_h} Km/h")
if(Km_h>75):
    print("Usted va a alta velocidad")
if(30<=Km_h<=75):
    print("Usted va bien")
if(Km_h<30):
    print("Usted va a baja velocidad")