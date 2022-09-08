from punto2_Raza import Raza
from punto2_Persona import Persona

class Mascota:
    __ANIO_ACTUAL__ = 2022
    def __init__(self, numRegistro, nombre, raza, anioNacimiento, amo):
        self.numRegistro = numRegistro
        self.nombre = nombre
        self.raza = raza
        self.anioNacimiento = anioNacimiento
        self.amo = amo
    def __str__(self):
        return "Numero de registro: %d\nNombre: %s\nRaza: %s\nAnio de Nacimiento: %d\nAmo: %s" % (self.numRegistro, self.nombre, self.raza, self.anioNacimiento, self.amo)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Mascota):
            return (self.numRegistro == o.numRegistro)

        return False

    @property
    def edad(self):
        return (self.__ANIO_ACTUAL__ - self.anioNacimiento)