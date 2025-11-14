# // Diccionarios Adicionales - Ejercicio 2
# Versión de Ejercicio 1 que trata con varias Personas
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/11/2025

# --- PERSONA           // Creamos la clase Persona para guardar datos facilmente
class Persona():
    def __init__(self,nombre:str,edad:int,direccion:str,telefono:int):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion
        self.__telefono = telefono

    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def direccion(self):
        return self.__direccion
    @property
    def telefono(self):
        return self.__telefono

    def __str__(self):
        return f"{self.nombre}\t- Edad: {self.edad} Dirección: {self.direccion}\tTelefono: {self.telefono}"

# * Creación Personas
personas : dict = {
    "Antonio" : Persona("Antonio",23,"Calle Las Flores",657656565),
    "María" : Persona("María",19,"Calle Playamar",987656565),
    "Carlos" : Persona("Carlos",16,"Calle Velazquez",645656565),
    "Jorge" : Persona("Jorge",21,"Calle Turmalina",878656565),
    "Raquel" : Persona("Raquel",25,"Calle Torres",981656565)
}   
for nombre in personas:
    print(personas[nombre])