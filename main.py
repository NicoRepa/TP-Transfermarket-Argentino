from clubes import cargar_clubes
from jugadores import cargar_jugadores

#crud jugadores
def crear_jugador(jugadores, liga_argentina, primera_nacional):
    """ Funcion para crear un jugador """
    id=len(jugadores)+1
    nombre_jugador = input("ingrese nombre del jugador: ")
    if nombre_jugador == "":
        print("el nombre no puede estar vacio.")
    edad = int(input("ingrese edad del jugador: "))
    if edad <=16:
        print("el jugador es muy joven para anotarlo.")
    posicion = input("ingrese la posicion donde juega: ")
    club_actual = input("ingrese el club donde esta jugando: ")
    valor_mercado = float(input("ingrese el valor del jugador: "))
    goles = int(input("ingrese la cantidad de goles que tiene: "))
    categoria = ""

    for club in liga_argentina:
        if club_actual.strip().lower() in club["club"].lower():
            categoria = "Liga Profesional"
            club_actual = club["club"]

    if not categoria:
        for club in primera_nacional:
            if club_actual.strip().lower() in club["club"].lower():
                categoria = "Primera Nacional"
                club_actual = club["club"]

    nuevo_jugador = {
        "id": id,
        "nombre": nombre_jugador,
        "edad": edad,
        "posicion": posicion,
        "club_actual": club_actual,
        "valor_mercado": valor_mercado,
        "categoria": categoria,
        "goles": goles
    }
    #print(nuevo_jugador)
    jugadores.append(nuevo_jugador)

def editar_jugador(jugadores, liga_argentina, primera_nacional):
    """Permite modificar los datos de un jugador."""

    nombre_buscar = input("Ingrese el nombre del jugador que desea editar: ")
    jugador_encontrado = None
    for jugador in jugadores:
        if (jugador["nombre"]) == nombre_buscar:
            jugador_encontrado = jugador
    if jugador_encontrado is None:
        print("No se encontró ningún jugador con ese nombre.")
        return

    print("Jugador encontrado:", jugador_encontrado["nombre"])
    print("¿Qué dato desea modificar?")
    print("1. Nombre")
    print("2. Edad")
    print("3. Posición")
    print("4. Club")
    print("5. Valor de mercado")
    print("6. Goles")
    print("Ingrese una opción: ")
    opcion = input(" ingrese la opcion que desea editar: ")

    if opcion == "1":
        jugador_encontrado["nombre"] = input("Ingrese el nuevo nombre: ")

    elif opcion == "2":
        edad = int(input("Ingrese la nueva edad: "))

        if edad <= 16:
            print("La edad debe ser mayor a 16.")
            return

        jugador_encontrado["edad"] = edad

    elif opcion == "3":
        jugador_encontrado["posicion"] = input(
            "Ingrese la nueva posición: "
        )

    elif opcion == "4":
        club_ingresado = input("Ingrese el nuevo club: ").strip()
        categoria = None
        nombre_club = None

        for club in liga_argentina:
            if club_ingresado.lower() == club["club"].lower():
                nombre_club = club["club"]
                categoria = "Liga Profesional"
                break

        if categoria is None:
            for club in primera_nacional:
                if club_ingresado.lower() == club["club"].lower():
                    nombre_club = club["club"]
                    categoria = "Primera Nacional"
                    break

        if categoria is None:
            print("El club no existe.")
            return

        jugador_encontrado["club_actual"] = nombre_club
        jugador_encontrado["categoria"] = categoria

    elif opcion == "5":
        jugador_encontrado["valor_mercado"] = float(
            input("Ingrese el nuevo valor de mercado: ")
        )

    elif opcion == "6":
        jugador_encontrado["goles"] = int(
            input("Ingrese la nueva cantidad de goles: ")
        )

    else:
        print("Opción inválida.")

    print("Jugador modificado correctamente")

def eliminar_jugador(jugadores):
    """Elimina un jugador por su nombre."""
    nombre_buscar = input("Ingrese el nombre del jugador que desea eliminar: ").lower()
    encontrado = False

    for jugador in jugadores:
        if jugador["nombre"].lower() == nombre_buscar:
            print(f"Jugador encontrado: {jugador['nombre']}")
            jugadores.remove(jugador)
            print("Jugador eliminado correctamente.")
            encontrado = True

    if not encontrado:
        print("No se encontró ningún jugador con ese nombre.")

def buscar_jugador(jugadores):
    """Busca un jugador por nombre y muestra sus datos."""
    nombre_buscar = input("Ingrese el nombre del jugador a buscar: ").strip().lower()
    encontrado = False

    for jugador in jugadores:
        # Usamos 'in' para coincidencia parcial (o '==' si piden nombre exacto)
        if nombre_buscar in jugador["nombre"].lower():
            print("\n--- Jugador encontrado ---")
            print(f"ID: {jugador['id']}")
            print(f"Nombre: {jugador['nombre']}")
            print(f"Edad: {jugador['edad']}")
            print(f"Posición: {jugador['posicion']}")
            print(f"Club: {jugador['club_actual']}")
            print(f"Categoría: {jugador['categoria']}")
            print(f"Valor de mercado: {jugador['valor_mercado']}")
            print(f"Goles: {jugador['goles']}")
            print("-" * 25)
            encontrado = True

    if not encontrado:
        print(f"No se encontró ningún jugador con el nombre '{nombre_buscar}'.")
def listar_jugadores(jugadores):
    """Muestra todos los jugadores registrados en el sistema."""
    for jugador in jugadores:
        print(f"ID: {jugador['id']} | {jugador['nombre']} ({jugador['edad']} años)")
        print(f"Posición: {jugador['posicion']} | Club: {jugador['club_actual']} ({jugador['categoria']})")
        print(f"Goles: {jugador['goles']} | Valor: ${jugador['valor_mercado']}M")
        print("-" * 45)
    

# Menu de jugadores
def menu_jugadores(jugadores, liga_argentina, primera_nacional):
    """Menu para acceder a las funciones de jugadores"""

    aux = True

    while aux == True:
        print("\nMENU DE JUGADORES")
        print("[0] Volver al menu principal")
        print("[1] Crear jugador")
        print("[2] Editar jugador")
        print("[3] Eliminar jugador")
        print("[4] Buscar jugador")
        print("[5] Listar jugadores")

        opcion = int(input("Ingrese una opcion segun su numero: "))

        if opcion == 1:
            crear_jugador(jugadores, liga_argentina, primera_nacional)

        elif opcion == 2:
            editar_jugador(jugadores, liga_argentina, primera_nacional)

        elif opcion == 3:
            eliminar_jugador(jugadores)

        elif opcion == 4:
            buscar_jugador(jugadores)

        elif opcion == 5:
            listar_jugadores(jugadores)

        elif opcion == 0:
            aux = False

        else:
            print("Ingrese una opcion correcta")

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

# Menu de clubes
def menu_clubes(liga_argentina, primera_nacional):
    """Menu para hacer consultas de clubes"""

    continuar = True

    while continuar == True:
        print("="*45)
        print("              MENU CLUBES")
        print("="*45)
        print("[0] Salir del menu")
        print("[1] Crear club")
        print("[2] Editar club")
        print("[3] Eliminar club")
        print("[4] Buscar club")
        print("[5] Listar clubes")
        print("="*45)

        opcion = int(input("Elija una opción segun su numero: "))

        if opcion == 1:
            crear_club(liga_argentina, primera_nacional)

        elif opcion == 2:
            editar_club(liga_argentina, primera_nacional)

        elif opcion == 3:
            eliminar_club(liga_argentina, primera_nacional)

        elif opcion == 4:
            buscar_club(liga_argentina, primera_nacional)

        elif opcion == 5:
            listar_clubes(liga_argentina, primera_nacional)

        elif opcion == 0:
            continuar = False

        else:
            print("\n Opción no válida.\n")

    print("\nVolviendo al menu principal")

#filtros
def filtrar_jugadores_por_edad(jugadores):
    pass
def filtrar_jugadores_por_club(jugadores):
    pass
def filtrar_jugadores_por_valor(jugadores):
    pass

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

#matrices
def crear_matriz_planteles():
    pass
def crear_matriz_jugadores():
    pass
def mostrar_matrices():
    pass 

# Menu de matrices
def menu_matrices(jugadores, liga_argentina, primera_nacional):
    """Menu para mostrar las matrices"""

    continuar = True

    while continuar == True:
        print("="*45)
        print("              MENU MATRICES")
        print("="*45)
        print("[0] Salir del menu")
        print("[1] Mostrar matriz de jugadores")
        print("[2] Mostrar matriz de planteles")
        print("="*45)

        opcion = int(input("Elija una opción segun su numero: "))

        if opcion == 1:
            matriz = crear_matriz_jugadores(jugadores)
            mostrar_matrices(matriz)

        elif opcion == 2:
            matriz = crear_matriz_planteles(
                liga_argentina,
                primera_nacional
            )
            mostrar_matrices(matriz)

        elif opcion == 0:
            continuar = False

        else:
            print("\n Opción no válida.\n")

    print("\nVolviendo al menu principal")

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
        print("\nIngrese una opcion del menu: ")
        print("[0] salir del programa")
        print("[1] ir al menu de jugadores")
        print("[2] ir al menu de clubes")
        print("[3] ir al menu de filtros")
        print("[4] ir al menu de estadisticas")
        print("[5] ir al menu de matrices")

        opcion = int(input("ingrese el numero de donde desea acceder: "))

        if opcion == 1:
            menu_jugadores(
                jugadores,
                liga_argentina,
                primera_nacional
            )

        elif opcion == 2:
            menu_clubes(
                liga_argentina,
                primera_nacional
            )

        elif opcion == 3:
            menu_filtros(jugadores)

        elif opcion == 4:
            menu_estadisticas(jugadores)

        elif opcion == 5:
            menu_matrices(
                jugadores,
                liga_argentina,
                primera_nacional
            )

        elif opcion == 0:
            aux = False

        else:
            print("Ingrese una opción correcta.\n")
            print("ingrese una opcion correcta")

    print("programa finalizado")


main()