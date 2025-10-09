# //Sentencias de Repetición - Ejercicio 7
# Programa que recoge una cadena de texto y una letra a buscar
# para mostrar el número de veces que aparece esa letra en la cadena
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
print("Introduzca una cadena de texto por teclado.")
cadena = input("Texto: ")
print("Introduzca un carácter a buscar.")
caracter = input("Carácter: ")
suma = 0
for i in range(0,len(cadena)):
    if(cadena[i] is caracter):
        suma += 1
print("El carácter",caracter,"ha aparecido",suma,"veces en la cadena introducida.")