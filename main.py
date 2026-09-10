from clubes import cargar_clubes
from jugadores import cargar_jugadores
#crud jugadores
def crear_jugador():
    pass
def editar_jugador():
    pass
def eliminar_jugador():
    pass
def buscar_jugador():
    pass
def listar_jugadores():
    pass

#crud clubes
def crear_club():
    pass
def editar_club():
    pass
def eliminar_club():
    pass
def buscar_club():
    pass
def listar_clubes():
    pass

#filtros
def filtrar_jugadores_por_edad():
    pass
def filtrar_jugadores_por_club():
    pass
def filtrar_jugadores_por_valor():
    pass

#estadisticas
from jugadores import cargar_jugadores

def calcular_promedio_edad_por_liga(lista_jugadores, nombre_categoria):
    """
    Calcula el promedio de edad de todos los jugadores según su categoría.
    Parámetros:
        lista_jugadores (list): Lista de diccionarios con la información de los futbolistas.
        nombre_categoria (str): 'Liga Profesional' o 'Primera Nacional'.
    """
    nombre_categoria_limpio = nombre_categoria.strip().lower()

    # Filtramos comparando con la clave 'categoria'
    jugadores_filtrados = [
        j for j in lista_jugadores 
        if j.get("categoria", "").strip().lower() == nombre_categoria_limpio
    ]

    if not jugadores_filtrados:
        print(f"\n❌ No se encontraron jugadores en la categoría '{nombre_categoria}'.\n")
        return 0.0

    suma_edades = sum(j.get("edad", 0) for j in jugadores_filtrados)
    promedio = suma_edades / len(jugadores_filtrados)

    print(f"\n📊 Promedio de edad en {nombre_categoria.title()}: {round(promedio, 2)} años\n")
    return round(promedio, 2)


def calcular_promedio_edad_por_club(lista_jugadores, nombre_club):
    """
    Calcula el promedio de edad de un plantel según el nombre del club.
    Parámetros:
        lista_jugadores (list): Lista de diccionarios con los futbolistas.
        nombre_club (str): Nombre completo o parcial del club a consultar.
    """
    nombre_club_limpio = nombre_club.strip().lower()

    if not nombre_club_limpio:
        print("\n❌ No ingresó ningún nombre de club.\n")
        return 0.0

    # Filtramos usando la clave 'club_actual'
    plantel = [
        j for j in lista_jugadores 
        if nombre_club_limpio in j.get("club_actual", "").lower()
    ]

    if not plantel:
        print(f"\n❌ No se encontraron jugadores para el club '{nombre_club}'.\n")
        return 0.0

    suma_edades = sum(j.get("edad", 0) for j in plantel)
    promedio = suma_edades / len(plantel)

    nombre_club_oficial = plantel[0].get("club_actual", nombre_club)
    print(f"\n📊 Promedio de edad del plantel de '{nombre_club_oficial}': {round(promedio, 2)} años\n")
    return round(promedio, 2)


# --- BUCLE PRINCIPAL DE CONSULTA DE PROMEDIOS ---
if __name__ == "__main__":
    # Carga inicial de datos
    jugadores_totales = cargar_jugadores()
    
    continuar = "s"

    while continuar.lower() == "s":
        print("\n" + "="*45)
        print("      CONSULTA DE PROMEDIOS DE EDAD")
        print("="*45)
        print(" [1] Promedio por Categoría / Liga")
        print(" [2] Promedio por Club")
        print("="*45)

        opcion = input("Elija una opción (1 o 2): ").strip()

        if opcion == "1":
            print("\nCategorías disponibles: 'Liga Profesional' o 'Primera Nacional'")
            cat = input("Ingrese la categoría a consultar: ").strip()
            calcular_promedio_edad_por_liga(jugadores_totales, cat)

        elif opcion == "2":
            club = input("\nIngrese el nombre del club (ej: 'Boca', 'River', 'Aldosivi'): ").strip()
            calcular_promedio_edad_por_club(jugadores_totales, club)

        else:
            print("\n❌ Opción no válida.\n")

        # Pregunta si desea seguir consultando
        continuar = input("¿Desea realizar otra consulta de promedios? (s/n): ").strip()

    print("\n👋 ¡Gracias por utilizar la consulta de promedios!")
def calcular_valor_por_club():
    pass
def calcular_goleador():
    pass

#matrices
def crear_matriz_planteles():
    pass
def crear_matriz_jugadores():
    pass
def mostrar_matrices():
    pass 

def main():
    """
    Inicializa los datos principales del programa.

    Carga los clubes y jugadores usando sus respectivas funciones
    y almacena los datos en variables locales para luego utilizarlos
    en las distintas funcionalidades del sistema.
    """
    liga_argentina, primera_nacional = cargar_clubes()
    jugadores = cargar_jugadores()

  
main()
