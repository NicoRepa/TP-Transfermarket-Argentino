from functools import reduce

# --- MÓDULO DE ESTADÍSTICAS ---



def calcular_promedio_edad_por_categoria(lista_jugadores, nombre_categoria):
    """ Funcion para calcular promedio de edad por categoria elegida"""
    cat = nombre_categoria.strip().lower()

   
    jugadores_cat = list(filter(lambda j: cat in j["categoria"].lower(), lista_jugadores))

    if len(jugadores_cat) == 0:
        print("No se encontraron jugadores para esa categoria.")
        return 0

    
    edades = list(map(lambda j: j["edad"], jugadores_cat))
    suma_edades = reduce(lambda a, b: a + b, edades)

    promedio = suma_edades / len(jugadores_cat)
    nombre_real = jugadores_cat[0]["categoria"]

    print(nombre_real, "tiene promedio de edad:", promedio)
    return promedio



def calcular_promedio_edad_por_club(lista_jugadores, nombre_club):
    """ Funcion para calcular promedio de edad por club elegido"""
    club = nombre_club.strip().lower()

    
    jugadores_club = list(filter(lambda j: club in j["club_actual"].lower(), lista_jugadores))

    if len(jugadores_club) == 0:
        print("No se encontraron jugadores para ese club.")
        return 0

   
    edades = list(map(lambda j: j["edad"], jugadores_club))
    suma_edades = reduce(lambda a, b: a + b, edades)

    promedio = suma_edades / len(jugadores_club)
    nombre_real = jugadores_club[0]["club_actual"]

    print(nombre_real, "tiene promedio de edad:", promedio)
    return promedio



def menu_promedios(jugadores):
    """Trae menu para hacer consultas de los promedios"""
    continuar = True
    while continuar:
        print("=" * 45)
        print("CONSULTA DE PROMEDIOS DE EDAD")
        print("=" * 45)
        print(" [0] Salir del menu")
        print(" [1] Promedio por Categoría / Liga")
        print(" [2] Promedio por Club")
        print("=" * 45)

        try:
            opcion = int(input("Elija una opción segun su numero: "))
        except ValueError:
            print("\n Opción no válida.\n")
            continue

        if opcion == 1:
            print(
                "\nCategorías disponibles: 'Liga Profesional' o 'Primera"
                " Nacional'"
            )
            cat = input("Ingrese la categoría a consultar: ").strip()
            calcular_promedio_edad_por_categoria(jugadores, cat)
        elif opcion == 2:
            club = input( "\nIngrese el nombre del club (ej: 'Boca', 'River',"" 'Aldosivi'): ").strip()
            calcular_promedio_edad_por_club(jugadores, club)
        elif opcion == 0:
            continuar = False
        else:
            print("\n Opción no válida.\n")

    print("\n ¡Gracias por utilizar la consulta de promedios!")



def calcular_valor_por_club(lista_jugadores):
    """Calcula el valor total de mercado de la plantilla de un club."""
    club_buscado = (input("Ingrese el nombre del club para calcular su valor: ").strip().lower())

    
    jugadores_club = list(filter(lambda j: club_buscado in j["club_actual"].lower(), lista_jugadores))
    cant = len(jugadores_club)

    if cant > 0:
        
        valores = list(map(lambda j: j["valor_mercado"], jugadores_club))
        suma_valor = reduce(lambda a, b: a + b, valores)

        print("\nSe encontraron", cant, "jugadores para ese club.")
        print(
            "El valor total de la plantilla es:",
            suma_valor,
            "millones de euros.",
        )
        return suma_valor
    else:
        print("\nNo se encontraron jugadores para ese club.")
        return None



def calcular_goleador(jugadores):
    """Calcula el goleador de cada liga"""
    liga_arg = list(filter(lambda j: j["categoria"] == "Liga Profesional", jugadores))
    primera_nac = list(filter(lambda j: j["categoria"] == "Primera Nacional", jugadores))

    print("\n--- MÁXIMOS GOLEADORES ---")

    
    if len(liga_arg) > 0:
        goleador_liga = reduce(lambda a, b: a if a["goles"] >= b["goles"] else b, liga_arg)
        print(
            "Liga Profesional:",
            goleador_liga["nombre"],
            "con",
            goleador_liga["goles"],
            "goles.",
        )
    else:
        print("Liga Profesional: Sin jugadores.")

    
    if len(primera_nac) > 0:
        goleador_pn = reduce(lambda a, b: a if a["goles"] >= b["goles"] else b, primera_nac)
        print(
            "Primera Nacional:",
            goleador_pn["nombre"],
            "con",
            goleador_pn["goles"],
            "goles.",
        )
    else:
        print("Primera Nacional: Sin jugadores.")


def menu_estadisticas(jugadores):
    """Menu para hacer consultas de estadisticas"""
    continuar = True

    while continuar:
        print("=" * 45)
        print("             MENU ESTADISTICAS")
        print("=" * 45)
        print("[0] Salir del menu")
        print("[1] Consultar promedios de edad")
        print("[2] Calcular valor de un club")
        print("[3] Consultar goleador")
        print("=" * 45)

        try:
            opcion = int(input("Elija una opción segun su numero: "))
        except ValueError:
            print("\n Opción no válida.\n")
            continue

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