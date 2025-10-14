# // Sentencias de Secuencias Adicionales - Ejercicio 2
# Programa que cuenta cuántas palabras hay en una cadena de texto
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def contarPalabras(cadena:str) -> int:
    return len(cadena.split())
#PROGRAMA =========================================================================
print("Introduzca una cadena de texto por teclado.")
cadena = input("Cadena: ")
print("Número de palabras:",contarPalabras(cadena))