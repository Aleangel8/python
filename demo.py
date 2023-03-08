"""def nombre():
    print(" funcion nombre")

def saludo(texto):
    print(" funcion nombre")
    print(f"Contenido de texto; {texto}")
    texto= "Nuevo valor"
    print(f"Contenido de texto; {texto}")

def demo(): pass # permite la no implementacion sin dar error

def demo2(texto, numero):
    print(f"Contenido de texto: {texto}")
    print(f"Contenido de numeto: {numero}")

def suma(a, b):
    return a+b

class Persona: pass


print(type(nombre))
print(type(saludo))
print(type(Persona))


nombre()
saludo("13212312")
demo2(20,34)
demo2(20, True)
demo2("holahola",[1,2,3,4])
print(suma(3, 4))
print(type(suma(3, 4)))



def resta(a, b):
    c= a - b
    return c

def resta2(a, b=50):
    c= a - b
    return c

def resta3(a=80, b=50):
    c= a - b
    return c

print(resta(10,20))
print(resta2(10))
print(resta3(b=10))

numeros = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]

def MayorDeCien(lista):
    resultado = []

    for item in lista:
        if(item > 100):
            resultado.append(item)

    return resultado

print(MayorDeCien(numeros))

#===========================================================

def Func1(x):
    if(x >100):
        return True
    else:
        return False

def Func2(x):
    if(x %2==0):
        return True
    else:
        return False



print(list(filter(Func2, numeros)))

#=============================================================

print(f"Valores Lambda >100: {list(filter(lambda a: a>100, numeros))}")
print(f"Valores Lambda son par: {list(filter(lambda a: a%2==0, numeros))}")
print(f"Valores Lambda <50: {list(filter(lambda a: a<50, numeros))}")

def Filtrado(formula, datos):
    resultado = []
    for i in datos:
        if(formula(i)):
            resultado.append(i)
    return resultado

print(">>>", Filtrado(lambda x: x<50, numeros))
"""

import asyncio

async def main():
    print("Hola ....")
    await asyncio.gather(func1(), func2())
    await asyncio.sleep(5)
    print(".... Mundo !!!")

async def func1():
    for i in range(11):
        print(i)
        await asyncio.sleep(1)

async def func2():
        print("Hola Func2")
        await asyncio.sleep(5)
        print("Fin Func2")


print("inicio")
asyncio.run(main())
print("fin")