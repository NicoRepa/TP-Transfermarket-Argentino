from cargar_informacion import cargar_clubes_liga_arg, cargar_clubes_primera_nacional, cargar_jugadores

from jugadores import *

from clubes import *

from filtros import *

from estadisticas import *

from matrices import *

def main():
    """
    Inicializa los datos principales del programa.

    Carga los clubes y jugadores usando sus respectivas funciones
    y almacena los datos en variables locales para luego utilizarlos
    en las distintas funcionalidades del sistema.
    """

    primera_nacional = cargar_clubes_primera_nacional()
    liga_argentina = cargar_clubes_liga_arg()
    jugadores = cargar_jugadores()

    aux = True

    while aux == True:
        print("\nIngrese una opcion del menu: ")
        print("[0] salir del programa")
        print("[1] ir al menu de jugadores")
        print("[2] ir al menu de clubes")
        print("[3] ir al menu de filtros")
        print("[4] ir al menu de estadisticas")
        print("[5] ir al menu de matrices")

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
            menu_filtros(jugadores)

        elif opcion == 4:
            menu_estadisticas(jugadores)

        elif opcion == 5:
            menu_matrices(
                jugadores
            )

        elif opcion == 0:
            aux = False

        else:
            print("Ingrese una opción correcta.\n")

    print("programa finalizado")


main()