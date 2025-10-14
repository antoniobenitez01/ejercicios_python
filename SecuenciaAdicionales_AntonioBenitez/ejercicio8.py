# // Sentencias de Secuencias Adicionales - Ejercicio 8
# Programa que recoge los números finales de una lista
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================
def segmento(min:int,max:int,lista:list) -> list:
    segmento = []
    contador = min
    for i in range(len(lista)):
        if(contador>=min and contador<=max):
            segmento.append(lista[contador-1])
        contador += 1
    return segmento
#PROGRAMA ========================================================================= 
numeros = [5,10,12,24,4,3,2]
print("Lista original:",numeros)
print(f'Números comprendidos entre 3 y 6: {segmento(3,6,numeros)}')