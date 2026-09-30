#matrices

def crear_matriz_planteles(jugadores):
    """Crea una matriz con los jugadores de un club"""

    club_buscado = input(
        "Ingrese el nombre del club que desea consultar: "
    ).lower()

    matriz = []

    matriz.append([
        "Nombre",
        "Posicion",
        "Edad",
        "Valor de Mercado",
        "Goles"
    ])

    for jugador in jugadores:
        if club_buscado in jugador["club_actual"].lower():

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

    opcion = int(input("Ingrese la liga que desea consultar: "))

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
        "Goles"
    ])

    for jugador in jugadores:
        if jugador["categoria"].lower() == categoria_buscada:

            fila = [
                jugador["nombre"],
                jugador["club_actual"],
                jugador["posicion"],
                jugador["edad"],
                jugador["valor_mercado"],
                jugador["goles"]
            ]

            matriz.append(fila)

    return matriz


def mostrar_matrices(matriz):
    """Muestra una matriz por pantalla"""

    for fila in matriz:

        for elemento in fila:
            print(elemento, end=" | ")

        print()

# Menu de matrices
def menu_matrices(jugadores):
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

        opcion = int(input("Elija una opción segun su numero: "))

        if opcion == 1:
            matriz = crear_matriz_jugadores(jugadores)
            mostrar_matrices(matriz)

        elif opcion == 2:
            matriz = crear_matriz_planteles(jugadores)
            mostrar_matrices(matriz)

        elif opcion == 0:
            continuar = False

        else:
            print("\n Opción no válida.\n")

    print("\nVolviendo al menu principal")