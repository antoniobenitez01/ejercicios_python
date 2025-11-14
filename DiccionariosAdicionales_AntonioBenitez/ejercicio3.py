# // Diccionarios Adicionales - Ejercicio 3
# Programa de Análisis de Ventas Diarias y Mensuales de El Gran Bazar
# mediante el uso de Diccionarios
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/11/2025

def sumaVentas(dias: dict):
    suma = 0
    for dia in ventas[producto]:
        suma += ventas[producto][dia]
    return suma

ventas = {
    "A": {1: 5, 2: 3, 3: 6, 4: 8, 5: 1},
    "B": {1: 3, 2: 7, 3: 2, 4: 0, 5: 4},
    "C": {1: 6, 2: 4, 3: 3, 4: 5, 5: 2},
    "D": {1: 0, 2: 2, 3: 1, 4: 3, 5: 0}
}

print("1. Calcular Total Unidades Vendidas en el Mes por cada Producto\n")
for producto in ventas:
    suma = sumaVentas(ventas[producto])
    print(f"Producto {producto}\t- Total Unidades Vendidas: {suma} {"unidad" if suma == 1 else "unidades"}")

print("\n2. Identificar el Producto con Más y Menos Ventas en el Mes\n")
for i in range(1,6):
    prodMin = ""
    prodMax = ""
    min = 100
    max = 0
    for producto in ventas:
        if(ventas[producto][i] > max):
            prodMax = producto
            max = ventas[producto][i]
        if(ventas[producto][i] < min):
            prodMin = producto
            min = ventas[producto][i]
    print(f"DÍA {i} - MÍNIMO = {prodMin}: {min} - MÁXIMO = {prodMax}: {max}")

print("\n3. Ventas diarias del Producto Más Vendido\n")
prodMax = ""
max = 0
for producto in ventas:
    suma = sumaVentas(ventas[producto])
    if(suma > max):
        prodMax = producto
        max = suma
diarias = max / len(ventas[prodMax])
print(f"VENTAS DIARIAS - Producto {prodMax}\tVentas: {diarias} {"venta" if diarias == 1 else "ventas"}")

print("\n4. Día con Mayor Venta por Producto\n")
for producto in ventas:
    diaMax = 1
    max = 0
    for dia in ventas[producto]:
        if(ventas[producto][dia] > max):
            max = ventas[producto][dia]
            diaMax = dia
    print(f"Producto {producto}\t- Día Máximo: {diaMax} - Ventas: {max}")