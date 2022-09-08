from punto1_Autor import Autor
from punto1_Categoria import Categoria
from punto1_Libro import Libro
from libros_cliente import *
categoria1 = Categoria("PROGRAMACION")
categoria3 = Categoria("Literatura")

autor1 = Autor("Lopecito", "Juanito")
autor2 = Autor("PEPITO", "CARLITO")
autor3 = Autor("Cervantes", "Miguel")

libro1 = Libro(23, "EL LIBRAZO DE JAVA", autor1, categoria1, 1850)
libro2 = Libro(23, "EL LIBRAZO DE JAVA", autor1, categoria1, 1850)
libro3 = Libro(1, "EL TRATADO DE C", autor2, categoria1, 2021)
libro4 = Libro(2, "El quijote quejon", autor3, categoria3, 1605)

print("¿Son iguales?")
print("Libro1 es igual a libro2? ", libro1 == libro2)
print("Libro1 es igual a libro3? ", libro1 == libro3)
print()

libros = [libro1, libro3, libro4]
imprimir(libros)

libros_por_categoria = filtrar_por_categoria(libros, categoria3)
print("Filtrado por categoria:")
imprimir(libros_por_categoria)

libros_por_autores = filtrar_por_autor(libros, autor2)
print("Filtrado por autor:")
imprimir(libros_por_autores)

libros_por_anio = filtrar_por_anio(libros, 1605)
print("Filtrado por anio de publicacion:")
imprimir(libros_por_anio)