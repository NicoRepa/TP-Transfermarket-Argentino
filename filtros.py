#filtros
from clubes import seleccionar_club_por_id, normalizar_nombre_club


def filtrar_jugadores_por_edad(jugadores):
    edad_minima = int(input("Ingrese la edad minima: "))
    edad_maxima = int(input("Ingrese la edad maxima: "))

    encontrados = []

    for jugador in jugadores:
        if jugador["edad"] >= edad_minima and jugador["edad"] <= edad_maxima:
            encontrados.append(jugador)

    if len(encontrados) > 0:
        for jugador in encontrados:
            print(jugador["id"], "-", jugador["nombre"], "-", jugador["edad"], "años")
    else:
        print("No se encontraron jugadores en ese rango de edad")

    return encontrados
def filtrar_jugadores_por_club(jugadores, liga_argentina, primera_nacional):
    club = seleccionar_club_por_id(liga_argentina, primera_nacional)
    if club is None:
        return []

    nombre_club = normalizar_nombre_club(club["club"])
    encontrados = []

    for jugador in jugadores:
        if normalizar_nombre_club(jugador["club_actual"]) == nombre_club:
            encontrados.append(jugador)

    if len(encontrados) > 0:
        for jugador in encontrados:
            print(jugador["id"], "-", jugador["nombre"], "-", jugador["club_actual"])
    else:
        print("No se encontraron jugadores para ese club")

    return encontrados
def filtrar_jugadores_por_valor(jugadores):
    valor_minimo = float(input("Ingrese el valor de mercado minimo: "))
    valor_maximo = float(input("Ingrese el valor de mercado maximo: "))

    encontrados = []

    for jugador in jugadores:
        if jugador["valor_mercado"] >= valor_minimo and jugador["valor_mercado"] <= valor_maximo:
            encontrados.append(jugador)

    if len(encontrados) > 0:
        for jugador in encontrados:
            print(jugador["id"], "-", jugador["nombre"], "-", jugador["valor_mercado"])
    else:
        print("No se encontraron jugadores en ese rango de valor")

    return encontrados

# Menu de filtros
def menu_filtros(jugadores, liga_argentina, primera_nacional):
    """Menu para hacer consultas con filtros"""

    continuar = True

    while continuar == True:
        print("="*45)
        print("MENU FILTROS")
        print("="*45)
        print("[0] Salir del menu")
        print("[1] Filtrar jugadores por edad")
        print("[2] Filtrar jugadores por club")
        print("[3] Filtrar jugadores por valor")
        print("="*45)

        opcion = int(input("Elija una opción segun su numero: "))

        if opcion == 1:
            filtrar_jugadores_por_edad(jugadores)

        elif opcion == 2:
            filtrar_jugadores_por_club(jugadores, liga_argentina, primera_nacional)

        elif opcion == 3:
            filtrar_jugadores_por_valor(jugadores)

        elif opcion == 0:
            continuar = False

        else:
            print("\n Opcion no valida")

    print("\nVolviendo al menu principal")
