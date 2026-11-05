import os


def guardar_transferencia(nombre_jugador, club_origen, club_destino):
    ruta = os.path.join(os.path.dirname(__file__), "historial_pases.txt")

    try:
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(
                nombre_jugador + ";" + club_origen + ";" + club_destino + "\n"
            )
    except OSError as error:
        print("No se pudo guardar el pase:", error)
        return False

    return True


def mostrar_historial():
    ruta = os.path.join(os.path.dirname(__file__), "historial_pases.txt")

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            hay_pases = False

            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) == 3:
                    print(datos[0], ":", datos[1], "->", datos[2])
                    hay_pases = True

            if hay_pases == False:
                print("Todavía no hay pases registrados.")

    except FileNotFoundError:
        print("Todavía no hay pases registrados.")
    except OSError as error:
        print("No se pudo leer el historial:", error)

#Menu del Historial

def menu_historial():
    continuar = True

    while continuar:
        print("\n=== HISTORIAL DE PASES ===")
        print("[0] Volver al menú principal")
        print("[1] Ver historial")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            mostrar_historial()
        elif opcion == "0":
            continuar = False
        else:
            print("Opción inválida.")