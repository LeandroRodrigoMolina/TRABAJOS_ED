from punto2_Especie import Especie

class Raza:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def __str__(self):
        return "%s \nEspecie: %s" % (self.nombre, self.especie)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Raza):
            return (self.nombre == o.nombre) and (self.especie == o.especie)
        
        return False