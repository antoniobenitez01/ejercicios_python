# //Clases - Ejercicio 1
# Programa que define una clase Persona
# Autor: Antonio Benítez Rodríguez
# Fecha: 11/11/2025

class Persona():

    # ---   CONSTRUCTOR

    def __init__(self, nombre:str = "Sin Nombre", direccion:str = "Sin Dirección", telefono: int = 000000000):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    # ---   GETTERS

    @property
    def nombre(self):
        return self.__nombre
    @property
    def direccion(self):
        return self.__direccion
    @property
    def telefono(self):
        return self.__telefono
    
    # ---   SETTERS

    @nombre.setter
    def nombre(self,nombre:str):
        self.__nombre = nombre
    @direccion.setter
    def direccion(self,direccion:str):
        self.__direccion = direccion
    @telefono.setter
    def telefono(self,telefono:int):
        self.__telefono = telefono

    # ---   MÉTODOS

    def __str__(self):
        return f"Nombre: {self.nombre}\t- Dirección: {self.direccion}\t- Teléfono: {self.telefono}"
    