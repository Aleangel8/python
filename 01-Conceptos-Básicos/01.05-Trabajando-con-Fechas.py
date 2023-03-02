from datetime import datetime
import time

t1 = time.time()
t2 = time.localtime(t1)
t3 = time.asctime(t2)  # datetime.srfdate(datetime.now(), "%c")

print(t1)
print(t2)
print(t2.tm_year)
print(t3)

##################################################################

dt1 = datetime.now()
print(f"Fecha 1: {dt1}")

print(" Hora:", dt1.hour)
print(" Minutos:", dt1.minute)
print(" Segundos:", dt1.second)
print(" Microsegundos:", dt1.microsecond)

dt2 = datetime.now().date()
print(f"Fecha 2: {dt2}")

print(" Dia:", dt2.day)
print(" Dia:", str(dt2.month).zfill(2))#Para que me salga con 0
print(" Dia:", dt2.year)

##################################################################

strFecha= input("Escribe tu fecha de nacimiento: ")
dt3 = datetime.strptime(strFecha, "%d-%m-%Y").date()

print(f"Fecha de nacimiento: {dt3}")
print("Fecha de Nacimiento:", dt3.strftime("%A, %d of %B, %Y"))
print(dt2.year-dt3.year1)
