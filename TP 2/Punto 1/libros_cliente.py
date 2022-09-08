from punto1_Autor import Autor
from punto1_Categoria import Categoria
from punto1_Libro import Libro

def imprimir(libros : list) -> None:
    for libro in libros:
        print("Libro:",libro)
        print()

def filtrar_por_categoria(libros : list, cat : Categoria) -> list:
    libros_categorias = []
    for libro in libros:
        if libro.categoria == cat:
            libros_categorias.append(libro)
    return libros_categorias

def filtrar_por_autor(libros : list, autor : Autor) -> list:
    libros_autores = []
    for libro in libros:
        if libro.autor == autor:
            libros_autores.append(libro)
    return libros_autores

def filtrar_por_anio(libros : list, anio : int) -> list:
    libros_por_anio = []
    for libro in libros:
        if libro.anio_publicacion == anio:
            libros_por_anio.append(libro)
    return libros_por_anio
