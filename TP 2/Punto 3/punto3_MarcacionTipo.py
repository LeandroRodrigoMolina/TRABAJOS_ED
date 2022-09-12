#Podria ser una enumeracion o asi como esta xd
class MarcacionTipo():
    def __init__(self, entrada, salida):
        self.entrada = entrada
        self.salida = salida

    def __str__(self):
        return "Entrada:%d\nSalida:%d\n" % (self.entrada, self.salida)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, MarcacionTipo):
            return (self.entrada == o.entrada) and (self.salida == o.salida)

        return False