#calcular el area de un circulo mediante el ingreso de su radio

import math

pi = math.pi

radio = float(input("Ingrese el radio del circulo: "))
area = pi * radio ** 2

print("El area del circulo es {}".format(area))


