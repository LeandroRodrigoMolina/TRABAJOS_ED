class Autor:
    def __init__(self, apellido, nombre):
        self.apellido = apellido
        self.nombre = nombre

    def __str__(self):
        return "%s %s"%(self.apellido, self.nombre)

    def __eq__(self, o):
        if isinstance(o, Autor):
                return (self.apellido == o.apellido) and (self.nombre == o.nombre)
        
        return False