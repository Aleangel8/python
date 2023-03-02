########################################################################################
#  Calcular velocidad
########################################################################################
# Requerimientos
#  Calc velocidad en km/h
#  La info la tenemos en metros y minutos
#  Mostrar si es alta o Moderada
#  Alta por encima de 75 km/h. baja <30 y moderada el resto 
#      
#       
#########################################################################################


volver=1
while(volver==1):
    while(volver==1):
        try:
            metros=input("Introduzca los metros: ")
            minutos=input("Introduzca los minutos: ")
            Km=int(metros)/1000
            h=int(minutos)/60
            Km_h=Km/h
        except ValueError:
            print("Datos Incorrectos")
            volver=1
        else:
            volver=0

    print(f"Usted va a {Km_h} Km/h")
    if(Km_h>75):
        print("Usted va a alta velocidad")
    if(30<=Km_h<=75):
        print("Usted va bien")
    if(Km_h<30):
        print("Usted va a baja velocidad")

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