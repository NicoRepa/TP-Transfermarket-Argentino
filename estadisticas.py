#estadisticas

def calcular_promedio_edad_por_categoria(lista_jugadores, nombre_categoria):
    """ Funcion para calcular promedio de edad por categoria elegida"""
    contador_edad = 0
    cantidad_jugadores = 0
    nombre_categoria = nombre_categoria.strip().lower()
    nombre_categoria_real = ""
    for jugador in lista_jugadores:  # 'jugador' es directamente el diccionario
        categoria = jugador["categoria"].lower()
        
        if nombre_categoria in categoria:
            contador_edad = contador_edad + jugador["edad"]
            cantidad_jugadores = cantidad_jugadores + 1
            nombre_categoria_real = categoria

    promedio = contador_edad / cantidad_jugadores
    print(f"{nombre_categoria_real} tiene promedio de edad: {promedio}")
    return promedio 

def calcular_promedio_edad_por_club(lista_jugadores, nombre_club):
    """ Funcion para calcular promedio de edad por club elegido"""
    contador_edad = 0
    cantidad_jugadores = 0
    nombre_club = nombre_club.strip().lower()
    nombre_club_real = ""
    for jugador in lista_jugadores:  # 'jugador' es directamente el diccionario
        club_actual = jugador["club_actual"].lower()
        
        if nombre_club in club_actual:
            contador_edad = contador_edad + jugador["edad"]
            cantidad_jugadores = cantidad_jugadores + 1
            nombre_club_real = club_actual

    promedio = contador_edad / cantidad_jugadores
    print(f"{nombre_club_real} tiene promedio de edad: {promedio}")
    return promedio 

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
            calcular_promedio_edad_por_categoria(jugadores, cat)
        elif opcion == 2:
            club = input("\nIngrese el nombre del club (ej: 'Boca', 'River', 'Aldosivi'): ").strip()
            calcular_promedio_edad_por_club(jugadores, club)
        elif opcion == 0:
            continuar = False
        else:
            print("\n Opción no válida.\n")

    print("\n ¡Gracias por utilizar la consulta de promedios!")


def calcular_valor_por_club(lista_jugadores):
    """Calcula el valor total de mercado de la plantilla de un club."""

    suma_valor = 0
    cantidad_jugadores = 0

    club_buscado = input("Ingrese el nombre del club para calcular su valor: ").strip().lower()

    for jugador in lista_jugadores:
        club_actual = jugador["club_actual"].lower()

        if club_buscado in club_actual:
            suma_valor = suma_valor + jugador["valor_mercado"]
            cantidad_jugadores = cantidad_jugadores + 1

    if cantidad_jugadores > 0:
        print(f"\nSe encontraron {cantidad_jugadores} jugadores para ese club.")
        print(f"El valor total de la plantilla es: {suma_valor:.2f} millones de euros.")
        return suma_valor
    else:
        print("\nNo se encontraron jugadores para ese club.")
        return None
def calcular_goleador(jugadores):
    """Calcula el goleador de cada liga"""
    goleador_liga_argentina = ""
    max_goles_liga_argentina = 0
    goleador_primera_nacional = ""
    max_goles_primera_nacional = 0

    for jugador in jugadores:

        if jugador["categoria"] == "Liga Profesional":
            if jugador["goles"] > max_goles_liga_argentina:
                max_goles_liga_argentina = jugador["goles"]
                goleador_liga_argentina = jugador

        elif jugador["categoria"] == "Primera Nacional":
            if jugador["goles"] > max_goles_primera_nacional:
                max_goles_primera_nacional = jugador["goles"]
                goleador_primera_nacional = jugador

    print("\n--- MÁXIMOS GOLEADORES ---")

    if goleador_liga_argentina:
        print(f"Liga Profesional: {goleador_liga_argentina['nombre']} con {goleador_liga_argentina['goles']} goles.")
    else:
        print("Liga Profesional: Sin jugadores.")

    if goleador_primera_nacional:
        print(f"Primera Nacional: {goleador_primera_nacional['nombre']} con {goleador_primera_nacional['goles']} goles.")
    else:
        print("Primera Nacional: Sin jugadores.") 


# Menu de estadisticas
def menu_estadisticas(jugadores):
    """Menu para hacer consultas de estadisticas"""

    continuar = True

    while continuar == True:
        print("="*45)
        print("            MENU ESTADISTICAS")
        print("="*45)
        print("[0] Salir del menu")
        print("[1] Consultar promedios de edad")
        print("[2] Calcular valor de un club")
        print("[3] Consultar goleador")
        print("="*45)

        opcion = int(input("Elija una opción segun su numero: "))

        if opcion == 1:
            menu_promedios(jugadores)

        elif opcion == 2:
            calcular_valor_por_club(jugadores)

        elif opcion == 3:
            calcular_goleador(jugadores)

        elif opcion == 0:
            continuar = False

        else:
            print("\n Opción no válida.\n")

    print("\nVolviendo al menu principal")
