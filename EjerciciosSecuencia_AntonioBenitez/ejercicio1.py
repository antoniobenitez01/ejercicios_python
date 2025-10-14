# // Sentencias de Secuencias - Ejercicio 1
# Programa que recoge números de teclado para
# mostrarlos a continuación de distintos modos en secuencia
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
# NUM CHECK - Comprueba que el dato introducido por teclado es un número
def numCheck(mensaje):
    isNum = False
    while(isNum is False):
        try:
            print(mensaje)
            num = int(input("Número: "))
            isNum = True
            return num
        except ValueError:
            print("No se ha introducido un número, inténtelo de nuevo.")
#PROGRAMA =========================================================================     
num = 1
numeros = []
while(num != 0):
    num = numCheck("Introduzca un número para añadir a la lista.\nSi introduce 0, se parará el programa.")
    if(num != 0):
        numeros.append(num)
print("Lista de números original:",numeros)
numeros.sort()
print("Lista de números en orden creciente:",numeros)
numeros.reverse()
print("Lista de números en orden decreciente:",numeros)