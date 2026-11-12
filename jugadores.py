#crud jugadores
from clubes import seleccionar_club_por_id
from validaciones import leer_entero, leer_entero_no_negativo, leer_edad
from validaciones import leer_decimal_no_negativo, leer_texto_no_vacio, leer_nombre_jugador


def obtener_jugador_por_id(jugadores, id_buscar):
    """Busca un jugador por ID y avisa si falta o si el ID esta repetido."""
    jugador_encontrado = None

    for jugador in jugadores:
        if str(jugador["id"]) == str(id_buscar).strip():
            if jugador_encontrado is not None:
                print("Hay mas de un jugador con ese ID, revise los datos")
                return None
            jugador_encontrado = jugador

    if jugador_encontrado is None:
        print("No se encontro ningun jugador con ese ID.")

    return jugador_encontrado


def crear_jugador(jugadores, liga_argentina, primera_nacional):
    """ Funcion para crear un jugador """
    id_nuevo = 1
    for jugador in jugadores:
        if jugador["id"] >= id_nuevo:
            id_nuevo = jugador["id"] + 1
    
    nombre_jugador = leer_nombre_jugador("Ingrese nombre del jugador: ")
    edad = leer_edad("Ingrese edad del jugador: ")
    posicion = leer_texto_no_vacio("Ingrese la posicion donde juega: ")
    
    print("Seleccione el club del jugador:")
    club = seleccionar_club_por_id(liga_argentina, primera_nacional)
    if club is None:
        return

    if club in liga_argentina:
        categoria = "Liga Profesional"
    else:
        categoria = "Primera Nacional"

    valor_mercado = leer_decimal_no_negativo("Ingrese el valor del jugador: ")
    goles = leer_entero_no_negativo("Ingrese la cantidad de goles que tiene: ")

    nuevo_jugador = {
        "id": id_nuevo,
        "nombre": nombre_jugador,
        "edad": edad,
        "posicion": posicion,
        "club_actual": club["club"],
        "valor_mercado": valor_mercado,
        "categoria": categoria,
        "goles": goles
    }
    
    jugadores.append(nuevo_jugador)
    print("¡Jugador creado con éxito!")
    print("ID del jugador:", id_nuevo)

def editar_jugador(jugadores, liga_argentina, primera_nacional):
    """Permite modificar los datos de un jugador."""

    id_buscar = input("Ingrese el ID del jugador que desea editar: ").strip()
    jugador_encontrado = obtener_jugador_por_id(jugadores, id_buscar)
    if jugador_encontrado is None:
        return

    print("Jugador encontrado:", jugador_encontrado["nombre"])
    print("¿Que dato desea modificar?")
    print("1. Nombre")
    print("2. Edad")
    print("3. Posicion")
    print("4. Club")
    print("5. Valor de mercado")
    print("6. Goles")
    print("Ingrese una opcion: ")
    opcion = input("ingrese la opcion que desea editar: ")

    if opcion == "1":
        jugador_encontrado["nombre"] = leer_nombre_jugador("Ingrese el nuevo nombre: ")

    elif opcion == "2":
        edad = leer_edad("Ingrese la nueva edad: ")
        jugador_encontrado["edad"] = edad

    elif opcion == "3":
        jugador_encontrado["posicion"] = leer_texto_no_vacio("Ingrese la nueva posicion: ")

    elif opcion == "4":
        print("Seleccione el nuevo club:")
        club = seleccionar_club_por_id(liga_argentina, primera_nacional)
        if club is None:
            return

        if club in liga_argentina:
            categoria = "Liga Profesional"
        else:
            categoria = "Primera Nacional"

        jugador_encontrado["club_actual"] = club["club"]
        jugador_encontrado["categoria"] = categoria

    elif opcion == "5":
        jugador_encontrado["valor_mercado"] = leer_decimal_no_negativo("Ingrese el nuevo valor de mercado: ")

    elif opcion == "6":
        jugador_encontrado["goles"] = leer_entero_no_negativo("Ingrese la nueva cantidad de goles: ")

    else:
        print("Opción inválida.")
        return

    print("Jugador modificado correctamente")

def eliminar_jugador(jugadores):
    """Elimina un jugador por su ID."""
    id_buscar = input("Ingrese el ID del jugador que desea eliminar: ").strip()
    jugador = obtener_jugador_por_id(jugadores, id_buscar)
    if jugador is None:
        return

    print("Jugador encontrado:", jugador["nombre"])
    jugadores.remove(jugador)
    print("Jugador eliminado correctamente.")

def buscar_jugador(jugadores):
    """Busca un jugador por ID y muestra sus datos."""
    id_buscar = input("Ingrese el ID del jugador a buscar: ").strip()
    jugador = obtener_jugador_por_id(jugadores, id_buscar)
    if jugador is None:
        return

    print("\n--- Jugador encontrado ---")
    print(f"ID: {jugador['id']}")
    print(f"Nombre: {jugador['nombre']}")
    print(f"Edad: {jugador['edad']}")
    print(f"Posición: {jugador['posicion']}")
    print(f"Club: {jugador['club_actual']}")
    print(f"Categoría: {jugador['categoria']}")
    print(f"Valor de mercado: {jugador['valor_mercado']}M")
    print(f"Goles: {jugador['goles']}")
    print("-" * 25)


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
        print("[2] Editar jugador por ID")
        print("[3] Eliminar jugador por ID")
        print("[4] Buscar jugador por ID")
        print("[5] Listar jugadores")

        opcion = leer_entero("Ingrese una opcion segun su numero: ")

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
