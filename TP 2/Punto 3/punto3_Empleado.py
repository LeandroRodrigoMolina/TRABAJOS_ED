from punto3_Oficina import Oficina
class Empleado:
    def __init__(self, legajo : int, documento : str, apellido : str, nombre : str, oficina : Oficina):
        self.legajo = legajo
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre
        self.oficina = oficina

    def __str__(self):
        return "Legajo: %s\nDocumento: %s\nApellido: %s\nNombre: %s\n\nOficina:%s" % (self.legajo, self.documento, self.apellido, self.nombre, self.oficina)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Empleado):
            return (self.legajo == o.legajo)
        
        return False

    def __lt__(self, other):
        return self.legajo < other.legajo