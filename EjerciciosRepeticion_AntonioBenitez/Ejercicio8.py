# //Sentencias de Repetición - Ejercicio 8
# Programa que recoge un número y calcula si es primo
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
import math
print("Introduzca un número por teclado.")
num = int(input("Número: "))
isPrimo = False
if(num > 1):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i != 0:
            isPrimo = True
if(isPrimo is True):
    print("El número introducido es primo.")
else:
    print("El número introducido no es primo.")