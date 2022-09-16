from datetime import datetime
from punto3_Empleado import Empleado
from punto3_MarcacionTipo import MarcacionTipo

class Marcacion():
    contador_instancias = 1;
    def __init__(self, empleado : Empleado, fecha_Hora : datetime, tipo: MarcacionTipo):
        self.__numRegistro = Marcacion.contador_instancias
        self.empleado = empleado
        self.fecha_Hora = fecha_Hora
        self.tipo = tipo

        Marcacion.contador_instancias = Marcacion.contador_instancias  + 1;

    @property
    def numRegistro(self):
        return self.__numRegistro

    @numRegistro.setter
    def numRegistro(self, a):
        raise ValueError("NO SE PUEDE.")
        
    def __str__(self):
        return "Numero registro: %d\n\nEmpleado:\n%s\nFecha y hora: %s\nTipo: %s" % (self.__numRegistro, self.empleado, self.fecha_Hora, self.tipo)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Marcacion):
            return (self.__numRegistro == o.__numRegistro)

        return False

    