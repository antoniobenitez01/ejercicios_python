# //Clases Adicionales - Ejercicio 1
# Programa que gestiona los productos de una tienda mediante el uso
# de las clases Producto, Electronicos, Ropa y Comida
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/11/2025

# ---   PRODUCTO
class Producto():

    def __init__(self, nombre:str, precio:float, descuento:int):
        if descuento < 0: raise Exception("El descuento del Producto no puede ser menor que 0.")
        self.__nombre = nombre
        self.__precio = precio
        self.__descuento = descuento
    
    def precio_final(self):
        return self.__precio - (self.__precio * (self.__descuento / 100))
    
# ---   PRODUCTO - Electronicos
class Electronicos(Producto):

    def __init__(self, nombre:str, precio:float, descuento:int):
        if descuento > 10: raise Exception("El descuento de Producto Electrónico no puede ser mayor que 10%.")
        super().__init__(nombre,precio,descuento)

# ---   PRODUCTO - Ropa
class Ropa(Producto):

    def __init__(self, nombre:str, precio:float, descuento:int):
        if descuento > 20: raise Exception("El descuento de Producto Ropa no puede ser mayor que 20%.")
        super().__init__(nombre,precio,descuento)

# ---   PRODUCTO - Comida
class Comida(Producto):

    def __init__(self, nombre:str, precio:float, descuento:int):
        if descuento != 0: raise Exception("El Producto Comida no admite descuento.")
        super().__init__(nombre,precio,descuento)

# --- PROGRAMA ===
