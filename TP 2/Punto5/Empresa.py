class Empresa():
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre

    def __str__(self):
        return "%s" % (self.nombre)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Empresa):
            return (self.nombre == o.nombre)
        
        return False