# Posicion 0: un numero
# Posicion 1: un numero
# Posicion 2: un textp con la operacion a realizar -> sum, res, div, mul

def Calcular(*arg):
    if(arg[2]=="sum"):
        return arg[0]+arg[1]
    if(arg[2]=="res"):
        return arg[0]-arg[1]
    if(arg[2]=="div"):
        return arg[0]/arg[1]
    if(arg[2]=="mul"):
        return arg[0]*arg[1]

suma=Calcular(15,5,"sum")
resta=Calcular(15,5,"res")
divi=Calcular(15,5,"div")
multi=Calcular(15,5,"mul")

print(f"La suma de 15 y 5 es: \n{suma}")
print(f"La resta de 15 y 5 es: \n{resta}")
print(f"La divicion de 15 y 5 es: \n{divi}")
print(f"La multiplicacion de 15 y 5 es: \n{multi}")

