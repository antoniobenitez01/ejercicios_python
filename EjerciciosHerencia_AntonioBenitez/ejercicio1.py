# //Herencia - Ejercicio 1
# Programa que define una clase Persona
# Autor: Antonio Benítez Rodríguez
# Fecha: 11/11/2025

class Persona():

    # ---   CONSTRUCTOR

    def __init__(self, nombre:str="Sin Nombre", apellidos:str="Sin Apellidos", edad:int=0, dni:str="Sin DNI"):
        if nombre == "": raise Exception("El campo nombre no puede estar vacío")
        if apellidos == "": raise Exception("El campo apellidos no puede estar vacío")
        if edad < 0: raise Exception("Edad debe ser 0 o mayor")
        if dni == "": raise Exception("El campo DNI no puede estar vacío")
        self.__nombre = nombre.upper()
        self.__apellidos = apellidos.upper()
        self.__edad = edad
        self.__dni = dni.upper()

    # ---   GETTERS

    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellidos(self):
        return self.__apellidos
    @property
    def edad(self):
        return self.__edad
    @property
    def dni(self):
        return self.__dni
    
    # ---   SETTERS

    @nombre.setter
    def nombre(self,nombre:str):
        if nombre == "": raise Exception("El campo nombre no puede estar vacío")
        self.__nombre = nombre.upper()
    @apellidos.setter
    def apellidos(self,apellidos:str):
        if apellidos == "": raise Exception("El campo apellidos no puede estar vacío")
        self.__apellidos = apellidos.upper()
    @edad.setter
    def edad(self,edad:int):
        if edad < 0: raise Exception("Edad debe ser 0 o mayor")
        self.__edad = edad
    @dni.setter
    def dni(self,dni:str):
        if dni == "": raise Exception("El campo DNI no puede estar vacío")
        self.__dni = dni.upper()
    
    # ---   MÉTODOS

    def mayorDeEdad(self) -> bool:
        return self.edad > 18
    
    def mostrar(self):
        print(f"{self.nombre + " " + self.apellidos} - Edad: {self.edad} - DNI: {self.dni}")
    