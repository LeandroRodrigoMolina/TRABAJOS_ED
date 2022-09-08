class Persona:
    def __init__(self, apellido, nombre, documento):
        self.apellido = apellido
        self.nombre = nombre
        self.documento = documento

    def __str__(self):
        return "%s %s \nDocumento: %s" % (self.apellido, self.nombre, self.documento)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Persona):
            return (self.documento == o.documento)
        
        return False