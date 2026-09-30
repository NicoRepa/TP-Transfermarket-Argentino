# crud clubes

def crear_club(liga_argentina, primera_nacional):
    """Registra un nuevo club en la división seleccionada."""

    nombre = input("Ingrese el nombre del club: ").strip()

    if nombre == "":
        print("El nombre del club no puede estar vacío.")
        return

    # Verificar si el club ya existe en Liga Profesional
    for club in liga_argentina:
        if nombre.lower() == club["club"].lower():
            print("El club ya existe.")
            return

    # Verificar si el club ya existe en Primera Nacional
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

    # Generar el ID del nuevo club
    id_nuevo = len(lista) + 1

    nuevo_club = {
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
    }

    lista.append(nuevo_club)

    print("Club creado correctamente.")
    print("El último ID de la lista es:", lista[-1]["id"])


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

                nuevo_nombre = input(
                    "Ingrese el nuevo nombre del club: "
                ).strip()

                if nuevo_nombre == "":
                    print("El nombre del club no puede estar vacío.")
                    return

                # Verificar que el nuevo nombre no exista
                for otro_club in liga_argentina:
                    if otro_club != club:
                        if nuevo_nombre.lower() == otro_club["club"].lower():
                            print("Ese nombre de club ya existe.")
                            return

                for otro_club in primera_nacional:
                    if otro_club != club:
                        if nuevo_nombre.lower() == otro_club["club"].lower():
                            print("Ese nombre de club ya existe.")
                            return

                club["club"] = nuevo_nombre

            elif opcion == "2":

                nuevo_valor = float(
                    input("Ingrese el nuevo valor del plantel: ")
                )

                if nuevo_valor < 0:
                    print("El valor no puede ser negativo.")
                    return

                club["valor_plantel_millones_eur"] = nuevo_valor

            elif opcion == "3":

                nuevos_titulos = int(
                    input("Ingrese los nuevos títulos nacionales: ")
                )

                if nuevos_titulos < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["titulos_nacionales"] = nuevos_titulos

            elif opcion == "4":

                nuevos_titulos = int(
                    input("Ingrese los nuevos títulos internacionales: ")
                )

                if nuevos_titulos < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["titulos_internacionales"] = nuevos_titulos

            elif opcion == "5":

                nuevas_libertadores = int(
                    input("Ingrese la cantidad de Copas Libertadores: ")
                )

                if nuevas_libertadores < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["copa_libertadores"] = nuevas_libertadores

            elif opcion == "6":

                nuevas_sudamericanas = int(
                    input("Ingrese la cantidad de Copas Sudamericanas: ")
                )

                if nuevas_sudamericanas < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["copa_sudamericana"] = nuevas_sudamericanas

            elif opcion == "7":

                nuevos_mundiales = int(
                    input(
                        "Ingrese la cantidad de Mundiales/Intercontinentales: "
                    )
                )

                if nuevos_mundiales < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["mundial_de_clubes_intercontinental"] = nuevos_mundiales

            elif opcion == "8":

                nuevos_totales = int(
                    input("Ingrese la cantidad de títulos totales: ")
                )

                if nuevos_totales < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["titulos_totales"] = nuevos_totales

            elif opcion == "9":

                nuevos_descensos = int(
                    input("Ingrese la cantidad de descensos: ")
                )

                if nuevos_descensos < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["descensos"] = nuevos_descensos

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

    termino = input(
        "Ingrese el nombre del club que desea buscar: "
    ).strip()

    if termino == "":
        print("Debe ingresar un nombre para realizar la búsqueda.")
        return

    encontrado = False

    for club in liga_argentina:

        if termino.lower() in club["club"].lower():

            print(
                club["id"],
                "-",
                club["club"]
            )

            encontrado = True

    for club in primera_nacional:

        if termino.lower() in club["club"].lower():

            print(
                club["id"],
                "-",
                club["club"]
            )

            encontrado = True

    if encontrado == False:
        print("No se encontró ningún club.")


def listar_clubes(liga_argentina, primera_nacional):
    """Muestra por consola todos los clubes de Liga Profesional y Primera Nacional."""

    print("\n=== LIGA PROFESIONAL ===")

    for club in liga_argentina:

        print(
            club["id"],
            "-",
            club["club"]
        )

    print("\n=== PRIMERA NACIONAL ===")

    for club in primera_nacional:

        print(
            club["id"],
            "-",
            club["club"]
        )
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