# //Sentencias de Repetición - Ejercicio 5
# Programa que recoge un número y muestra los primeros
# cuadrados hasta llegar al número introducido
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
print("Introduzca un número por teclado")
num = int(input("Número: "))
for n in range(1,num+1):
    print(n ** 2,end=" ")