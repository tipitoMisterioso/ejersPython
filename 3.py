#Obtener fecha y horas actuales del sistema

import datetime as f

fecha = f.datetime.now()

print(fecha)

print(type(fecha))

print(fecha.strftime("%d/%m/%Y %H:%M:%S"))