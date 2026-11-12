from historial import guardar_transferencia
from clubes import seleccionar_club_por_id, normalizar_nombre_club
from jugadores import obtener_jugador_por_id


def simular_pase(jugadores, liga_argentina, primera_nacional):
    id_buscar = input("Ingrese el ID del jugador: ").strip()
    jugador_encontrado = obtener_jugador_por_id(jugadores, id_buscar)
    if jugador_encontrado is None:
        return

    print("Seleccione el club de destino:")
    club = seleccionar_club_por_id(liga_argentina, primera_nacional)
    if club is None:
        return

    club_destino = club["club"]
    if club in liga_argentina:
        categoria_destino = "Liga Profesional"
    else:
        categoria_destino = "Primera Nacional"
    club_origen = jugador_encontrado["club_actual"]

    if normalizar_nombre_club(club_origen) == normalizar_nombre_club(club_destino):
        print("El jugador ya pertenece a ese club.")
        return

    pase_guardado = guardar_transferencia(jugador_encontrado["nombre"],club_origen,club_destino)

    if pase_guardado == False:
        print("No se realizó el pase porque no se pudo guardar el historial.")
        return

    jugador_encontrado["club_actual"] = club_destino
    jugador_encontrado["categoria"] = categoria_destino

    print("Pase realizado correctamente.")
    print(jugador_encontrado["nombre"], "ahora juega en", club_destino)

#Menu del Mercado De Pases

def menu_mercado_de_pases(jugadores, liga_argentina, primera_nacional):
    continuar = True

    while continuar:
        print("=== MERCADO DE PASES ===")
        print("[0] Volver al menú principal")
        print("[1] Simular un pase")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            simular_pase(jugadores, liga_argentina, primera_nacional)
        elif opcion == "0":
            continuar = False
        else:
            print("Opción inválida")
