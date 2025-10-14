# // Sentencias de Secuencias - Ejercicio 4
# Programa que lee dos cadenas de texto por teclado y
# determina si una es palíndromo de la otra
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def esPalindromo(cadena1:str,cadena2:str,mayus:bool) -> bool:
    esPali = False
    if(mayus is False):
        if(cadena1.lower() == cadena2[::-1].lower()):
            esPali = True
    else:
        if(cadena1 == cadena2[::-1]):
            esPali = True
    return esPali

def booleanCheck(mensaje:str) -> bool:
    chosen = False
    boolean = False
    while(chosen is False):
        print(mensaje)
        respuesta = input("Respuesta: ")
        if(respuesta.lower() == "si" or respuesta.lower() == "sí"):
            boolean = True
            chosen = True
        elif(respuesta.lower() == "no"):
            boolean = False
            chosen = True
        else:
            print("La respuesta introducida no es válida, inténtelo de nuevo.")
    return boolean
#PROGRAMA =========================================================================  
print("Introduzca una cadena de texto.")
cadena1 = input("Cadena: ")
print("Introduzca otra cadena de texto.")
cadena2 = input("Cadena: ")
mayus = booleanCheck("¿Desea tener en cuenta las mayúsculas o no? (SI o NO)")
if(esPalindromo(cadena1,cadena2,mayus)):
    print(f'{cadena1} es un palíndromo de {cadena2}')
else:
     print(f'{cadena1} no es un palíndromo de {cadena2}')