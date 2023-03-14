numeros = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]

print(f"Valores mayores de 100: ", list(filter(lambda x: x > 100, numeros)))
print(f"Valores pares: ", list(filter(lambda x: x % 2 == 0, numeros)))
print(f"Valores menores de 50: ", list(filter(lambda x: x < 50, numeros)))

print("===========================================================================")


def Procesar(lista):
    resultado = []
    for numero in lista:
        resultado.append(numero * 10)
    
    return resultado

print(numeros)
print(Procesar(numeros))

print(list(map(lambda x: x*10, numeros)))
print(list(map(lambda x: f"{x} x 10 = {x*10}", numeros)))

print(list(map(lambda x: x*10, filter(lambda x: x > 100, numeros))))
print(list(filter(lambda x: x > 700, map(lambda x: x*10, numeros))))