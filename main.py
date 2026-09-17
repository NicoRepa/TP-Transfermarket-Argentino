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
    liga_argentina, primera_nacional = cargar_clubes()
    jugadores = cargar_jugadores()
    aux = True
    while aux == True:
        print("Ingrese una opción del menú: \n")
        print("[0] Salir del programa \n")
        print("[1] Ir al menú de promedios \n")
        print("[2] Calcular valor total por club \n")
        
        opcion = input("Ingrese el número de la opción elegida: ").strip()
        
        if opcion == "1":
            menu_promedios(jugadores)
        elif opcion == "2":
            calcular_valor_por_club(jugadores)
        elif opcion == "0":
            aux = False
        else:
            print("Ingrese una opción correcta.\n")

main()