from clubes import cargar_clubes
from jugadores import cargar_jugadores

#crud jugadores
def crear_jugador(jugadores, liga_argentina, primera_nacional):
    pass
def editar_jugador(jugadores):
    pass
def eliminar_jugador(jugadores):
    pass
def buscar_jugador(jugadores):
    pass
def listar_jugadores(jugadores):
    pass

# crud clubes

def crear_club(liga_argentina, primera_nacional):
    """Registra un nuevo club en la división seleccionada."""

    nombre = input("Ingrese el nombre del club: ")

    if nombre == "":
        print("El nombre del club no puede estar vacío.")
        return

    for club in liga_argentina:
        if nombre.lower() == club["club"].lower():
            print("El club ya existe.")
            return

    for club in primera_nacional:
        if nombre.lower() == club["club"].lower():
            print("El club ya existe.")
            return

    division = input(
        "Ingrese la división (1: Liga Profesional / 2: Primera Nacional): "
    )

    while division != "1" and division != "2":
        print("División inválida. Ingrese 1 o 2.")
        division = input(
            "Ingrese la división (1: Liga Profesional / 2: Primera Nacional): "
        )

    if division == "1":
        lista = liga_argentina
    else:
        lista = primera_nacional

    id_nuevo = len(lista) + 1

    lista.append({
        "id": id_nuevo,
        "club": nombre,
        "valor_plantel_millones_eur": 0,
        "titulos_nacionales": 0,
        "titulos_internacionales": 0,
        "copa_libertadores": 0,
        "copa_sudamericana": 0,
        "mundial_de_clubes_intercontinental": 0,
        "titulos_totales": 0,
        "descensos": 0
    })

    print("Club creado correctamente.")


def editar_club(liga_argentina, primera_nacional):
    """Permite modificar los datos de un club existente."""

    division = input(
        "Ingrese la división (1: Liga Profesional / 2: Primera Nacional): "
    )

    while division != "1" and division != "2":
        print("División inválida.")
        division = input(
            "Ingrese la división (1: Liga Profesional / 2: Primera Nacional): "
        )

    if division == "1":
        lista = liga_argentina
    else:
        lista = primera_nacional

    id_buscar = input("Ingrese el ID del club que desea editar: ")

    encontrado = False

    for club in lista:
        if str(club["id"]) == id_buscar:
            encontrado = True

            print("Club encontrado:", club["club"])

            opcion = input("""
¿Qué dato desea modificar?
1. Nombre
2. Valor del plantel
3. Títulos nacionales
4. Títulos internacionales
5. Copa Libertadores
6. Copa Sudamericana
7. Mundial de Clubes/Intercontinental
8. Títulos totales
9. Descensos
Ingrese una opción: """)

            if opcion == "1":
                club["club"] = input("Ingrese el nuevo nombre: ")

            elif opcion == "2":
                club["valor_plantel_millones_eur"] = float(
                    input("Ingrese el nuevo valor del plantel: ")
                )

            elif opcion == "3":
                club["titulos_nacionales"] = int(
                    input("Ingrese los nuevos títulos nacionales: ")
                )

            elif opcion == "4":
                club["titulos_internacionales"] = int(
                    input("Ingrese los nuevos títulos internacionales: ")
                )

            elif opcion == "5":
                club["copa_libertadores"] = int(
                    input("Ingrese la cantidad de Copas Libertadores: ")
                )

            elif opcion == "6":
                club["copa_sudamericana"] = int(
                    input("Ingrese la cantidad de Copas Sudamericanas: ")
                )

            elif opcion == "7":
                club["mundial_de_clubes_intercontinental"] = int(
                    input("Ingrese la cantidad de Mundiales/Intercontinentales: ")
                )

            elif opcion == "8":
                club["titulos_totales"] = int(
                    input("Ingrese la cantidad de títulos totales: ")
                )

            elif opcion == "9":
                club["descensos"] = int(
                    input("Ingrese la cantidad de descensos: ")
                )

            else:
                print("Opción inválida.")
                return

            print("Club modificado correctamente.")
            break

    if encontrado == False:
        print("No se encontró ningún club con ese ID.")

def eliminar_club(liga_argentina, primera_nacional):
    """Elimina un club existente de la lista correspondiente."""

    division = input(
        "Ingrese la división (1: Liga Profesional / 2: Primera Nacional): "
    )

    while division != "1" and division != "2":
        print("División inválida.")
        division = input(
            "Ingrese la división (1: Liga Profesional / 2: Primera Nacional): "
        )

    if division == "1":
        lista = liga_argentina
    else:
        lista = primera_nacional

    id_buscar = input("Ingrese el ID del club que desea eliminar: ")

    encontrado = False

    for club in lista:
        if str(club["id"]) == id_buscar:
            encontrado = True

            print("Club encontrado:", club["club"])

            lista.remove(club)

            print("Club eliminado correctamente.")
            break

    if encontrado == False:
        print("No se encontró ningún club con ese ID.")

def buscar_club(liga_argentina, primera_nacional):
    """Busca clubes por nombre utilizando coincidencias parciales."""

    termino = input("Ingrese el nombre del club que desea buscar: ")

    encontrado = False

    for club in liga_argentina:
        if termino.lower() in club["club"].lower():
            print(club["id"], "-", club["club"])
            encontrado = True

    for club in primera_nacional:
        if termino.lower() in club["club"].lower():
            print(club["id"], "-", club["club"])
            encontrado = True

    if encontrado == False:
        print("No se encontró ningún club.")


def listar_clubes(liga_argentina, primera_nacional):
    """Muestra por consola todos los clubes de Liga Profesional y Primera Nacional."""

    print("=== LIGA PROFESIONAL ===")

    for club in liga_argentina:
        print(club["id"], "-", club["club"])

    print("\n=== PRIMERA NACIONAL ===")

    for club in primera_nacional:
        print(club["id"], "-", club["club"])

#filtros
def filtrar_jugadores_por_edad(jugadores):
    pass
def filtrar_jugadores_por_club(jugadores):
    pass
def filtrar_jugadores_por_valor(jugadores):
    pass

#estadisticas

def calcular_promedio_edad_por_liga(lista_jugadores, nombre_categoria):
    """
    Calcula el promedio de edad de todos los jugadores según su categoría.
    Parámetros:
        lista_jugadores (list): Lista de diccionarios con la información de los futbolistas.
        nombre_categoria (str): 'Liga Profesional' o 'Primera Nacional'.
    """
    nombre_categoria_limpio = nombre_categoria.strip().lower()

    # Filtramos comparando con la clave 'categoria'
    jugadores_filtrados = [
        j for j in lista_jugadores 
        if j.get("categoria", "").strip().lower() == nombre_categoria_limpio
    ]

    if not jugadores_filtrados:
        print(f"\n No se encontraron jugadores en la categoría '{nombre_categoria}'.\n")
        return 0.0

    suma_edades = sum(j.get("edad", 0) for j in jugadores_filtrados)
    promedio = suma_edades / len(jugadores_filtrados)

    print(f"\n Promedio de edad en {nombre_categoria.title()}: {round(promedio, 2)} años\n")
    return round(promedio, 2)


def calcular_promedio_edad_por_club(lista_jugadores, nombre_club):
    """
    Calcula el promedio de edad de un plantel según el nombre del club.
    Parámetros:
        lista_jugadores (list): Lista de diccionarios con los futbolistas.
        nombre_club (str): Nombre completo o parcial del club a consultar.
    """
    nombre_club_limpio = nombre_club.strip().lower()

    if not nombre_club_limpio:
        print("\n No ingresó ningún nombre de club.\n")
        return 0.0

    # Filtramos usando la clave 'club_actual'
    plantel = [
        j for j in lista_jugadores 
        if nombre_club_limpio in j.get("club_actual", "").lower()
    ]

    if not plantel:
        print(f"\n No se encontraron jugadores para el club '{nombre_club}'.\n")
        return 0.0

    suma_edades = sum(j.get("edad", 0) for j in plantel)
    promedio = suma_edades / len(plantel)

    nombre_club_oficial = plantel[0].get("club_actual", nombre_club)
    print(f"\n Promedio de edad del plantel de '{nombre_club_oficial}': {round(promedio, 2)} años\n")
    return round(promedio, 2)

# Menu de consulta para promedios
def menu_promedios(jugadores):
    """Trae menu para hacer consultas de los promedios"""
    continuar = True
    while continuar == True:
        print("="*45)
        print("      CONSULTA DE PROMEDIOS DE EDAD")
        print("="*45)
        print(" [0] Salir del menu")
        print(" [1] Promedio por Categoría / Liga")
        print(" [2] Promedio por Club")
        print("="*45)

        opcion = int(input("Elija una opción segun su numero: "))

        if opcion == 1:
            print("\nCategorías disponibles: 'Liga Profesional' o 'Primera Nacional'")
            cat = input("Ingrese la categoría a consultar: ").strip()
            calcular_promedio_edad_por_liga(jugadores, cat)
        elif opcion == 2:
            club = input("\nIngrese el nombre del club (ej: 'Boca', 'River', 'Aldosivi'): ").strip()
            calcular_promedio_edad_por_club(jugadores, club)
        elif opcion == 0:
            continuar = False
        else:
            print("\n Opción no válida.\n")

    print("\n ¡Gracias por utilizar la consulta de promedios!")


def calcular_valor_por_club():
    pass
def calcular_goleador():
    pass

#matrices
def crear_matriz_planteles():
    pass
def crear_matriz_jugadores():
    pass
def mostrar_matrices():
    pass 

def main():
    """
    Inicializa los datos principales del programa.

    Carga los clubes y jugadores usando sus respectivas funciones
    y almacena los datos en variables locales para luego utilizarlos
    en las distintas funcionalidades del sistema.
    """
    liga_argentina, primera_nacional = cargar_clubes()
    jugadores = cargar_jugadores()
    aux = True
    while aux == True:
        print("ingrese una opcion del menu: \n")
        print("[0] salir del programa \n")
        print("[1] ir al menu de promedios \n")
        opcion = int(input("ingrese el numero de donde desea acceder: "))
        if opcion == 1:
            menu_promedios(jugadores)
        elif opcion == 0:
            aux = False
        else:
            print("ingrese una opcion correcta")
  
main()