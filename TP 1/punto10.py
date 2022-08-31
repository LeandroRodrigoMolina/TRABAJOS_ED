personas = []
def pasar_datos_diccionario(datos_trabajo,legajo, apellido, nombre, camisa_talle, zapatos_seguridad):
    datos_trabajo['Legajo'] = legajo
    datos_trabajo['Apellido'] = apellido
    datos_trabajo['Nombre'] = nombre
    datos_trabajo['Talle de la camisa'] = camisa_talle
    datos_trabajo['¿Tiene zapatos de seguridad?'] = zapatos_seguridad
    return datos_trabajo

def cargar_datos():
    datos_trabajo = {}
    print("Ingrese datos de la ropa de trabajo del empleado.")

    legajo = int(input("Ingrese legajo:"))
    apellido = input("Ingrese apellido:")
    nombre = input("Ingrese nombre:")
    camisa_talle = int(input("Ingrese talle de la camisa:"))
    pantalon_talle = int(input("Ingrese talle del pantalon:"))
    zapatos_seguridad = input("¿Tiene zapatos de seguridad? responda con: si/no:")
   
    if(zapatos_seguridad.lower() == "si"):
        zapatos_seguridad = True
        personas.append(pasar_datos_diccionario(datos_trabajo, legajo, apellido, nombre, camisa_talle, zapatos_seguridad))

    elif(zapatos_seguridad.lower() == "no"):
        zapatos_seguridad = False
        personas.append(pasar_datos_diccionario(datos_trabajo, legajo, apellido, nombre, camisa_talle, zapatos_seguridad))

    else:
        print("No es valido el dato ingresado (solo si/no).")
    
def quitar_persona():
    print(personas)
    print("Cantidad de personas en la lista:", len(personas))
    print("¿Que persona quiere eliminar de la lista? ingrese indice:")
    indice = int(input())
    personas.pop(indice)
    print(personas)

def ordenar_legajo():
    personas.sort(key = lambda p: p["Legajo"])

def ordenar_apellido_nombre():
    personas.sort(key = lambda p: p["Apellido"] and p["Nombre"])

def menu():
    i = 0
    print("¡Bienvenido al menu! para ingresar algun metodo ingrese el numero que aparece al lado. Para salir ingrese '-1'")
    print("")
    while(i != -1):
        print("")
        print("1: Cargar dato.\n2: Eliminar dato\n3: Ordenar por legajo.\n4: Ordenar por apellido y nombre.\n5: Mostrar listado de personas.")
        i = int(input("Ingrese numero, para salir ingrese '-1': "))
        if(i == 1):
            cargar_datos()
        elif(i == 2):
            quitar_persona()
        elif(i == 3):
            ordenar_legajo()
        elif(i == 4):
            ordenar_apellido_nombre()
        elif(i == 5):
            print(personas)
        else:
            print("")
            print("*****¡Ingrese un valor valido o '-1' para salir!*****")

menu()