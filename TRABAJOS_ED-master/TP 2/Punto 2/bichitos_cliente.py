from punto2_Raza import Raza
from punto2_Persona import Persona
from punto2_Mascota import Mascota
from punto2_Especie import Especie

import operator

def imprimir(mascotas : list) -> None:
    for mascota in mascotas:
        print(mascota)
        print()

def filtrar_gerontes(mascotas : list) -> list:
    lista_gerontes = []
    for mascota in mascotas:
        edad_aux = mascota.edad
        if(edad_aux > 13):
            lista_gerontes.append(mascota)

    return lista_gerontes

def filtrar_por_especie(mascotas : list, especie) -> list:
    lista_especie = []
    for mascota in mascotas:
        if(mascota.raza.especie == especie):
            lista_especie.append(mascota)

    return lista_especie

def max_mascotero(mascotas : list) -> Persona:
    cont = 0
    mayor = 0

    for mascota in mascotas:
        persona = mascota.amo
        for i in mascotas:
            if persona == i.amo:
                cont += 1
                persona_AUX = persona
        if (cont > mayor):
            mayor = cont
            mayor_amo = persona_AUX
        cont = 0
    return mayor_amo

persona1 = Persona("Lopeciño", "Juancito", "48524321")
persona2 = Persona("Block", "Walter", "02345847")
persona3 = Persona("Murphy", "Robert P.", "44713575")
persona4 = Persona("Rockwell", "Lew", "202178247")

especie1 = Especie("Canino")
especie2 = Especie("Felino")

raza1 = Raza("Perro", especie1)
raza2 = Raza("Gato", especie2)

mascota1 = Mascota(78, "COSO", raza1, 2000, persona1)
mascota2 = Mascota(50, "CASA", raza2, 1999, persona1)
mascota3 = Mascota(2, "PEPE", raza1, 2018, persona3)
mascota4 = Mascota(20, "JORGE", raza2, 2020, persona4)
mascota3 = Mascota(200, "MASH", raza2, 1999, persona2)
mascota5 = Mascota(12, "ROCCO", raza1, 2021, persona1)
mascota6 = Mascota(9, "LUJAN", raza1, 2012, persona4)

lista = []
lista.append(mascota1)
lista.append(mascota2)
lista.append(mascota3)
lista.append(mascota4)
lista.append(mascota5)
lista.append(mascota6)

lista_gerontes = filtrar_gerontes(lista)
lista_especie = filtrar_por_especie(lista, especie1)
maximo_persona = max_mascotero(lista)

imprimir(lista)

print("*"*80)
print("FILTRADO POR GERONTES: \n", lista_gerontes)

print("*"*80)
print("FILTRADO POR ESPECIE POR CANINO: \n", lista_especie)

print("*"*80)
print("Maximo mascotero:\n", maximo_persona)