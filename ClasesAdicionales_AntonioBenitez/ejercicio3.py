# //Clases Adicionales - Ejercicio 3
# Sistema para gestionar Vehículos en una flota de transporte mediante el uso de
# las clases Vehiculo, Coche, Moto y Camion
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/11/2025

from abc import ABC,abstractmethod

# ---   VEHICULO
class Vehiculo(ABC):

    @abstractmethod
    def __init__(self, modelo:str, anyo:int,litros:int):
        self.__modelo = modelo
        self.__anyo = anyo
        self.__litros = litros

    @property
    def modelo(self):
        return self.__modelo
    @property
    def anyo(self):
        return self.__anyo
    @property
    def litros(self):
        return self.__litros
    
    def calcular_consumo(self, kilometros: int) -> float:
        return (self.litros/100) * kilometros
    
# ---   VEHICULO - Coche
class Coche(Vehiculo):
    def __init__(self,modelo:str,anyo:int):
        super().__init__(modelo,anyo,5)

# ---   VEHICULO - Camion
class Camion(Vehiculo):

    def __init__(self,modelo:str,anyo:int,carga:int):
        super().__init__(modelo,anyo,20)
        self.__carga = carga

    @property
    def carga(self):
        return self.__carga
    
    def calcular_consumo(self,kilometros: int) -> float:
        consumo = (self.litros/100) * kilometros
        consumo += (consumo * 0.1) * self.carga
        return consumo
    
# ---   VEHICULO - Moto
class Moto(Vehiculo):
    def __init__(self,modelo:str,anyo:int):
        super().__init__(modelo,anyo,3)

# --- PROGRAMA
vehiculos = [Coche("Toyota Yaris",2019),Camion("Honda Truck",2014,5),Moto("Yamaha Turbo",2001)]
for vehiculo in vehiculos:
    print(f"Consumo del Vehículo {vehiculo.__class__.__name__}: {vehiculo.calcular_consumo(200)} litros")
