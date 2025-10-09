# //Sentencias de Repetición - Ejercicio 10
# Programa que recoge un número y muestra un triángulo
# formado por secuencias decrecientes de números impares
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
import math
print("Introduzca un número.")
num = int(input("Número: "))
contador = 1
max = 1
for i in range(1,num+1):
    max = contador
    for j in range(1,i+1):
        print(contador," ",end="")
        contador -= 1
        while(contador % 2 == 0 and contador > 1):
            contador -= 1
    contador = max + 2
    print()