# // Sentencias de Secuencias Adicionales - Ejercicio 10
# Programa que determina el mayor rectángulo según el área de dos rectángulos
# Autor: Antonio Benítez Rodríguez
# Fecha: 20/10/2025

#FUNCIONES =========================================================================
def mayorRectangulo(rec1:list,rec2:list) -> list:
    recMayor = []
    area1 = rec1[0] * rec1[1]
    area2 = rec2[0] * rec2[1]
    if(area1 > area2):
        recMayor = rec1
    else:
        recMayor = rec2
    return recMayor
#PROGRAMA ========================================================================= 
rec1 = [5,3]
print("Rectángulo 1:",rec1)
rec2 = [2,6]
print("Rectángulo 2:",rec2)
print(f"Rectángulo mayor: {mayorRectangulo(rec1,rec2)}")