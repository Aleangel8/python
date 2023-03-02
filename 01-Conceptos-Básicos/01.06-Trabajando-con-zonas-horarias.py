from datetime import datetime, timedelta, timezone
from pytz import timezone
import pytz

# Mostrar 

#print(pytz.all_timezones)
#print(type(pytz.all_timezones))

#Mostrar la fecha actual
dt= datetime.now()
print(dt)

print("Tokyo")
print(datetime.now(pytz.timezone("Asia/Tokyo")))
print("Madrid")
print(datetime.now(pytz.timezone("Europe/Madrid")))
print("Alaska")
print(datetime.now(pytz.timezone("US/Alaska")))
print("UTC")
print(datetime.now(pytz.timezone("UTC")))


#####   pip install pytz