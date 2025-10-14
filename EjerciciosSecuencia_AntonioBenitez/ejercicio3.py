# // Sentencias de Secuencias - Ejercicio 3
# Programa que lee un texto y determina si es palíndromo
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def esPalindromo(cadena:str) -> bool:
    esPali = False
    temp1, temp2 = cadena[:len(cadena)//2], cadena[len(cadena)//2:]
    if(len(temp1) != len(temp2)):
        temp2 = temp2[1:]
    temp2 = temp2[::-1]
    if(temp1.lower() == temp2.lower()):
        esPali = True
    return esPali
#PROGRAMA =========================================================================  
print("Introduzca una cadena de texto.")
cadena = input("Cadena: ")
if(esPalindromo(cadena)):
    print("La cadena introducida es un palíndromo.")
else:
     print("La cadena introducida no es un palíndromo.")