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
def calcular_promedio_edad_por_liga():
    pass
def calcular_promedio_edad_por_club():
    pass
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