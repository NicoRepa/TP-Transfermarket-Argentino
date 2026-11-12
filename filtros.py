#filtros
from clubes import seleccionar_club_por_id, normalizar_nombre_club
from validaciones import leer_entero, leer_entero_no_negativo, leer_decimal_no_negativo


def filtrar_jugadores_por_edad(jugadores):
    edad_minima = leer_entero_no_negativo("Ingrese la edad minima: ")
    edad_maxima = leer_entero_no_negativo("Ingrese la edad maxima: ")
    while edad_maxima < edad_minima:
        print("La edad maxima no puede ser menor que la minima.")
        edad_maxima = leer_entero_no_negativo("Ingrese la edad maxima: ")

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
    valor_minimo = leer_decimal_no_negativo("Ingrese el valor de mercado minimo: ")
    valor_maximo = leer_decimal_no_negativo("Ingrese el valor de mercado maximo: ")
    while valor_maximo < valor_minimo:
        print("El valor maximo no puede ser menor que el minimo.")
        valor_maximo = leer_decimal_no_negativo("Ingrese el valor de mercado maximo: ")

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

        opcion = leer_entero("Elija una opcion segun su numero: ")

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
