########################################################################################
#  Ejercicio 10A
########################################################################################
"""  Escribe una función que pinte por pantalla un triangulo, cuadrado o circulo. Utiliza como máximo 10 sentencias print.

Entrada de datos:
tipo de figura

Salida de datos:
figura impresa

"""
#########################################################################################
# Podria sustituirse por un dictionario con las tres figuras como keys y las listas en los respectivos values
triangulo= ["   *   ","  * *  "," *   * ","* * * *"]
cuadrado= ["* * * *","*     *","*     *","* * * *"]
circulo= ["  * *  ","*     *","*     *","  * *  "]

def Figura(figura):
    if(figura == "triangulo"):
        for i in triangulo:
                print(i)
    if(figura == "cuadrado"):
        for i in cuadrado:
                print(i)
    if(figura == "circulo"):
        for i in circulo:
                print(i)
    else: 
        print("Figura no registrada")


# Toma de datos
volver=1
while(volver==1):
    volver3=1
    while(volver3==1):
        try:
           figura=input("Escriba el nombre de la figura deseada(triángulo,cuadrado,círculo): ")
           Figura(figura)
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