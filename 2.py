#Utilzar placeholder. sep y end en el print

print("Esto cambio el caracteres final del print", end='@')

#le aplico un salto de linea para que no quede todo junto
print()

print("Esto cambiar el caracteres de separacion de las palabras", sep='.')

datos = {"nombre": "Dario", "ciudad":"Mar del Plata"}
print("Utilzamos placeholder. Mi nombre es {} y soy de la ciudad de {}" .format(datos["nombre"], datos["ciudad"]))