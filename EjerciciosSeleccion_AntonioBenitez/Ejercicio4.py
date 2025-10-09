# //Sentencias de Selección - Ejercicio 4
# Programa que recoge un dividendo y un divisor,
# realizando la división siempre y cuando el divisor no sea cero
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca el dividendo")
x = int(input("Dividendo: "))
print("Introduzca el divisor")
y = int(input("Divisor: "))
if y == 0:
    print("No se puede dividir entre 0.")
else:
    print("La división de los números introducidos es", x/y)