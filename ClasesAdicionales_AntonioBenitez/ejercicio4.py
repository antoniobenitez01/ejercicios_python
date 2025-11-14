# //Clases Adicionales - Ejercicio 4
# Sistema para gestionar los empleados de una Empresa mediante el uso de clases
# Empleado, Asalariados, Por Hora, Comisionistas
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/11/2025

from abc import ABC,abstractmethod

# ---       EMPLEADO
class Empleado(ABC):

    @abstractmethod
    def __init__(self,nombre:str,id:str,salario:float):
        self.__nombre = nombre
        self.__id = id
        self.__salario = salario;

    @property
    def nombre(self):
        return self.__nombre
    @property
    def id(self):
        return self.__id
    @property
    def salario(self):
        return self.__salario
    
    @abstractmethod
    def calcular_salario(self):
        pass

# ---       EMPLEADO - Asalariados
class Asalariados(Empleado):

    def __init__(self,nombre:str,id:str,salario:float):
        super().__init__(nombre,id,salario)
    
    def calcular_salario(self):
        return self.salario

# ---       EMPLEADO - Por Hora
class PorHora(Empleado):

    def __init__(self,nombre:str,id:str,salario:float,horas:int):
        if(horas > 160): raise Exception("El campo Horas no puede ser mayor de 160")
        super().__init__(nombre,id,salario)
        self.__horas = horas

    @property
    def horas(self):
        return self.__horas
    
    def calcular_salario(self):
        return self.salario * self.horas

# ---       EMPLEADO - Comisionistas
class Comisionistas(Empleado):

    def __init__(self,nombre:str,id:str,salario:float,porcentaje:int):
        if((porcentaje < 0) or (porcentaje > 100)): raise Exception("El campo Porcentaje debe estar entre 0 y 100")
        super().__init__(nombre,id,salario)
        self.__porcentaje = porcentaje
    
    @property
    def porcentaje(self):
        return self.__porcentaje
    
    def calcular_salario(self) -> float:
        return self.salario + (self.salario * (self.porcentaje / 100))

# ---       PROGRAMA
empleados = [Asalariados("Antonio","AAA111",2500),PorHora("María","BBBB222",10,100),Comisionistas("Carlos","CCC333",1500,50)]
suma = 0;
for empleado in empleados:
    print(f"Calculando Salario de Clase {empleado.__class__.__name__}: {empleado.calcular_salario()}€")
    suma += empleado.calcular_salario()
print(f"Salario Total de Empresa: {suma}€")