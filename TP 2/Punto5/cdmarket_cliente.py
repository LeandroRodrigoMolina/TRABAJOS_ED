from Empresa import Empresa
from Genero import Genero
from Videojuego import Videojuego
from Plataforma import Plataforma
from VideojuegosAdmin import VideojuegosAdmin
from datetime import date

genero1 = Genero("Accion")
genero2 = Genero("Aventura")
genero3 = Genero("Arcade")
genero4 = Genero("Mundo abierto")
genero5 = Genero("Deportes")

plataforma1 = Plataforma("Play 2", False)
plataforma2 = Plataforma("Xbox", False)
plataforma3 = Plataforma("PSP", True)
plataforma4 = Plataforma("Wii", False)

lista_plataforma = [plataforma1, plataforma2, plataforma3, plataforma4]

empresa1 = Empresa("Activision")
empresa2 = Empresa("Rockstar")
empresa3 = Empresa("ID Software")
empresa4 = Empresa("Electronic Arts")

fecha1 = date(2000,11,2)
fecha2 = date(1990,4,6)
fecha3 = date(2012,8,22)
fecha4 = date(2005,3,17)

videojuego1 = Videojuego("GTA IV", genero4, lista_plataforma, "Juego con buena historia", 25.36, empresa2, empresa2, fecha1, 9.55)
videojuego2 = Videojuego("COD", genero1, lista_plataforma, "Juegito de tiros", 60.55, empresa1, empresa1, fecha2, 7.05)
videojuego3 = Videojuego("DOOM", genero3, lista_plataforma, "El doom", 0.05, empresa3, empresa3, fecha3, 9.99)
videojuego4 = Videojuego("FIFA 2012", genero5, lista_plataforma, "el futvol", 500.45, empresa4, empresa4, fecha4, 7.00)
videojuego5 = Videojuego("GTA Vice City", genero2, lista_plataforma, "Juegito tipo peli Scarface", 6.99, empresa2, empresa2, fecha2, 8.21)
videojuego6 = Videojuego("FIFA 2016", genero5, lista_plataforma, "el futvol pero en otro año", 6846845.45, empresa4, empresa4, fecha4, 8.12)

videojuegos_admin = VideojuegosAdmin()

videojuegos_admin.agregar(videojuego1)
videojuegos_admin.agregar(videojuego2)
videojuegos_admin.agregar(videojuego3)
videojuegos_admin.agregar(videojuego4)
videojuegos_admin.agregar(videojuego5)
videojuegos_admin.agregar(videojuego6)

lista_filtrado_desarrolladora = VideojuegosAdmin()
lista_filtrado_desarrolladora = videojuegos_admin.filtrar_por_desarrolladora(empresa2)

lista_filtrado_distribuidora = VideojuegosAdmin()
lista_filtrado_distribuidora = videojuegos_admin.filtrar_por_distribuidora(empresa4)

lista_filtrado_genero = VideojuegosAdmin()
lista_filtrado_genero = videojuegos_admin.filtrar_por_genero(genero3)

lista_por_plataforma = VideojuegosAdmin()
lista_por_plataforma = videojuegos_admin.cantidad_por_plataforma()

print("__len__:", videojuegos_admin.__len__())
print("__getitem__:", videojuegos_admin.__getitem__(0))
videojuegos_admin.__delitem__(0)
print("DESPUES DE __delitem__:")
print("__getitem__:", videojuegos_admin.__getitem__(0))
videojuegos_admin.agregar(videojuego1)



print("*"*80)
print("FILTRADO POR DESARROLLADORA Rockstar: ", lista_filtrado_desarrolladora)

print("*"*80)
print("FILTRADO POR DISTRIBUIDORA Electronic Arts: ", lista_filtrado_distribuidora)

print("*"*80)
print("FILTRADO POR GENERO ARCADE: ", lista_filtrado_genero)

print("*"*80)
videojuegos_admin.ordenar_titulo()
print("ORDENADO POR TITULO: ", videojuegos_admin)

print("*"*80)
videojuegos_admin.ordenar_mejores_primero()
print("ORDENADO POR MEJORES PRIMERO: ", videojuegos_admin)

print("*"*80)
print("LISTADO PLATAFORMAS: ", lista_plataforma)
print("CANTIDAD POR PLATAFORMA: ", lista_por_plataforma)