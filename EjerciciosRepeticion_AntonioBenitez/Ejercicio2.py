# //Sentencias de Repetición - Ejercicio 2
# Programa que recoge un número y calcula su factorial
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
print("Introduzca un número por teclado.")
num = int(input("Número: "))
for n in range(1,num):
    num = num * n
print("Resultado factorial:",num)