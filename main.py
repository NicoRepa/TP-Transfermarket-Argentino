from archivos import *

from jugadores import *

from clubes import *

from filtros import *

from estadisticas import *

from matrices import *

from mercadoDePases import menu_mercado_de_pases

from historial import menu_historial

def main():
    """
    Inicializa los datos principales del programa.

    Carga los clubes y jugadores usando sus respectivas funciones
    y almacena los datos en variables locales para luego utilizarlos
    en las distintas funcionalidades del sistema.
    """
    aux = True
    liga_argentina = cargar_json("clubesPrimera.json")
    primera_nacional = cargar_json("clubesPrimeraNacional.json")
    jugadores = cargar_json("jugadores.json")
    clasicos = cargar_json("clasicos.json")

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
            aux = False
            guardar_json("clubesPrimera.json", liga_argentina)
            guardar_json("clubesPrimeraNacional.json", primera_nacional)
            guardar_json("jugadores.json", jugadores)

        else:
            print("Ingrese una opción correcta\n")

    print("programa finalizado")


main()
