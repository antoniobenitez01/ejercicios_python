# //Sentencias de Repetición - Ejercicio 9
# Programa que comprueba que se recoge un número impar para
# a continuación mostrar una pirámide de astericos con el número como base
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
import math
# ========== COMPROBACIÓN NÚMERO IMPAR ===========
num = 10
while(num % 2 == 0):
    print("Introduzca un número impar.")
    num = int(input("Número: "))
    if(num % 2 == 0):
        print("El número introducido no es impar, inténtelo de nuevo")
# ================== PROGRAMA ====================
space = int(num/2) + 1 # Calculamos el número de espacios inicial
for i in range(1,num+1):
    if i%2!=0:
        for j in range(1, space):
            print(" ",end="")
        for k in range(0,i):
            print("*",end="")
        print()
        space -=1
space = 1
for i in range(num-1, 0,-1):
    if i%2 != 0:
        for j in range(0,space):
            print(" ",end="")
        for k in range(0,i):
            print("*",end="")
        print()
        space += 1

        