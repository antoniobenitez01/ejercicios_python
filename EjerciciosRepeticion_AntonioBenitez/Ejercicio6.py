# //Sentencias de Repetición - Ejercicio 6
# Programa que recoge un número de filas y columnas
# y muestra una tabla de tantas filas y columnas
# como se hayan introducido
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
print("Introduzca el número de filas.")
filas = int(input("Filas: "))
print("Introduzca el número de columnas.")
columns = int(input("Columnas: "))
contador = 1
for i in range(0,filas):
    for j in range(0,columns):
        print(contador, end=" ")
        contador += 1
    print()