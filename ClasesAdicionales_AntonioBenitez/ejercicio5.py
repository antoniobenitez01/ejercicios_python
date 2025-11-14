# //Clases Adicionales - Ejercicio 5
# Sistema para gestionar los vehículos que operan en la flota
# de una Empresa de Transporte mediante el uso de las clases
# GestionFlota, Vehiculo, Auto, Camion
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/11/2025

from abc import ABC,abstractmethod
from funciones import *

# ---       VEHICULO
class Vehiculo(ABC):
    @abstractmethod
    def __init__(self,matricula:str,modelo:str,disponible:bool):
        self.__matricula = matricula
        self.__modelo = modelo
        self.disponible = disponible
    @property
    def matricula(self):
        return self.__matricula
    @property
    def modelo(self):
        return self.__modelo

    # - Alternar Disponibilidad: Alterna la Disponibilidad del Vehículo
    def alternarDisponibilidad(self):
        if self.disponible == True:
            self.disponible = False
        else:
            self.disponible = True
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.matricula}\t- Modelo: {self.modelo}\tDisponible: {"Sí" if self.disponible else "No"}"

# ---       VEHICULO - Auto
class Auto(Vehiculo):
    def __init__(self,matricula:str,modelo:str,disponible:bool,asientos:int):
        super().__init__(matricula,modelo,disponible)
        self.__asientos = asientos
    @property
    def asientos(self):
        return self.__asientos
    def __str__(self):
        return super().__str__() + f"\tAsientos: {self.asientos}{"asiento" if self.asientos == 1 else "asientos"}"

# ---       VEHICULO - Camion
class Camion(Vehiculo):
    def __init__(self,matricula:str,modelo:str,disponible:bool,carga:float):
        super().__init__(matricula,modelo,disponible)
        self.__carga = carga
    @property
    def carga(self):
        return self.__carga
    def __str__(self):
        return super().__str__() + f"\tCarga: {self.carga}kg"

# ---       GESTION de FLOTA
class GestionFlota():
    def __init__(self,vehiculos:dict[str,Vehiculo]):
        self.__vehiculos = vehiculos

    @property
    def vehiculos(self):
        return self.__vehiculos
    
    # - Registrar Vehículo: Registra el Vehículo introducido por parámetro en la Flota
    def registrarVehiculo(self,vehiculo : Vehiculo):
        if(vehiculo.matricula in self.vehiculos):
            print("El Vehículo introducido ya está registrado.")
        else:
            self.vehiculos[vehiculo.matricula] = vehiculo

    # - Consultar Vehículo: Imprime la información del Vehículo con la Matrícula introducida por parámetro
    def consultarVehiculo(self,matricula: str):
        if(matricula in self.vehiculos):
            print(self.vehiculos[matricula])
        else:
            print("La Matrícula introducida no está registrada.")

    # - Listar Vehículos: Imprime la información de todos los vehículos disponibles en la Flota
    def listarVehiculos(self):
        for matricula in self.vehiculos:
            if(self.vehiculos[matricula].disponible):
                print(self.vehiculos[matricula])
    
    # - Cambiar Estado: Alterna el Estado del Vehículo con la Matrícula introducida por parámetro
    def cambiarEstado(self, matricula:str):
        if(matricula in self.vehiculos):
            self.vehiculos[matricula].alternarDisponibilidad()
        else:
            print("La Matrícula introducida no está registrada.")

    # - Eliminar Vehículo: Elimina el Vehículo con la Matrícula introducida por parámetro      
    def eliminarVehiculo(self, matricula:str):
        if(matricula in self.vehiculos):
            if(booleanCheck("¿Está seguro de que desea eliminar este Vehículo? (SI/NO)")):
                del self.vehiculos[matricula]
            else:
                print("Operación cancelada.")
        else:
            print("La Matrícula introducida no está registrada.")

# ---       PROGRAMA

#       Creación inicial de Diccionario de Vehículos
vehiculos : dict = {
    "0001AAA" : Auto("0001AAA","Toyota Yaris",True,4),
    "0002BBB" : Camion("0002BBB","Mazda Truck",True,10000),
    "0003CCC" : Auto("0003CCC","Seat Ibiza",True,2),
    "0004DDD" : Camion("0004DDD","Honda Limit",True,20000),
}
flota = GestionFlota(vehiculos)
opcion : int = 0
while(opcion != 6):
    opcion = menu("\n=== GESTIÓN FLOTA DE VEHÍCULOS ==="+
               "\n1. Registrar un Nuevo Vehículo"+
               "\n2. Consultar datos Vehículos por Matrícula"+
               "\n3. Listar Vehículos disponibles"+
               "\n4. Cambiar Estado de Vehículo por Matrícula"+
               "\n5. Eliminar Vehículo por Matrícula"+
               "\n6. Apagar el programa",1,6)
    match(opcion):
        case 1:
            newVehiculo = None
            print("\nIntroduzca la Matrícula del nuevo Vehículo.")
            newMatricula = input("Matrícula: ")
            print("Introduzca el Modelo del nuevo Vehículo.")
            newModelo = input("Modelo: ")
            newDisponible = booleanCheck("¿El Vehículo está Disponible? (SI/NO)")
            if(tipoCheck("¿Que tipo de Vehículo es? ( AUTO / CAMION )")):
                newAsientos = numCheck("Introduzca el número de Asientos.","Asientos: ")
                newVehiculo = Auto(newMatricula,newModelo,newDisponible,newAsientos) 
            else:
                newCarga = numCheck("Introduzca la carga en kilogramos.","Carga: ")
                newVehiculo = Camion(newMatricula,newModelo,newDisponible,newCarga) 
            if(newVehiculo != None):
                flota.registrarVehiculo(newVehiculo)
            else:
                print("Ha ocurrido un problema al crear el nuevo Vehículo.")
        case 2:
            print("\nIntroduzca la Matrícula del Vehículo a consultar.")
            buscarMatricula = input("Matrícula: ")
            flota.consultarVehiculo(buscarMatricula)
        case 3:
            print()
            flota.listarVehiculos()
        case 4:
            print("\nIntroduzca la Matrícula del Vehículo para cambiar su Estado.")
            buscarMatricula = input("Matrícula: ")
            flota.cambiarEstado(buscarMatricula)
        case 5:
            print("\nIntroduzca la Matrícula del Vehículo a eliminar.")
            buscarMatricula = input("Matrícula: ")
            flota.eliminarVehiculo(buscarMatricula)
        case 6:
            print("Apagando programa ...")