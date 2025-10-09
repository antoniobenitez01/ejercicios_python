# //Sentencias de Repetición - Ejercicio 4
# Programa que recoge un número y muestra un triángulo con el número como base
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
print("Introduzca un número por teclado")
num = int(input("Número: "))
for n in range(0,num):
    for nn in range (0,n+1):
        print("* ",end="")
    print()