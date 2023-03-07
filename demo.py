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

"""

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

