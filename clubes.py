# crud clubes
import json
import os


def normalizar_nombre_club(nombre):
    """Quita espacios y tildes para comparar nombres de clubes."""
    nombre = nombre.strip().lower()
    nombre = nombre.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ü", "u")
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
        if nombre.lower() == club["club"].lower():
            print("El club ya existe")
            return

    # Verificar si el club ya existe en Primera Nacional
    for club in primera_nacional:
        if nombre.lower() == club["club"].lower():
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


def editar_club(liga_argentina, primera_nacional):
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
            3. Titulos nacionales
            4. Titulos internacionales
            5. Copa Libertadores
            6. Copa Sudamericana
            7. Mundial de Clubes/Intercontinental
            8. Titulos totales
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
                        if nuevo_nombre.lower() == otro_club["club"].lower():
                            print("Ese nombre de club ya existe")
                            return

                for otro_club in primera_nacional:
                    if otro_club != club:
                        if nuevo_nombre.lower() == otro_club["club"].lower():
                            print("Ese nombre de club ya existe")
                            return

                club["club"] = nuevo_nombre

            elif opcion == "2":

                nuevo_valor = float(input("Ingrese el nuevo valor del plantel: "))

                if nuevo_valor < 0:
                    print("El valor no puede ser negativo")
                    return

                club["valor_plantel_millones_eur"] = nuevo_valor

            elif opcion == "3":

                nuevos_titulos = int(input("Ingrese los nuevos titulos nacionales: "))

                if nuevos_titulos < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["titulos_nacionales"] = nuevos_titulos

            elif opcion == "4":

                nuevos_titulos = int(input("Ingrese los nuevos titulos internacionales: "))

                if nuevos_titulos < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["titulos_internacionales"] = nuevos_titulos

            elif opcion == "5":

                nuevas_libertadores = int(input("Ingrese la cantidad de Copas Libertadores: "))

                if nuevas_libertadores < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["copa_libertadores"] = nuevas_libertadores

            elif opcion == "6":

                nuevas_sudamericanas = int(input("Ingrese la cantidad de Copas Sudamericanas: "))

                if nuevas_sudamericanas < 0:
                    print("La cantidad no puede ser negativa.")
                    return

                club["copa_sudamericana"] = nuevas_sudamericanas

            elif opcion == "7":

                nuevos_mundiales = int(input("Ingrese la cantidad de Mundiales/Intercontinentales: "))

                if nuevos_mundiales < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["mundial_de_clubes_intercontinental"] = nuevos_mundiales

            elif opcion == "8":

                nuevos_totales = int(input("Ingrese la cantidad de titulos totales: "))

                if nuevos_totales < 0:
                    print("La cantidad no puede ser negativa")
                    return

                club["titulos_totales"] = nuevos_totales

            elif opcion == "9":

                nuevos_descensos = int(input("Ingrese la cantidad de descensos: "))

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


def eliminar_club(liga_argentina, primera_nacional):
    """Elimina un club existente de la lista correspondiente"""

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

            lista.remove(club)

            print("Club eliminado correctamente")
            break

    if encontrado == False:
        print("No se encontro ningun club con ese ID")


def buscar_clubes(liga_argentina, primera_nacional):
    """Busca un club por division e ID y muestra sus datos y su clasico rival"""
    club = seleccionar_club_por_id(liga_argentina, primera_nacional)
    if club is None:
        return

    # Función auxiliar para leer clasicos.json y obtener el rival
    def obtener_clasico_rival(nombre_completo):
        directorio = os.path.dirname(__file__)
        ruta_clasicos = os.path.join(directorio, "clasicos.json")
        try:
            with open(ruta_clasicos, "r", encoding="utf-8") as f:
                lista_clasicos = json.load(f)
            for c in lista_clasicos:
                if c.get("club1") == nombre_completo:
                    return c.get("club2")
                elif c.get("club2") == nombre_completo:
                    return c.get("club1")
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return "Sin clasico registrado"

    rival = obtener_clasico_rival(club["club"])

    print("\n--- INFORMACIÓN DEL CLUB ---")
    for clave, valor in club.items():
        print(f"{clave}: {valor}")
    print(f"clasico_rival: {rival}")
    print("-" * 30)


def listar_clubes(liga_argentina, primera_nacional):
    """Muestra por consola todos los clubes de Liga Profesional y Primera Nacional"""

    print("\n=== LIGA PROFESIONAL ===")

    for club in liga_argentina:

        print(club["id"],"-",club["club"])

    print("\n=== PRIMERA NACIONAL ===")

    for club in primera_nacional:

        print(club["id"],"-",club["club"])
def comparar_clasicos(liga_argentina, primera_nacional):
    """Selecciona un club por division e ID y lo compara con su clasico rival"""
    club_1 = seleccionar_club_por_id(liga_argentina, primera_nacional)
    if club_1 is None:
        return

    todos_los_clubes = liga_argentina + primera_nacional

    # 2. Leer clasicos.json para obtener la pareja/clasico
    directorio = os.path.dirname(__file__)
    ruta_clasicos = os.path.join(directorio, "clasicos.json")
    nombre_rival = None
    
    try:
        with open(ruta_clasicos, "r", encoding="utf-8") as f:
            lista_clasicos = json.load(f)
            
        for par in lista_clasicos:
            if par.get("club1") == club_1["club"]:
                nombre_rival = par.get("club2")
                break
            elif par.get("club2") == club_1["club"]:
                nombre_rival = par.get("club1")
                break
    except (FileNotFoundError, json.JSONDecodeError):
        pass

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
    print(f" COMPARACION: {club_1['club']}  vs  {club_2['club']}")
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
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)) and clave != "id":
            if val1 > val2:
                print(f"   --> Vencedor: {club_1['club']}")
            elif val2 > val1:
                print(f"   --> Vencedor: {club_2['club']}")
            else:
                print("   --> Empate")
        print("-" * 60)
# Menu de clubes
def menu_clubes(liga_argentina, primera_nacional):
    """Menu para hacer consultas de clubes"""

    continuar = True

    while continuar == True:
        print("="*45)
        print("MENU CLUBES")
        print("="*45)
        print("[0] Salir del menu")
        print("[1] Crear club")
        print("[2] Editar club por ID")
        print("[3] Eliminar club por ID")
        print("[4] Buscar club por ID")
        print("[5] Listar clubes")
        print("[6] Comparar clasicos")
        print("="*45)

        opcion = int(input("Elija una opcion segun su numero: "))

        if opcion == 1:
            crear_club(liga_argentina, primera_nacional)

        elif opcion == 2:
            editar_club(liga_argentina, primera_nacional)

        elif opcion == 3:
            eliminar_club(liga_argentina, primera_nacional)

        elif opcion == 4:
            buscar_clubes(liga_argentina, primera_nacional)

        elif opcion == 5:
            listar_clubes(liga_argentina, primera_nacional)

        elif opcion == 6:
            comparar_clasicos(liga_argentina, primera_nacional)

        elif opcion == 0:
            continuar = False

        else:
            print("\n Opcion no valida")

    print("\nVolviendo al menu principal")
