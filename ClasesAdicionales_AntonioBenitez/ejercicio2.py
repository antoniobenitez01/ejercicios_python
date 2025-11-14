# //Clases Adicionales - Ejercicio 2
# Sistema para gestionar reservas en un hotel mediante el uso de 
# clases Reserva, Individual, Doble y Suite
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/11/2025

from abc import ABC,abstractmethod

# ---       RESERVA
class Reserva(ABC):

    @abstractmethod
    def __init__(self, precio:float):
        if precio < 0: raise Exception("El campo Precio no puede ser menor que 0.")
        self.__precio = precio

    @property
    def precio(self):
        return self.__precio

    def calcular_precio(self,noches) -> float:
        return self.precio * noches

# ---       RESERVA - Individual
class Individual(Reserva):

    def __init__(self):
        super().__init__(50)

# ---       RESERVA - Dobles
class Dobles(Reserva):

    def __init__(self,suplemento: bool):
        super().__init__(75)
        self.__suplemento = suplemento

    @property
    def suplemento(self):
        return self.__suplemento
    
    def calcular_precio(self,noches):
        precioFinal = self.precio * noches
        if(self.suplemento):
            precioFinal += 10
        return precioFinal

# ---       RESERVA - Suite
class Suite(Reserva):

    def __init__(self):
        super().__init__(150)

    def calcular_precio(self,noches):
        precioFinal = self.precio * noches
        if(noches > 3):
            precioFinal -= (precioFinal * 0.1)
        return precioFinal

# ---       PROGRAMA
reservas = [Individual(),Dobles(True),Suite()]
for reserva in reservas:
    print(f"Precio por estancia en {reserva.__class__.__name__}: {reserva.calcular_precio(5)}€")