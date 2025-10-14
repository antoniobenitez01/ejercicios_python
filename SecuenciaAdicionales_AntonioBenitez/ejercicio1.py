# // Sentencias de Secuencias Adicionales - Ejercicio 1
# Programa que cuenta las vocales de una cadena de texto
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def contarVocales(cadena:str) -> int:
    numVocales = 0
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for c in cadena:
        if c.isalpha():
            if c in vocales:
                numVocales += 1
    return numVocales
#PROGRAMA =========================================================================
print("Introduzca una cadena de texto por teclado.")
cadena = input("Cadena: ")
print("Número de vocales:",contarVocales(cadena))