#filtros
def filtrar_jugadores_por_edad(jugadores):
    edad_minima = int(input("Ingrese la edad mínima: "))
    edad_maxima = int(input("Ingrese la edad máxima: "))

    encontrados = []

    for jugador in jugadores:
        if jugador["edad"] >= edad_minima and jugador["edad"] <= edad_maxima:
            encontrados.append(jugador)

    if len(encontrados) > 0:
        for jugador in encontrados:
            print(jugador["id"], "-", jugador["nombre"], "-", jugador["edad"], "años")
    else:
        print("No se encontraron jugadores en ese rango de edad.")

    return encontrados
def filtrar_jugadores_por_club(jugadores):
    club_buscado = input("Ingrese el nombre del club: ").strip().lower()

    encontrados = []

    for jugador in jugadores:
        club_actual = jugador["club_actual"].lower()

        if club_buscado in club_actual:
            encontrados.append(jugador)

    if len(encontrados) > 0:
        for jugador in encontrados:
            print(jugador["id"], "-", jugador["nombre"], "-", jugador["club_actual"])
    else:
        print("No se encontraron jugadores para ese club.")

    return encontrados
def filtrar_jugadores_por_valor(jugadores):
    valor_minimo = float(input("Ingrese el valor de mercado mínimo: "))
    valor_maximo = float(input("Ingrese el valor de mercado máximo: "))

    encontrados = []

    for jugador in jugadores:
        if jugador["valor_mercado"] >= valor_minimo and jugador["valor_mercado"] <= valor_maximo:
            encontrados.append(jugador)

    if len(encontrados) > 0:
        for jugador in encontrados:
            print(jugador["id"], "-", jugador["nombre"], "-", jugador["valor_mercado"])
    else:
        print("No se encontraron jugadores en ese rango de valor.")

    return encontrados

# Menu de filtros
def menu_filtros(jugadores):
    """Menu para hacer consultas con filtros"""

    continuar = True

    while continuar == True:
        print("="*45)
        print("              MENU FILTROS")
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
            filtrar_jugadores_por_club(jugadores)

        elif opcion == 3:
            filtrar_jugadores_por_valor(jugadores)

        elif opcion == 0:
            continuar = False

        else:
            print("\n Opción no válida.\n")

    print("\nVolviendo al menu principal")