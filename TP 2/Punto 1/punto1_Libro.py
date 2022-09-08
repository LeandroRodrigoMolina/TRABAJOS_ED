from punto1_Autor import Autor
from punto1_Categoria import Categoria
class Libro:
    def __init__(self, num_Inventario, titulo, autor, categoria, anio_publicacion):
        self.num_Inventario = int(num_Inventario)
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.anio_publicacion = int(anio_publicacion)

    def __str__(self):
        return "Numero de inventario: %d\nTitulo: %s\nAutor: %s\nCategoria: %s\nAnio de publicacion: %d"%(self.num_Inventario, self.titulo, self.autor, self.categoria, self.anio_publicacion)


    def __eq__(self, o):
        if isinstance(o, Libro):
            return (self.num_Inventario == o.num_Inventario)

        return False