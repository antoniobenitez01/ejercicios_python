# // Sentencias de Secuencias Adicionales - Ejercicio 6
# Programa que elimina los exteriores de una lista
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def interior(lista : list) -> list:
    return lista[1:-1]
#PROGRAMA ========================================================================= 
numeros = [10,5,2,3,4,1]
print("Lista original:",numeros)
print(f'Lista interior: {interior(numeros)}')