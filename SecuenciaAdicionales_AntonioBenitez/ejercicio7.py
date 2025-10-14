# // Sentencias de Secuencias Adicionales - Ejercicio 7
# Programa que recoge los números finales de una lista
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def finales(num:int,lista:list) -> list:
    finales = []
    temp = lista
    for i in range(num):
        finales.append(temp[-1])
        temp.pop()
    finales.reverse()
    return finales
#PROGRAMA ========================================================================= 
numeros = [10, 5, 2, 3, 5, 4, 15]
print("Lista original:",numeros)
print(f'Últimos 3 números: {finales(3,numeros)}')