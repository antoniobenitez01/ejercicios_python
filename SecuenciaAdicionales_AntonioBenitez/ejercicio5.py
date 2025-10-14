# // Sentencias de Secuencias Adicionales - Ejercicio 5
# Programa que devuelve el rango de una lista de números
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def rango(lista: list) -> list:
    lista.sort()
    numMin = lista[0]
    lista.reverse()
    numMax = lista[0]
    return [numMin,numMax]
#PROGRAMA ========================================================================= 
numeros = [5,8,10,2,3,1]
print("Lista original:",numeros)
print(f'Rango de números: {rango(numeros)}')
