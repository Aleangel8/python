"""
yield permite extraer valores de una funcion y almacenarlos de uno en uno
en objetos iterables q se pueden recorrer, sin la necesidad de ocupar memoria RAM

son mas eficientes q funciones tradicionales y va bien para listas de valores infinitos
entre llamada y llamada entra en un estado de pausa
"""



numeros = [8, 14, 65, 7, 14, 99, 745, 1, -35, 1408]



# Solo devolverá el 1er elemento de la lista x5
def demo1(lista):
    for i in lista:
        return i * 5

# Devuelve toda la lista x5
def demo2(lista):
    resultado = []
    for i in lista:
        resultado.append(i * 5)
    return resultado



def demo3(lista):
    for i in lista:
        yield (i * 5)


# Devuelve el objeto de tipo generador
print("\nResultado:", demo3(numeros))
# Transforma el generador en una lista
print("Resultado To-List:", list(demo3(numeros)))

# Imprime los generadores uno a uno
generador = demo3(numeros)
print(next(generador))
print(next(generador))
print(next(generador))


# Imprime todos los generadores
generador = demo3(numeros)
for i in generador:
    print(">>", i)


exit()
generador2 = ((i * 5) for i in numeros)
print("\nNext>>>", next(generador2))
print("Next>>>", next(generador2), "\n")

for i in generador2:
    print("For>>>", i)

print("Next>->", next(generador2))
print("Next>->", next(generador2))
for i in generador2:
    print("For>->", i)