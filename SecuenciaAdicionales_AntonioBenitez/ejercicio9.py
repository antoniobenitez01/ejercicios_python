# // Sentencias de Secuencias Adicionales - Ejercicio 9
# Programa que recoge los primeros y últimos números de una lista
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def extremos(num:int,lista:list) -> list:
    extremos = []
    for i in range(num):
        extremos.append(lista[i])
    temp1 = lista
    temp1.reverse()
    temp2 = []
    for i in range(num):
        temp2.append(temp1[i])
    temp2.reverse()
    extremos = extremos + temp2
    return extremos
#PROGRAMA ========================================================================= 
numeros = [5,10,12,24,4,3,2]
print("Lista original:",numeros)
print(f'Mostrando 2 Números de cada extremos: {extremos(2,numeros)}')