"""
for i in range(0, 50, 1):
    print(f"Numero {i}")
for j in range(30, 50, 2):
    print(f"Numero {j}")
for k in range(20, 0, -3):
    print(f"Numero {k}")

citricos = ["naranja", "limón", "pomelo", "lima","mandarina"]

for x in range(0, len(citricos), 1):#   Devuelve en x las posiciones no se usa
    print(f"{x}: {citricos[x]}")

print("")

for x in citricos:#  Devuelve el valor en x, Es el tipo***
    print(f"{x}")

"""
for x in range(0, 50, 1):
    print(f"Numero {x}- Inicio")
    if(x == 10):
        continue
    if(x == 20):
        break
    print(f"Numero {x} - Fin")