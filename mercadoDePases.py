from historial import guardar_transferencia


def simular_pase(jugadores, liga_argentina, primera_nacional):
    id_buscar = input("Ingrese el ID del jugador: ").strip()
    jugador_encontrado = None

    for jugador in jugadores:
        if str(jugador["id"]) == id_buscar:
            jugador_encontrado = jugador
            break

    if jugador_encontrado is None:
        print("No se encontró ningún jugador con ese ID.")
        return

    nombre_destino = input(
        "Ingrese el nombre del club de destino: "
    ).strip().lower()

    if nombre_destino == "":
        print("Debe ingresar el nombre de un club.")
        return

    clubes_encontrados = []

    for club in liga_argentina:
        if nombre_destino in club["club"].lower():
            clubes_encontrados.append({
                "club": club["club"],
                "categoria": "Liga Profesional"
            })

    for club in primera_nacional:
        if nombre_destino in club["club"].lower():
            clubes_encontrados.append({
                "club": club["club"],
                "categoria": "Primera Nacional"
            })

    if len(clubes_encontrados) == 0:
        print("No se encontró ningún club con ese nombre.")
        return

    if len(clubes_encontrados) > 1:
        print("Hay varios clubes que coinciden:")

        for club in clubes_encontrados:
            print("-", club["club"])

        print("Escriba un nombre más específico e intente de nuevo.")
        return

    club_destino = clubes_encontrados[0]["club"]
    categoria_destino = clubes_encontrados[0]["categoria"]
    club_origen = jugador_encontrado["club_actual"]

    if club_origen.lower() == club_destino.lower():
        print("El jugador ya pertenece a ese club.")
        return

    pase_guardado = guardar_transferencia(
        jugador_encontrado["nombre"],
        club_origen,
        club_destino
    )

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
        print("\n=== MERCADO DE PASES ===")
        print("[0] Volver al menú principal")
        print("[1] Simular un pase")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            simular_pase(jugadores, liga_argentina, primera_nacional)
        elif opcion == "0":
            continuar = False
        else:
            print("Opción inválida.")