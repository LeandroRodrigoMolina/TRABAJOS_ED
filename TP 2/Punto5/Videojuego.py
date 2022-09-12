from datetime import time
from Empresa import Empresa
from Genero import Genero

class Videojuego():
    def __init__(self, titulo:str, genero:Genero, plataformas:list, descripcion:str, precio:float, empresa_Dev:Empresa, empresa_Distri:Empresa, fecha_Lanzamiento:date, ranking_metacritic:float):
        self.titulo = titulo
        self.genero = genero
        self.plataformas = plataformas
        self.descripcion = descripcion
        self.precio = precio
        self.empresa_Dev = empresa_Dev
        self.empresa_Distri = empresa_Distri
        self.fecha_Lanzamiento = fecha_Lanzamiento

        if(ranking_metacritic > 10 or ranking_metacritic < 0):
            raise ValueError("No se puede asignar valores > 10 o valores < 0")
        else:
            self.__ranking_metacritic = ranking_metacritic

    def __str__(self):
        return "Titulo: %s\nGenero: %s\nPlataformas: %s\nDescripcion: %s\nPrecio: %s\nEmpresa desarrolladora: %s\nEmpresa distribuidora: %s\nFecha de lanzamiento: %s\nRanking metacritic: %s" % (self.titulo, self.genero, self.plataformas, self.descripcion, self.precio, self.empresa_Dev, self.empresa_Distri, self.fecha_Lanzamiento, self.__ranking_metacritic)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Videojuego):
            return (self.titulo == self.titulo)
        
        return False

    @ranking_metacritic.setter
    def ranking_metacritic(self, ranking):
        if(ranking > 10 or ranking < 0):
            raise ValueError("No se puede asignar valores > 10 o valores < 0")
        else:
            self.__ranking_metacritic = ranking