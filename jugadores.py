#crud jugadores
def crear_jugador(jugadores, liga_argentina, primera_nacional):
    """ Funcion para crear un jugador """
    id = len(jugadores) + 1
    
    nombre_jugador = input("ingrese nombre del jugador: ")
    while nombre_jugador == "":
        print("el nombre no puede estar vacio.")
        nombre_jugador = input("ingrese nombre del jugador: ")
        
    edad = int(input("ingrese edad del jugador: "))
    while edad < 15 or edad > 45:
        print("La edad debe ser mayor a 15 y menor a 45.")
        edad = int(input("ingrese edad del jugador: "))
        
    posicion = input("ingrese la posicion donde juega: ")
    
    # Pedimos el club inicial fuera del while
    club_actual = input("ingrese el club donde esta jugando: ")
    categoria = ""
    club_oficial = ""

    # Validamos el club dentro del while
    while not categoria:
        # 1. Buscar en Liga Profesional
        for club in liga_argentina:
            if club_actual.strip().lower() in club["club"].lower():
                categoria = "Liga Profesional"
                club_oficial = club["club"]
                break  # Salimos del for al encontrarlo

        # 2. Si no se encontró, buscar en Primera Nacional
        if not categoria:
            for club in primera_nacional:
                if club_actual.strip().lower() in club["club"].lower():
                    categoria = "Primera Nacional"
                    club_oficial = club["club"]
                    break  # Salimos del for al encontrarlo

        # 3. Si no está en ninguna de las dos, pedimos de nuevo
        if not categoria:
            print("ingrese un club que exista en cualquiera de las 2 ligas")
            club_actual = input("ingrese el club donde esta jugando: ")

    # Una vez validado, pedimos los datos que faltaban
    valor_mercado = float(input("ingrese el valor del jugador: "))
    goles = int(input("ingrese la cantidad de goles que tiene: "))

    nuevo_jugador = {
        "id": id,
        "nombre": nombre_jugador,
        "edad": edad,
        "posicion": posicion,
        "club_actual": club_oficial,  # Usamos el nombre oficial limpio
        "valor_mercado": valor_mercado,
        "categoria": categoria,
        "goles": goles
    }
    
    jugadores.append(nuevo_jugador)
    print("¡Jugador creado con éxito!")

def editar_jugador(jugadores, liga_argentina, primera_nacional):
    """Permite modificar los datos de un jugador."""

    id_buscar = input("Ingrese el ID del jugador que desea editar: ")
    jugador_encontrado = None
    for jugador in jugadores:
        if str(jugador["id"]) == id_buscar:
            jugador_encontrado = jugador
    if jugador_encontrado is None:
        print("No se encontró ningún jugador con ese ID.")
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

        if edad < 15 or edad > 45:
            print("La edad debe ser mayor a 15 y menor a 45.")
        

        jugador_encontrado["edad"] = edad

    elif opcion == "3":
        jugador_encontrado["posicion"] = input("Ingrese la nueva posición: ")

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