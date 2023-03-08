def Saludo(nombre):
    print(f"Hola, me llamo {nombre}")

minombre= "Borja"
Saludo(minombre)
Saludo("Fco. de Borja")

demo = lambda nombre : print(f"Hola, me llamo {nombre}")
demo("Ana")

def Sumar(num):
    return lambda a : a + num

def Restar(num):
    return lambda a : a - num

def Multiplicar(num):
    return lambda a : a * num

#multiplicar = lambda a : a * num
#nombfuncion =lambda parametros  : Formula
# la llamada es igual-> nombfuncion(parametros)
def Dividir(num):
    return lambda a : a / num


def Imprimir(formula, valor):#formula es la funcion lambda retornada
    print(f"valor {valor}")
    print(f"Resultado: {formula(valor)}") 

Imprimir(Sumar(5), 25)
#Sumar(5) == formula=lambda a:a+5 
Imprimir(Restar(5), 25)
#Restar(5) == formula=lambda a:a-5 
Imprimir(Multiplicar(5), 25)
#Multiplicar(5) == formula=lambda a:a*5 
Imprimir(Dividir(5), 25)
#Dividir(5) == formula=lambda a:a:55 

#print(Multiplicar(25))