from archivos import *

from jugadores import *

from clubes import *

from filtros import *

from estadisticas import *

from matrices import *

from mercadoDePases import menu_mercado_de_pases

from historial import menu_historial
from validaciones import leer_entero

def main():
    """
    Inicializa los datos principales del programa.

    Carga los clubes y jugadores usando sus respectivas funciones
    y almacena los datos en variables locales para luego utilizarlos
    en las distintas funcionalidades del sistema.
    """
    aux = True
    liga_argentina = cargar_json("clubesPrimera.json")
    primera_nacional = cargar_json("ClubesPrimeraNacional.json")
    jugadores = cargar_json("jugadores.json")
    clasicos = cargar_json("clasicos.json")
    if liga_argentina is None or primera_nacional is None or jugadores is None or clasicos is None:
        print("No se inicio el programa para evitar perder datos, revise los archivos")
        return

    while aux == True:
        print("\nIngrese una opcion del menu: ")
        print("[0] salir del programa")
        print("[1] ir al menu de jugadores")
        print("[2] ir al menu de clubes")
        print("[3] ir al menu de filtros")
        print("[4] ir al menu de estadisticas")
        print("[5] ir al menu de matrices")
        print("[6] Ir al menú del mercado de pases")
        print("[7] Ir al historial de pases")

        opcion = leer_entero("Ingrese el numero de donde desea acceder: ")

        if opcion == 1:
            menu_jugadores(
                jugadores,
                liga_argentina,
                primera_nacional
            )

        elif opcion == 2:
            menu_clubes(
                liga_argentina,
                primera_nacional,
                jugadores,
                clasicos
            )

        elif opcion == 3:
            menu_filtros(jugadores, liga_argentina, primera_nacional)

        elif opcion == 4:
            menu_estadisticas(jugadores, liga_argentina, primera_nacional)

        elif opcion == 5:
            menu_matrices(
                jugadores,
                liga_argentina,
                primera_nacional
            )
            
        elif opcion == 6:
            menu_mercado_de_pases(
            jugadores,
            liga_argentina,
            primera_nacional
            )

        elif opcion == 7:
            menu_historial()

        elif opcion == 0:
            guardado_liga = guardar_json("clubesPrimera.json", liga_argentina)
            guardado_nacional = guardar_json("ClubesPrimeraNacional.json", primera_nacional)
            guardado_jugadores = guardar_json("jugadores.json", jugadores)
            guardado_clasicos = guardar_json("clasicos.json", clasicos)
            if guardado_liga and guardado_nacional and guardado_jugadores and guardado_clasicos:
                aux = False
            else:
                print("No se guardaron todos los datos, puede volver a intentar salir")

        else:
            print("Ingrese una opción correcta\n")

    print("programa finalizado")


main()
