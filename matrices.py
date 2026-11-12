#matrices
from clubes import seleccionar_club_por_id, normalizar_nombre_club
from validaciones import leer_entero


def crear_matriz_planteles(jugadores, liga_argentina, primera_nacional):
    """Crea una matriz con los jugadores de un club"""

    club = seleccionar_club_por_id(liga_argentina, primera_nacional)
    if club is None:
        return []

    nombre_club = normalizar_nombre_club(club["club"])
    matriz = []

    matriz.append([
        "Nombre",
        "Posicion",
        "Edad",
        "Valor de Mercado",
        "Goles"])

    for jugador in jugadores:
        if normalizar_nombre_club(jugador["club_actual"]) == nombre_club:

            fila = [
                jugador["nombre"],
                jugador["posicion"],
                jugador["edad"],
                jugador["valor_mercado"],
                jugador["goles"]
            ]

            matriz.append(fila)

    return matriz


def crear_matriz_jugadores(jugadores):
    """Crea una matriz con todos los jugadores de una liga"""

    print("1. Liga Profesional")
    print("2. Primera Nacional")

    opcion = leer_entero("Ingrese la liga que desea consultar: ")

    if opcion == 1:
        categoria_buscada = "liga profesional"

    elif opcion == 2:
        categoria_buscada = "primera nacional"

    else:
        print("Opcion incorrecta")
        return []

    matriz = []

    matriz.append([
        "Nombre",
        "Club",
        "Posicion",
        "Edad",
        "Valor de Mercado",
        "Goles"])

    for jugador in jugadores:
        if jugador["categoria"].lower() == categoria_buscada:

            fila = [
                jugador["nombre"],
                jugador["club_actual"],
                jugador["posicion"],
                jugador["edad"],
                jugador["valor_mercado"],
                jugador["goles"]]

            matriz.append(fila)

    return matriz


def mostrar_matrices(matriz):
    """Muestra una matriz por pantalla"""

    for fila in matriz:

        for elemento in fila:
            print(elemento, end=" | ")

        print()

# Menu de matrices
def menu_matrices(jugadores, liga_argentina, primera_nacional):
    """Menu para mostrar las matrices"""

    continuar = True

    while continuar == True:
        print("="*45)
        print("              MENU MATRICES")
        print("="*45)
        print("[0] Salir del menu")
        print("[1] Mostrar jugadores por liga")
        print("[2] Mostrar plantel de un club")
        print("="*45)

        opcion = leer_entero("Elija una opcion segun su numero: ")

        if opcion == 1:
            matriz = crear_matriz_jugadores(jugadores)
            mostrar_matrices(matriz)

        elif opcion == 2:
            matriz = crear_matriz_planteles(jugadores, liga_argentina, primera_nacional)
            mostrar_matrices(matriz)

        elif opcion == 0:
            continuar = False

        else:
            print("Opción no válida.")

    print("\nVolviendo al menu principal")
