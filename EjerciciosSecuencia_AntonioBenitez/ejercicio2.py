# // Sentencias de Secuencias - Ejercicio 2
# Programa que recoge cadenas de texto por teclado para
# mostrarlos a continuación de distintos modos en secuencia
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

cadena = "hola"
cadenas = []
while("".join(cadena.split()) != ""):
    print("Introduzca una cadena de texto por teclado.\nSi no introduce nada o solo espacios, se parará el programa.")
    cadena = (input("Cadena: "))
    if("".join(cadena.split()) != ""):
        cadenas.append(cadena)
print("Cadenas de texto originales:",cadenas)
cadenas.sort()
print("Cadenas de texto en orden creciente:",cadenas)
cadenas.reverse()
print("Cadenas de texto originales en orden decreciente:",cadenas)