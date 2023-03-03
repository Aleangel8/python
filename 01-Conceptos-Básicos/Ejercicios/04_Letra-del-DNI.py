########################################################################################
#  Calcular la letra del DNI
########################################################################################
# Requerimientos
#  Calc la letra del DNI
#  Resto de dividir el DNI %23, el resto
#  
#   
#      
#       
#########################################################################################

letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D','X']

volver=1
while(volver==1):
    while(volver==1):
        try:
            DNI=input("Introduzca su DNI sin Letra: ")
            DNI_resto=int(DNI)%23
            
        except ValueError:
            print("Datos Incorrectos")
            volver=1
        else:
            volver=0
    print(f"Su letra es: {letras[DNI_resto]}")
    
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