class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "%s"%(self.nombre)

    def __eq__(self, o):
        if isinstance(o, Categoria):
            return (self.nombre == o.nombre)

        return False