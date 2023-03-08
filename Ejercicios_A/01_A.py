########################################################################################
#  Ejercicio 1A
########################################################################################
"""  Escribe una función para calcular el consumo medio de combustible de un vehículo.

Entrada de datos:
    -Kilometros recorridos
    -Listros de combustible consumidos
Salida de datos:
    -litros consumidos por kilimetro
"""
#########################################################################################
#Con funcion
"""def consumo(Km, Litros):
    return Km/Litros"""



# Toma de datos
volver=1
while(volver==1):
    while(volver==1):
        try:
            print("Bienvenido")
            km=int(input("Introduzca cant de Km: "))
            litros=int(input("Introduzca el consumo en Litros: ")) 
# Procesar Datos
            consumo=lambda km,litros:km/litros
            print(f"Usted consume {consumo(km,litros)} Km/L") 
        except ZeroDivisionError:
            print("Consumo 0 es imposible")
            volver=1    
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