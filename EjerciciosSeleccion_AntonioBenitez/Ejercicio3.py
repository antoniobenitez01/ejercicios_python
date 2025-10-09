# //Sentencias de Selección - Ejercicio 3
# Programa que lee 3 números y los ordena de menor a mayor
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca 3 números")
x = int(input("1º Número: "))
y = int(input("2º Número: "))
z = int(input("3º Número: "))
if x > y:
    x,y = y,x
if x > z:
    x,z = z,x
if y > z:
    y,x = x,y
print (x, "<", y, "<", z)
