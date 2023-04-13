
import datetime

print(datetime.date.today())
print(datetime.datetime.now())

fecha_completa = datetime.datetime.now()

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
print(fecha_completa.hour)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y")
print(fecha_personalizada)
