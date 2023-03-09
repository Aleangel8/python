numeros = [8, 14, 65, 7, 14, 99, 745, 1, -35, 1408]
"""
def demo1(lista):
    resultado = []
    for i in lista:
        return i*5
    
def demo2(lista):
    resultado = []
    for i in lista:
        resultado.append(i*5)
        
    return resultado

print(demo1(numeros))
print(demo2(numeros))
"""
def demo3(lista):
    for i in lista:
        yield(i*5)

print("Resultado: ",demo3(numeros))
print("Resultado to-list",list(demo3(numeros)))

#Imprime algo raro pero es asi
generador = demo3(numeros)
#Imprime los valores 1 a 1
print(next(generador))
print(next(generador))
print(next(generador))

print("")

#Imprime cada uno de los valores generados
generador = demo3(numeros)
for i in generador:
    print(">>", i)
print("")

#Imprime el 1 y 2 uno a uno y los demas con for por donde se queda
generador2 = ((i * 5) for i in numeros)
print("Next>>>", next(generador2))
print("Next>>>", next(generador2))
for i in generador2:
    print("For>>>", i)

print("Next>->", next(generador2))
print("Next>->", next(generador2))
for i in generador2:
    print("For>->", i)
