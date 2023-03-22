########################################################################################
#  00 Declaracion de la renta
########################################################################################
"""  Escribe un programa que muestre el nombre del día de la semana del cumpleaños del usuario desde su nacimiento hasta hoy.

Entrada de datos:
Ingresos
Pagos ya realizados

Salida de datos:
Total Ganado
Total A Pagar
Total neto


Diferencia de pago


Hasta 12.450 €, el tipo impositivo es de 19%.
De 12.450 € a 20.200 €, el tipo impositivo es de 24%.
De 20.200 € a 35.200 €, el tipo impositivo es de 30%.
De 35.200 € a 60.000 €, el tipo impositivo es de 37%.
De 60.000 € a 300.000 €, el tipo impositivo es de 45%.
"""
#########################################################################################
earnings= []
payments_made= []

def Calc(earnings,payments_made):
    Total_earnings=sum(earnings)
    Total_payment_made=sum(payments_made)
    T1=0
    T2=0
    T3=0
    T4=0
    T5=0
    if(Total_earnings<12450):
        T1=Total_earnings*0.19
    if(12450<=Total_earnings<20200):
        T1= 12450*0.19
        T2= (Total_earnings-12450)*0.24
    if(20200<=Total_earnings<35200):
        T1= 12450*0.19
        T2= 20200*0.24
        T3= (Total_earnings-20200)*0.30
    if(35200<=Total_earnings<60000):
        T1= 12450*0.19
        T2= 20200*0.24
        T3= 35200*0.30
        T4= (Total_earnings-35200)*0.37
    if(60000<=Total_earnings<300000):
        T1= 12450*0.19
        T2= 20200*0.24
        T3= 35200*0.30
        T4= 60000*0.37
        T5= (Total_earnings-60000)*0.45
    
    print(f"Total Ganado: {Total_earnings}€")
    print(f"Total a Pagar: {T1+T2+T3+T4+T5}")
    print(f"Total Pagado: {Total_payment_made}€")
    print(f"Diferencia: {Total_payment_made-(T1+T2+T3+T4+T5)}")
    print(f"Ganancias netas: {Total_earnings-(T1+T2+T3+T4+T5)}")

# Toma de datos
volver=1
while(volver==1):
    volver3=1
    while(volver3==1):
        try:
            # Coger todas las Ganancias
            volver4=1
            while(volver4==1):
                earning=float(input("Ingrese sus Ganancias, ponga 0 para terminar:"))
                if(earning!=0):
                    earnings.append(earning)
                if(earning==0):
                    volver4=0
            # Coger todos los Pagos
            volver5=1
            while(volver5==1):
                payment_made=float(input("Ingrese sus Pagos, ponga 0 para terminar:"))
                if(payment_made!=0):
                    payments_made.append(payment_made)
                if(payment_made==0):
                    volver5=0
            # Calcular Declaracion
            Calc(earnings,payments_made)
        except ValueError:
            print("Fecha introducida incorrecta")
            volver3=1
        else:
            volver3=0

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



