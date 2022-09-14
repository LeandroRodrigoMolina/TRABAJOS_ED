from datetime import time
from Empresa import Empresa
from Genero import Genero

class Videojuego():
    def __init__(self, titulo:str, genero, plataformas:list, descripcion:str, precio:float, empresa_Dev, empresa_Distri, fecha_Lanzamiento, ranking:float):
        self.titulo = titulo
        self.genero = genero
        self.plataformas = plataformas
        self.descripcion = descripcion
        self.precio = precio
        self.empresa_Dev = empresa_Dev
        self.empresa_Distri = empresa_Distri
        self.fecha_Lanzamiento = fecha_Lanzamiento

        if(ranking > 10 or ranking < 0):
            raise ValueError("No se puede asignar valores > 10 o valores < 0")
        
        self.__rankingMetacritic = ranking

    def __str__(self):
        return "Titulo: %s\nGenero: %s\nPlataformas: %s\nDescripcion: %s\nPrecio: %s\nEmpresa desarrolladora: %s\nEmpresa distribuidora: %s\nFecha de lanzamiento: %s\nRanking metacritic: %s" % (self.titulo, self.genero, self.plataformas, self.descripcion, self.precio, self.empresa_Dev, self.empresa_Distri, self.fecha_Lanzamiento, self.__rankingMetacritic)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Videojuego):
            return (self.titulo == self.titulo)
        
        return False

    @property
    def rankingMetacritic(self):
        return self.__rankingMetacritic
        
    @rankingMetacritic.setter
    def rankingMetacritic(self, ranking):
        if(ranking > 10 or ranking < 0):
            raise ValueError("No se puede asignar valores > 10 o valores < 0")
        else:
            self.__rankingMetacritic = ranking