import pytest
from estadisticas import (
    calcular_promedio_edad_por_categoria,
    calcular_promedio_edad_por_club,
    calcular_goleador
)


def test_promedio_edad_por_club_exitoso():
    """Prueba el calculo correcto del promedio de edad de un club con datos validos"""
    jugadores_prueba = [{"nombre": "Jugador A", "edad": 30, "club_actual": "Boca Juniors"}, {"nombre": "Jugador B", "edad": 20, "club_actual": "Boca Juniors"}]
    
    promedio = calcular_promedio_edad_por_club(jugadores_prueba, "Boca Juniors")
    assert promedio == 25.0


def test_promedio_edad_club_inexistente():
    """Prueba el comportamiento cuando se consulta por un club que no esta registrado"""
    jugadores_prueba = [{"nombre": "Jugador A", "edad": 28, "club_actual": "River Plate"}]

    promedio = calcular_promedio_edad_por_club(jugadores_prueba, "Boca Juniors")
    assert promedio == 0.0


def test_promedio_edad_por_categoria():
    """Prueba el calculo del promedio de edad filtrando por categoria"""
    jugadores_prueba = [{"nombre": "Jugador A", "edad": 22, "categoria": "Liga Profesional"}, {"nombre": "Jugador B", "edad": 26, "categoria": "Liga Profesional"}]

    promedio_liga = calcular_promedio_edad_por_categoria(jugadores_prueba, "Liga Profesional")
    assert promedio_liga == 24.0


def test_casos_borde_lista_vacia():
    """Prueba el comportamiento de las funciones ante una lista sin registros"""
    lista_vacia = []

    assert calcular_promedio_edad_por_club(lista_vacia, "Boca Juniors") == 0.0
    assert calcular_promedio_edad_por_categoria(lista_vacia, "Liga Profesional") == 0.0


def test_calcular_goleador():
    """Prueba que la funcion de calcular goleador procese la lista sin errores"""
    jugadores_prueba = [{"nombre": "Goleador A", "goles": 10, "categoria": "Liga Profesional"}, {"nombre": "Jugador B", "goles": 4, "categoria": "Liga Profesional"}]
    calcular_goleador(jugadores_prueba)