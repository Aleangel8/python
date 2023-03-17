########################################################################################
#  Ejercicio 6A
########################################################################################
"""  
Escribe una función que calcule el precio de una pizza.

Entrada de datos:

Ingredientes + Cantidad del ingrediente (almacenar en listas)
FIN, la cofección de la pizza a finalizado
Salida de datos:

Coste de las pizza desglosado

# Ejercicio 6A

ingredientes = { "Base": 8.90, "Pepperoni": 0.50,
 "Pollo": 0.35, "Carne": 0.35, "Pimiento": 0.25, "Cebolla": 0.25, "Champiñon": 0.25, "Aceituna": 0.50, "Piña": 0.35, "ExtraQueso": 1 }

     
"""
#########################################################################################
import random
def cal_order(order):pass

list_ing=["ba", "pe", "po", "ca", "pi", "ce", "ch", "ac", "pi", "ex"]
ingredientes = {"ba": 8.90, "pe": 0.50,
 "po": 0.35, "ca": 0.35, "pi": 0.25, "ce": 0.25, "ch": 0.25, "ac": 0.50, "pi": 0.35, "ex": 1}




def cal_Precio(order):
    Total_Price=0
    for i in order:
        Total_Price+=order[i]
    return Total_Price
    

# Toma de datos
volver=1
while(volver==1):
    order={"ba": 8.90, "pe": 0.00,
 "po": 0.00, "ca": 0.00, "pi": 0.00, "ce": 0.00, "ch": 0.00, "ac": 0.00, "pi": 0.00, "ex": 0.00}
    print(f"\nWELCOME to PIZZA-CODE")
    print("Carta(Precio Base: 8.90€):\n\nAgregos:\n1-Pepperoni: 0.50€\n2-Pollo: 0.35€\n3-Carne: 0.35€\n4-Pimiento: 0.25€\n5-Cebolla: 0.25€\n6-Champiñon: 0.25€\n7-Aceituna: 0.50€\n8-Piña: 0.35€\n9-ExtraQueso: 1€")
    while(volver==1):
        try:
            # Tomar pedido
            opt=input("Desea agregos: Si(1) o No(0): ")
            if(opt=="1"):
            
                agrego=int(input("Indique el numero del agrego: "))
                cant=float(input("Indique la cantidad: "))
                # Busco con el numero en la lista de ingredientes y modifico la orden usando la plantilla de ingredientes por la cantidad
                order[list_ing[agrego]]=ingredientes[list_ing[agrego]]*cant
                opt=input("Desea algo más: Si(1) o No(0): ")                   
                if(opt=="1"):
                    print("Carta(Precio Base: 8.90€):\n\nAgregos:\n1-Pepperoni: 0.50€\n2-Pollo: 0.35€\n3-Carne: 0.35€\n4-Pimiento: 0.25€\n5-Cebolla: 0.25€\n6-Champiñon: 0.25€\n7-Aceituna: 0.50€\n8-Piña: 0.35€\n9-ExtraQueso: 1€")
                    volver=1
                if(opt=="0"):
                    print("Pizza preparada:")
                    volver=0
            else:        
                print("Pizza preparada:")
                volver=0
        except ValueError:
            print("Error, no introdujo uno valor numerico")
            volver=1


    Total_Price=cal_Precio(order)
    print(f"La pizza cuesta: {Total_Price}€")
    print(f"El deslose de la cuenta es{order}")



#   Check volver a intentar y validar entrada
    volver2=1
    while(volver2==1):   
        try:
           volver=(input("Pulse 0 para Salir, Cualquier otro numero volver a intentar : "))
           if(int(volver)!=0):
            volver=1   
        except ValueError:
            print("No se introdujo un numero")
            volver2=1
        else:
            volver2=0