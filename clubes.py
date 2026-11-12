# crud clubes
from validaciones import leer_entero, leer_entero_no_negativo, leer_decimal_no_negativo


def normalizar_nombre_club(nombre):
    """Quita espacios y tildes para comparar nombres de clubes."""
    nombre = nombre.strip().lower()
    nombre = nombre.replace("á", "a").replace("é", "e").replace("í", "i")
    nombre = nombre.replace("ó", "o").replace("ú", "u").replace("ü", "u")
    return nombre


def seleccionar_club_por_id(liga_argentina, primera_nacional):
    """Selecciona un club por su division e ID"""
    division = input("Ingrese la division (1: Liga Profesional / 2: Primera Nacional): ").strip()

    while division != "1" and division != "2":
        print("Division invalida. Ingrese 1 o 2.")
        division = input("Ingrese la division (1: Liga Profesional / 2: Primera Nacional): ").strip()

    if division == "1":
        lista = liga_argentina
    else:
        lista = primera_nacional

    if len(lista) == 0:
        print("No hay clubes registrados en esa division")
        return 

    for club in lista:
        print(club["id"], "-", club["club"])

    id_buscar = input("Ingrese el ID del club: ").strip()

    for club in lista:
        if str(club["id"]) == id_buscar:
            return club

    print("No se encontro ningun club con ese ID en la division seleccionada")
    return 


def crear_club(liga_argentina, primera_nacional):
    """Registra un nuevo club en la división seleccionada"""

    nombre = input("Ingrese el nombre del club: ").strip()

    if nombre == "":
        print("El nombre del club no puede estar vacio")
        return

    # Verificar si el club ya existe en Liga Profesional
    for club in liga_argentina:
        if normalizar_nombre_club(nombre) == normalizar_nombre_club(club["club"]):
            print("El club ya existe")
            return

    # Verificar si el club ya existe en Primera Nacional
    for club in primera_nacional:
        if normalizar_nombre_club(nombre) == normalizar_nombre_club(club["club"]):
            print("El club ya existe")
            return

    division = input("Ingrese la division (1: Liga Profesional / 2: Primera Nacional): ")

    while division != "1" and division != "2":
        print("Division invalida. Ingrese 1 o 2.")

        division = input("Ingrese la división (1: Liga Profesional / 2: Primera Nacional): ")

    if division == "1":
        lista = liga_argentina
    else:
        lista = primera_nacional

    # Generar el ID del nuevo club
    id_nuevo = 1
    for club in lista:
        if club["id"] >= id_nuevo:
            id_nuevo = club["id"] + 1

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
    print("El ultimo ID de la lista es:", lista[-1]["id"])


def editar_club(liga_argentina, primera_nacional, jugadores, clasicos):
    """Permite modificar los datos de un club existente."""

    division = input("Ingrese la division (1: Liga Profesional / 2: Primera Nacional): ")

    while division != "1" and division != "2":
        print("Division invalida.")

        division = input("Ingrese la division (1: Liga Profesional / 2: Primera Nacional): ")

    if division == "1":
        lista = liga_argentina
    else:
        lista = primera_nacional

    id_buscar = input("Ingrese el ID del club que desea editar: ").strip()

    encontrado = False

    for club in lista:

        if str(club["id"]) == id_buscar:

            encontrado = True

            print("Club encontrado:", club["club"])
            print("""Que dato desea modificar?
            1. Nombre
            2. Valor del plantel
            3. Títulos nacionales
            4. Títulos internacionales
            5. Copa Libertadores
            6. Copa Sudamericana
            7. Mundial de Clubes/Intercontinental
            8. Títulos totales
            9. Descensos""")
            opcion = input("Ingrese una opcion: ")

            if opcion == "1":

                nuevo_nombre = input("Ingrese el nuevo nombre del club: ").strip()

                if nuevo_nombre == "":
                    print("El nombre del club no puede estar vacio")
                    return

                # Verificar que el nuevo nombre no exista
                for otro_club in liga_argentina:
                    if otro_club != club:
                        if normalizar_nombre_club(nuevo_nombre) == normalizar_nombre_club(otro_club["club"]):
                            print("Ese nombre de club ya existe")
                            return

                for otro_club in primera_nacional:
                    if otro_club != club:
                        if normalizar_nombre_club(nuevo_nombre) == normalizar_nombre_club(otro_club["club"]):
                            print("Ese nombre de club ya existe")
                            return

                nombre_anterior = normalizar_nombre_club(club["club"])
                club["club"] = nuevo_nombre
                for jugador in jugadores:
                    if normalizar_nombre_club(jugador["club_actual"]) == nombre_anterior:
                        jugador["club_actual"] = nuevo_nombre
                for par in clasicos:
                    if normalizar_nombre_club(par["club1"]) == nombre_anterior:
                        par["club1"] = nuevo_nombre
                    if normalizar_nombre_club(par["club2"]) == nombre_anterior:
                        par["club2"] = nuevo_nombre

            elif opcion == "2":

                nuevo_valor = leer_decimal_no_negativo("Ingrese el nuevo valor del plantel: ")

                if nuevo_valor < 0:
                    print("El valor no puede ser negativo")
                    return

                club["valor_plantel_millones_eur"] = nuevo_valor

            elif opcion == "3":

                nuevos_titulos = leer_entero_no_negativo("Ingrese los nuevos titulos nacionales: ")

                if nuevos_titulos < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["titulos_nacionales"] = nuevos_titulos

            elif opcion == "4":

                nuevos_titulos = leer_entero_no_negativo("Ingrese los nuevos titulos internacionales: ")

                if nuevos_titulos < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["titulos_internacionales"] = nuevos_titulos

            elif opcion == "5":

                nuevas_libertadores = leer_entero_no_negativo("Ingrese la cantidad de Copas Libertadores: ")

                if nuevas_libertadores < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["copa_libertadores"] = nuevas_libertadores

            elif opcion == "6":

                nuevas_sudamericanas = leer_entero_no_negativo("Ingrese la cantidad de Copas Sudamericanas: ")

                if nuevas_sudamericanas < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["copa_sudamericana"] = nuevas_sudamericanas

            elif opcion == "7":

                nuevos_mundiales = leer_entero_no_negativo("Ingrese la cantidad de Mundiales/Intercontinentales: ")

                if nuevos_mundiales < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["mundial_de_clubes_intercontinental"] = nuevos_mundiales

            elif opcion == "8":

                nuevos_totales = leer_entero_no_negativo("Ingrese la cantidad de títulos totales: ")

                if nuevos_totales < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["titulos_totales"] = nuevos_totales

            elif opcion == "9":

                nuevos_descensos = leer_entero_no_negativo("Ingrese la cantidad de descensos: ")

                if nuevos_descensos < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["descensos"] = nuevos_descensos

            else:
                print("Opcion invalida")
                return

            print("Club modificado correctamente")
            break

    if encontrado == False:
        print("No se encontro ningun club con ese ID")


def eliminar_club(liga_argentina, primera_nacional, jugadores, clasicos):
    """Elimina un club existente de la lista correspondiente."""

    division = input("Ingrese la división (1: Liga Profesional / 2: Primera Nacional): ")

    while division != "1" and division != "2":
        print("Division invalida.")

        division = input("Ingrese la division (1: Liga Profesional / 2: Primera Nacional): ")

    if division == "1":
        lista = liga_argentina
    else:
        lista = primera_nacional

    id_buscar = input("Ingrese el ID del club que desea eliminar: ").strip()

    encontrado = False

    for club in lista:

        if str(club["id"]) == id_buscar:

            encontrado = True

            print("Club encontrado:", club["club"])

            for jugador in jugadores:
                if normalizar_nombre_club(jugador["club_actual"]) == normalizar_nombre_club(club["club"]):
                    print("No se puede eliminar un club que tiene jugadores, transfieralos o eliminelos primero")
                    return

            for par in clasicos.copy():
                if par["club1"] == club["club"] or par["club2"] == club["club"]:
                    clasicos.remove(par)

            lista.remove(club)

            print("Club eliminado correctamente")
            break

    if encontrado == False:
        print("No se encontro ningun club con ese ID")


def obtener_clasico_rival(nombre_completo, clasicos):
    """Devuelve el rival del club o None si no hay un clasico registrado"""
    for par in clasicos:
        if par["club1"] == nombre_completo:
            return par["club2"]
        elif par["club2"] == nombre_completo:
            return par["club1"]
    return None


def buscar_clubes(liga_argentina, primera_nacional, clasicos):
    """Busca un club por division e ID y muestra sus datos y su clasico rival"""
    club = seleccionar_club_por_id(liga_argentina, primera_nacional)
    if club is None:
        return

    rival = obtener_clasico_rival(club["club"], clasicos)
    if rival is None:
        rival = "Sin clasico registrado"

    print("\n--- INFORMACIÓN DEL CLUB ---")
    for clave, valor in club.items():
        print(f"{clave}: {valor}")
    print(f"clasico_rival: {rival}")
    print("-" * 30)


def listar_clubes(liga_argentina, primera_nacional, jugadores):
    """Muestra por consola todos los clubes de Liga Profesional y Primera Nacional"""

    print("\n=== LIGA PROFESIONAL ===")

    for club in liga_argentina:

        cantidad = 0
        for jugador in jugadores:
            if normalizar_nombre_club(jugador["club_actual"]) == normalizar_nombre_club(club["club"]):
                cantidad += 1
        print(club["id"], "-", club["club"], "-", cantidad, "jugadores")

    print("\n=== PRIMERA NACIONAL ===")

    for club in primera_nacional:

        cantidad = 0
        for jugador in jugadores:
            if normalizar_nombre_club(jugador["club_actual"]) == normalizar_nombre_club(club["club"]):
                cantidad += 1
        print(club["id"], "-", club["club"], "-", cantidad, "jugadores")


def comparar_clasicos(liga_argentina, primera_nacional, clasicos):
    """Selecciona un club por division e ID y lo compara con su clasico rival"""
    club_1 = seleccionar_club_por_id(liga_argentina, primera_nacional)
    if club_1 is None:
        return

    todos_los_clubes = liga_argentina + primera_nacional

    nombre_rival = obtener_clasico_rival(club_1["club"], clasicos)

    if not nombre_rival:
        print(f"\nEl club '{club_1['club']}' no tiene un clasico registrado en clasicos.json")
        return

    # 3. Buscar el objeto del rival en la lista de clubes
    club_2 = None
    for c in todos_los_clubes:
        if c["club"] == nombre_rival:
            club_2 = c
            break

    if not club_2:
        print(f"\nSe encontro la pareja '{nombre_rival}', pero sus datos no estan cargados en los archivos JSON de clubes")
        return

    # 4. Mostrar la comparacion lado a lado
    print("\n" + "=" * 60)
    print(f" COMPARACIÓN: {club_1['club']}  vs.  {club_2['club']}")
    print("=" * 60)
    
    # Recorremos todas las claves que tienen los diccionarios (id, valor, titulos, etc)
    for clave in club_1.keys():
        val1 = club_1[clave]
        val2 = club_2.get(clave, "N/A")
        
        # Le damos un formato prolijo a la salida
        print(f" • {clave.upper().replace('_', ' ')}:")
        print(f"   - {club_1['club']}: {val1}")
        print(f"   - {club_2['club']}: {val2}")
        
        # Si la clave representa un valor numerico comparable (como titulos o valor de plantel), mostramos quien gana
        if clave != "id" and clave != "club":
            if clave == "descensos" and val1 != val2:
                if val1 < val2:
                    print(f"   --> Menos descensos: {club_1['club']}")
                else:
                    print(f"   --> Menos descensos: {club_2['club']}")
            elif val1 > val2:
                print(f"   --> Vencedor: {club_1['club']}")
            elif val2 > val1:
                print(f"   --> Vencedor: {club_2['club']}")
            else:
                print("   --> Empate")
        print("-" * 60)
# Menu de clubes
def menu_clubes(liga_argentina, primera_nacional, jugadores, clasicos):
    """Menu para hacer consultas de clubes"""

    continuar = True

    while continuar == True:
        print("="*45)
        print("              MENU CLUBES")
        print("="*45)
        print("[0] Salir del menu")
        print("[1] Crear club")
        print("[2] Editar club por ID")
        print("[3] Eliminar club por ID")
        print("[4] Buscar club por ID")
        print("[5] Listar clubes")
        print("[6] Comparar clásicos")
        print("="*45)

        opcion = leer_entero("Elija una opcion segun su numero: ")

        if opcion == 1:
            crear_club(liga_argentina, primera_nacional)

        elif opcion == 2:
            editar_club(liga_argentina, primera_nacional, jugadores, clasicos)

        elif opcion == 3:
            eliminar_club(liga_argentina, primera_nacional, jugadores, clasicos)

        elif opcion == 4:
            buscar_clubes(liga_argentina, primera_nacional, clasicos)

        elif opcion == 5:
            listar_clubes(liga_argentina, primera_nacional, jugadores)

        elif opcion == 6:
            comparar_clasicos(liga_argentina, primera_nacional, clasicos)

        elif opcion == 0:
            continuar = False

        else:
            print("\n Opcion no valida")

    print("\nVolviendo al menu principal")
