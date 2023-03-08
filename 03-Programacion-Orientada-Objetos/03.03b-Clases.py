class A:
    Num1= 0
    Num2= 0

    def __init__(self) -> None:
        self.Num1
        self.Num2

    def Suma(self) ->int:
        return self.Num1+self.Num2
    
    def Resta(self) ->int:
        return self.Num1-self.Num2
    
class B:
    Numero1= None
    Numero2= None

    def __init__(self, n1, n2) -> None:
        self.Numero1=n1
        self.Numero2=n2

    def Suma(self) ->int:
        return self.Numero1+self.Numero2
    
    def Div(self) ->int:
        return self.Numero1/self.Numero2

class Calculadora(B, A): pass  #El orden determina la prioridad de herenciadi

c= Calculadora(36, 18)
print(f"Suma: {c.Suma()}")
print(f"Resta: {c.Resta()}")
print(f"Dividir: {c.Div()}")
print(dir(c))# Nos muestra todo el contenido de la clase