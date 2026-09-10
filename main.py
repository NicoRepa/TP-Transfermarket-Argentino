from clubes import cargar_clubes
from jugadores import cargar_jugadores
#crud jugadores
def crear_jugador():
    pass
def editar_jugador():
    pass
def eliminar_jugador():
    pass
def buscar_jugador():
    pass
def listar_jugadores():
    pass

#crud clubes
def crear_club():
    """ Registra un nuevo club en la división seleccionada """

    nombre = input("Ingrese el nombre del club: ")

    if nombre == "":
        print("El nombre del club no puede estar vacío.")
        return

    for club in liga_argentina:
        if nombre.lower() == club["club"].lower():
            print("El club ya existe")
            return

    for club in primera_nacional:
        if nombre.lower() == club["club"].lower():
            print("El club ya existe")
            return

    division = input("Ingrese la división (1: Primera División / 2: Primera Nacional): ")

    while division != "1" and division != "2":
        print("División inválida. Ingrese 1 o 2.")
    division = input("Ingrese la división (1: Primera División / 2: Primera Nacional): ")

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
def editar_club():
    """ Permite modificar los datos de un club existente """

    id_buscar = input("Ingrese el ID del club que desea editar: ")

    todos_los_clubes = liga_argentina + primera_nacional

    encontrado = False

    for club in todos_los_clubes:
        if (club["id"]) == id_buscar:
            encontrado = True
            print("Club encontrado:", club["club"])

            print("Nombre:", club["club"])
            print("Valor del plantel:", club["valor_plantel_millones_eur"])
            print("Títulos nacionales:", club["titulos_nacionales"])
            print("Títulos internacionales:", club["titulos_internacionales"])
            print("Copa Libertadores:", club["copa_libertadores"])
            print("Copa Sudamericana:", club["copa_sudamericana"])
            print("Mundial de Clubes/Intercontinental:", club["mundial_de_clubes_intercontinental"])
            print("Títulos totales:", club["titulos_totales"])
            print("Descensos:", club["descensos"])

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

    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "7" and opcion != "8" and opcion != "9":
        print("Opción inválida. Ingrese un número del 1 al 9.")

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
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        club["club"] = nuevo_nombre

    elif opcion == "2":
        nuevo_valor = input("Ingrese el nuevo valor del plantel: ")
        club["valor_plantel_millones_eur"] = nuevo_valor

    elif opcion == "3":
        nuevos_titulos = input("Ingrese los nuevos títulos nacionales: ")
        club["titulos_nacionales"] = nuevos_titulos

    elif opcion == "4":
        nuevos_titulos = input("Ingrese los nuevos títulos internacionales: ")
        club["titulos_internacionales"] = nuevos_titulos

    elif opcion == "5":
        nuevas_libertadores = input("Ingrese la nueva cantidad de Copas Libertadores: ")
        club["copa_libertadores"] = nuevas_libertadores

    elif opcion == "6":
        nuevas_sudamericanas = input("Ingrese la nueva cantidad de Copas Sudamericanas: ")
        club["copa_sudamericana"] = nuevas_sudamericanas

    elif opcion == "7":
        nuevo_mundial = input("Ingrese la nueva cantidad de Mundiales de Clubes/Intercontinentales: ")
        club["mundial_de_clubes_intercontinental"] = nuevo_mundial

    elif opcion == "8":
        nuevos_totales = input("Ingrese la nueva cantidad de títulos totales: ")
        club["titulos_totales"] = nuevos_totales

    elif opcion == "9":
        nuevos_descensos = input("Ingrese la nueva cantidad de descensos: ")
        club["descensos"] = nuevos_descensos

    print("Club modificado correctamente.")

    if encontrado == False:
        print("No se encontró ningún club con ese ID.")

def eliminar_club():
    """ Elimina un club existente de la lista correspondiente """

    id_buscar = input("Ingrese el ID del club que desea eliminar: ")

    todos_los_clubes = liga_argentina + primera_nacional

    encontrado = False

    for club in todos_los_clubes:
        if (club["id"]) == id_buscar:
            encontrado = True
            print("Club encontrado:", club["club"])

            if club in liga_argentina:
                liga_argentina.remove(club)
            else:
                primera_nacional.remove(club)

            print("Club eliminado correctamente.")
            break

    if encontrado == False:
        print("No se encontró ningún club con ese ID.")

def buscar_club():
    """ Busca clubes por nombre utilizando coincidencias parciales """

    termino = input ("Ingrese el nombre del club que desea buscar: ")

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
            print ("No se encontro ningun club")

def listar_clubes():
    """ Muestra por consola todos los clubes de Primera División y Primera Nacional"""
    print ("=== PRIEMRA DIVISION ===")

    for club in liga_argentina:
        print(club ["id"], "-", club ["club"])

    print ("=== PRIMERA NACIONAL ===")

    for club in primera_nacional:
        print(club ["id"], "-", club ["club"])

#filtros
def filtrar_jugadores_por_edad():
    pass
def filtrar_jugadores_por_club():
    pass
def filtrar_jugadores_por_valor():
    pass

#estadisticas
from jugadores import cargar_jugadores

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
        print(f"\n❌ No se encontraron jugadores en la categoría '{nombre_categoria}'.\n")
        return 0.0

    suma_edades = sum(j.get("edad", 0) for j in jugadores_filtrados)
    promedio = suma_edades / len(jugadores_filtrados)

    print(f"\n📊 Promedio de edad en {nombre_categoria.title()}: {round(promedio, 2)} años\n")
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
        print("\n❌ No ingresó ningún nombre de club.\n")
        return 0.0

    # Filtramos usando la clave 'club_actual'
    plantel = [
        j for j in lista_jugadores 
        if nombre_club_limpio in j.get("club_actual", "").lower()
    ]

    if not plantel:
        print(f"\n❌ No se encontraron jugadores para el club '{nombre_club}'.\n")
        return 0.0

    suma_edades = sum(j.get("edad", 0) for j in plantel)
    promedio = suma_edades / len(plantel)

    nombre_club_oficial = plantel[0].get("club_actual", nombre_club)
    print(f"\n📊 Promedio de edad del plantel de '{nombre_club_oficial}': {round(promedio, 2)} años\n")
    return round(promedio, 2)


# --- BUCLE PRINCIPAL DE CONSULTA DE PROMEDIOS ---
if __name__ == "__main__":
    # Carga inicial de datos
    jugadores_totales = cargar_jugadores()
    
    continuar = "s"

    while continuar.lower() == "s":
        print("\n" + "="*45)
        print("      CONSULTA DE PROMEDIOS DE EDAD")
        print("="*45)
        print(" [1] Promedio por Categoría / Liga")
        print(" [2] Promedio por Club")
        print("="*45)

        opcion = input("Elija una opción (1 o 2): ").strip()

        if opcion == "1":
            print("\nCategorías disponibles: 'Liga Profesional' o 'Primera Nacional'")
            cat = input("Ingrese la categoría a consultar: ").strip()
            calcular_promedio_edad_por_liga(jugadores_totales, cat)

        elif opcion == "2":
            club = input("\nIngrese el nombre del club (ej: 'Boca', 'River', 'Aldosivi'): ").strip()
            calcular_promedio_edad_por_club(jugadores_totales, club)

        else:
            print("\n❌ Opción no válida.\n")

        # Pregunta si desea seguir consultando
        continuar = input("¿Desea realizar otra consulta de promedios? (s/n): ").strip()

    print("\n👋 ¡Gracias por utilizar la consulta de promedios!")
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

  
main()
