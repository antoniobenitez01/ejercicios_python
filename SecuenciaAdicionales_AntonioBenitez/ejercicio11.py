# // Sentencias de Secuencias Adicionales - Ejercicio 10
# Programa que intercambia las coordenadas X e Y
# Autor: Antonio Benítez Rodríguez
# Fecha: 20/10/2025

#FUNCIONES =========================================================================
def intercambiar(coor:list) -> list:
    return [coor[1],coor[0]]
#PROGRAMA ========================================================================= 
coor1 = [5,2]
print("Coordenada 1:",coor1)
print(f"Coordenada intercambiada: {intercambiar(coor1)}")
coor2 = [6,7]
print("Coordenada 2:",coor2)
print(f"Coordenada intercambiada: {intercambiar(coor2)}")