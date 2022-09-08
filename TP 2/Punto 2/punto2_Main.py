from punto2_Persona import Persona
from punto2_Especie import Especie
from punto2_Raza import Raza
from punto2_Mascota import Mascota

persona1 = Persona("Lopeciño", "Juancito", "48524321")
especie1 = Especie("Jijuajua")
raza1 = Raza("Xaxa", especie1)
mascota1 = Mascota(78, "COSO", raza1, 1892, persona1)

print("Persona:", persona1)
print()
print("Especie:",especie1)
print()
print("Raza:", raza1)
print()
print(mascota1)

print(persona1 == persona1)
print(especie1 == especie1)
print(raza1 == raza1)
print(mascota1 == mascota1)

print()
print(persona1 == False)
print(especie1 == False)
print(raza1 == False)
print(mascota1 == False)

print("Probando __repr__")
print(persona1.__repr__())
print()
print(especie1.__repr__())
print()
print(raza1.__repr__())
print()
print(mascota1.__repr__())

print("Edad del bicho:", mascota1.edad)