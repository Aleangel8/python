# Posicion 0: un numero
# Posicion 1: un numero
# Posicion 2: un textp con la operacion a realizar -> sum, res, div, mul

def Calcular(*arg):
#Verifica en que posicion está el str
    if(type(arg[0])==str):
        n1=arg[1]
        n2=arg[2]
        cal=arg[0]
    if(type(arg[1])==str):
        n1=arg[0]
        n2=arg[2]
        cal=arg[1]
    if(type(arg[2])==str):
        n1=arg[0]
        n2=arg[1]
        cal=arg[2]
#Realiza los calculos
    if(cal=="sum"):
        return n1+n2
    if(cal=="res"):
        return n1-n2
    if(cal=="div"):
        return n1/n2
    if(cal=="mul"):
        return n1*n2
#Imprime
suma=Calcular(15,5,"sum")
resta=Calcular("res",15,5)
divi=Calcular(15, "div",5)
multi=Calcular(15,5,"mul")

print(f"La suma de 15 y 5 es: \n{suma}")
print(f"La resta de 15 y 5 es: \n{resta}")
print(f"La divicion de 15 y 5 es: \n{divi}")
print(f"La multiplicacion de 15 y 5 es: \n{multi}")

