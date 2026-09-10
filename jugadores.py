def cargar_jugadores():
    """
    Carga la información inicial de los jugadores del sistema.

    Cada jugador se representa mediante un diccionario que contiene
    su id, nombre, edad, posición, club actual, valor de mercado,
    categoría y cantidad de goles.

    Devuelve:
        jugadores: lista de diccionarios con todos los jugadores cargados.
    """
    jugadores = [
        {
            "id": 1,
            "nombre": "Lucas Acosta",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 2,
            "nombre": "Elías López",
            "edad": 26,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.225,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 3,
            "nombre": "Néstor Breitenbruch",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.25,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 4,
            "nombre": "Joaquín Pombo",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.3,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 5,
            "nombre": "Mateo Vales",
            "edad": 19,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 6,
            "nombre": "Martín García",
            "edad": 21,
            "posicion": "Mediocentro",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.075,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 7,
            "nombre": "Bautista Dadín",
            "edad": 20,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.25,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 8,
            "nombre": "Nicolás Gaitán",
            "edad": 38,
            "posicion": "Mediocentro ofensivo",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.102,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 9,
            "nombre": "Lucas Castro",
            "edad": 37,
            "posicion": "Mediocentro ofensivo",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.125,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 10,
            "nombre": "Felipe Anso",
            "edad": 19,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 0.05,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 11,
            "nombre": "Andrés Vombergar",
            "edad": 31,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Aldosivi",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 12,
            "nombre": "Brayan Cortés",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 13,
            "nombre": "Kevin Coronel",
            "edad": 22,
            "posicion": "Lateral derecho",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 1.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 14,
            "nombre": "Francisco Álvarez",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 15,
            "nombre": "Franco Vázquez",
            "edad": 21,
            "posicion": "Defensa central",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 16,
            "nombre": "Sebastián Prieto",
            "edad": 33,
            "posicion": "Lateral izquierdo",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 17,
            "nombre": "Emiliano Viveros",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 18,
            "nombre": "Kevin Gutiérrez",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 19,
            "nombre": "Nicolás Oroz",
            "edad": 32,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 20,
            "nombre": "Hernán López Muñoz",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 21,
            "nombre": "Gastón Verón",
            "edad": 25,
            "posicion": "Delantero",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 22,
            "nombre": "Tomás Molina",
            "edad": 31,
            "posicion": "Delantero centro",
            "club_actual": "Asociación Atlética Argentinos Juniors",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 23,
            "nombre": "Diego Rodríguez",
            "edad": 37,
            "posicion": "Portero",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.35,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 24,
            "nombre": "Santiago López",
            "edad": 23,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 25,
            "nombre": "Renzo Malanca",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 26,
            "nombre": "Brandon Oviedo",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 27,
            "nombre": "Nicolás Meriano",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 28,
            "nombre": "Lautaro Cano",
            "edad": 22,
            "posicion": "Lateral",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 29,
            "nombre": "Ignacio Pais",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 30,
            "nombre": "Tomás Adoryán",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 31,
            "nombre": "Lisandro Piñero",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 32,
            "nombre": "Matías Hernández",
            "edad": 20,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 33,
            "nombre": "Alexander Machado",
            "edad": 24,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Banfield",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 34,
            "nombre": "Marcelo Miño",
            "edad": 28,
            "posicion": "Portero",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 35,
            "nombre": "Nicolás Demartini",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 36,
            "nombre": "Yonatthan Rak",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 37,
            "nombre": "Kevin Jappert",
            "edad": 21,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 38,
            "nombre": "Elías Pereyra",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 39,
            "nombre": "Damián Martínez",
            "edad": 36,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 0.35,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 40,
            "nombre": "Iván Tapia",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 41,
            "nombre": "Dardo Miloc",
            "edad": 35,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 42,
            "nombre": "Tomás Porra",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 43,
            "nombre": "Gonzalo Maroni",
            "edad": 27,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 1.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 44,
            "nombre": "Norberto Briasco",
            "edad": 30,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Barracas Central",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 45,
            "nombre": "Alan Aguerre",
            "edad": 35,
            "posicion": "Portero",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 46,
            "nombre": "Santiago Moyano",
            "edad": 28,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 47,
            "nombre": "Alejandro Maciel",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.9,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 48,
            "nombre": "Facundo Mansilla",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 49,
            "nombre": "Darío Cáceres",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 50,
            "nombre": "Fernando Juárez",
            "edad": 28,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 51,
            "nombre": "Marco Iacobellis",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 52,
            "nombre": "Juan Cardozo",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 53,
            "nombre": "Michael Santos",
            "edad": 33,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 54,
            "nombre": "Horacio Tijanovich",
            "edad": 30,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 55,
            "nombre": "Lucas Varaldo",
            "edad": 24,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Central Córdoba (Santiago del Estero)",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 56,
            "nombre": "Matías Borgogno",
            "edad": 27,
            "posicion": "Portero",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 57,
            "nombre": "Valentín Loza",
            "edad": 19,
            "posicion": "Defensor",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 58,
            "nombre": "Damián Fernández",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 59,
            "nombre": "Héctor Martínez",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 60,
            "nombre": "Fernando Román",
            "edad": 32,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 61,
            "nombre": "Santiago Sosa",
            "edad": 27,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 62,
            "nombre": "César Pérez",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 63,
            "nombre": "David Barbona",
            "edad": 31,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 64,
            "nombre": "Juan Gutiérrez",
            "edad": 24,
            "posicion": "Delantero",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 65,
            "nombre": "Agustín Hausch",
            "edad": 23,
            "posicion": "Delantero",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 66,
            "nombre": "Tiziano Perrotta",
            "edad": 19,
            "posicion": "Delantero",
            "club_actual": "Club Social y Deportivo Defensa y Justicia",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 67,
            "nombre": "Ignacio Arce",
            "edad": 34,
            "posicion": "Portero",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 68,
            "nombre": "Cristian Paz",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 69,
            "nombre": "Nicolás Sansotre",
            "edad": 35,
            "posicion": "Defensor",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.35,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 70,
            "nombre": "Mariano Bracamonte",
            "edad": 25,
            "posicion": "Defensor",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 71,
            "nombre": "Facundo Miño",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 72,
            "nombre": "Ignacio Gariglio",
            "edad": 31,
            "posicion": "Defensor",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 73,
            "nombre": "Milton Céliz",
            "edad": 33,
            "posicion": "Mediocampista",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 74,
            "nombre": "Jonathan Goitía",
            "edad": 31,
            "posicion": "Mediocampista",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 75,
            "nombre": "Brian Sánchez",
            "edad": 32,
            "posicion": "Mediocampista",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 76,
            "nombre": "Nicolás Benegas",
            "edad": 29,
            "posicion": "Delantero centro",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 77,
            "nombre": "Antony Alonso",
            "edad": 27,
            "posicion": "Delantero",
            "club_actual": "Club Deportivo Riestra",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 78,
            "nombre": "Luis Ingolotti",
            "edad": 26,
            "posicion": "Portero",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 79,
            "nombre": "Leonel Di Plácido",
            "edad": 32,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 80,
            "nombre": "Clever Ferreira",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 81,
            "nombre": "Luciano Vallejo",
            "edad": 22,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 82,
            "nombre": "Ignacio Galván",
            "edad": 24,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 83,
            "nombre": "Leonel Vega",
            "edad": 22,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 84,
            "nombre": "Renzo Tesuri",
            "edad": 30,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 85,
            "nombre": "Lautaro Agustín Godoy",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 86,
            "nombre": "Franco Nicola",
            "edad": 24,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 87,
            "nombre": "Nicolás Laméndola",
            "edad": 28,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 88,
            "nombre": "Leandro Díaz",
            "edad": 34,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Tucumán",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 7
        },
        {
            "id": 89,
            "nombre": "Thiago Cardozo",
            "edad": 30,
            "posicion": "Portero",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 90,
            "nombre": "Alcides Benítez",
            "edad": 24,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 91,
            "nombre": "Leonardo Morales",
            "edad": 35,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 0.3,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 92,
            "nombre": "Lisandro López",
            "edad": 37,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 0.2,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 93,
            "nombre": "Adrián Spörle",
            "edad": 31,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 94,
            "nombre": "Emiliano Rigoni",
            "edad": 33,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 95,
            "nombre": "Adrián Sánchez",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 96,
            "nombre": "Franco Vázquez",
            "edad": 37,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 97,
            "nombre": "Juan Velázquez",
            "edad": 22,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 98,
            "nombre": "Lucas Zelarayán",
            "edad": 34,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 99,
            "nombre": "Nicolás Fernández",
            "edad": 30,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Belgrano (Córdoba)",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 100,
            "nombre": "Álvaro Montero",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 101,
            "nombre": "Leandro Lozano",
            "edad": 27,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 102,
            "nombre": "Lautaro Di Lollo",
            "edad": 22,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 103,
            "nombre": "Facundo Herrera",
            "edad": 20,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 104,
            "nombre": "Lautaro Blanco",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 5.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 105,
            "nombre": "Tomás Belmonte",
            "edad": 28,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 3.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 106,
            "nombre": "Leandro Paredes",
            "edad": 32,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 5.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 107,
            "nombre": "Santiago Ascacíbar",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 6.0,
            "categoria": "Liga Profesional",
            "goles": 5
        },
        {
            "id": 108,
            "nombre": "Alan Velasco",
            "edad": 24,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 6.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 109,
            "nombre": "Miguel Merentiel",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 4.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 110,
            "nombre": "Leonel Flores",
            "edad": 19,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Boca Juniors",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 111,
            "nombre": "Fernando Muslera",
            "edad": 40,
            "posicion": "Portero",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 112,
            "nombre": "Eric Meza",
            "edad": 27,
            "posicion": "Lateral derecho",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 113,
            "nombre": "Leandro González Pirez",
            "edad": 34,
            "posicion": "Defensa central",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 114,
            "nombre": "Tomás Palacios",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 6.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 115,
            "nombre": "Gastón Benedetti",
            "edad": 25,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 116,
            "nombre": "Gabriel Neves",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 1.3,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 117,
            "nombre": "Alexis Castro",
            "edad": 32,
            "posicion": "Mediocampista",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 1.8,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 118,
            "nombre": "Baltasar Gallego Rodríguez",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 119,
            "nombre": "Edwuin Cetré",
            "edad": 28,
            "posicion": "Extremo",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 120,
            "nombre": "Brian Aguirre",
            "edad": 23,
            "posicion": "Extremo",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 5.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 121,
            "nombre": "Adolfo Gaich",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Estudiantes de La Plata",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 122,
            "nombre": "Lucas Bruera",
            "edad": 28,
            "posicion": "Portero",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.25,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 123,
            "nombre": "Juan Antonini",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.3,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 124,
            "nombre": "Gonzalo Maffini",
            "edad": 33,
            "posicion": "Defensa central",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 125,
            "nombre": "Matías Valenti",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 126,
            "nombre": "Alejandro Cabrera",
            "edad": 33,
            "posicion": "Mediocampista",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 127,
            "nombre": "Gonzalo González",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 128,
            "nombre": "Siro Rosané",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.35,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 129,
            "nombre": "Gabriel Alanís",
            "edad": 32,
            "posicion": "Mediocampista",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 130,
            "nombre": "Fernando Rodríguez",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.3,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 131,
            "nombre": "Mauro Valiente",
            "edad": 26,
            "posicion": "Delantero",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 132,
            "nombre": "Ibrahim Hesar",
            "edad": 32,
            "posicion": "Delantero",
            "club_actual": "Asociación Atlética Estudiantes (Río Cuarto)",
            "valor_mercado": 0.25,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 133,
            "nombre": "Nelson Insfrán",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 134,
            "nombre": "Bautista Barros Schelotto",
            "edad": 26,
            "posicion": "Defensor",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 135,
            "nombre": "Germán Conti",
            "edad": 32,
            "posicion": "Defensa central",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 136,
            "nombre": "Enzo Martínez",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 137,
            "nombre": "Pedro Silva Torrejón",
            "edad": 29,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 138,
            "nombre": "Mateo Seoane",
            "edad": 22,
            "posicion": "Mediocampista",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 139,
            "nombre": "Ignacio Miramón",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 140,
            "nombre": "Ignacio Fernández",
            "edad": 36,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 141,
            "nombre": "Lucas Janson",
            "edad": 32,
            "posicion": "Extremo",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 142,
            "nombre": "Agustín Auzmendi",
            "edad": 29,
            "posicion": "Delantero centro",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 5
        },
        {
            "id": 143,
            "nombre": "Maximiliano Zalazar",
            "edad": 25,
            "posicion": "Delantero",
            "club_actual": "Club de Gimnasia y Esgrima La Plata",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 144,
            "nombre": "César Rigamonti",
            "edad": 39,
            "posicion": "Portero",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.05,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 145,
            "nombre": "Luciano Paredes",
            "edad": 24,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.45,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 146,
            "nombre": "Diego Mondino",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.3,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 147,
            "nombre": "Ezequiel Muñoz",
            "edad": 35,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.075,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 148,
            "nombre": "Matías Recalde",
            "edad": 29,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.15,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 149,
            "nombre": "Fermín Antonini",
            "edad": 29,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.175,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 150,
            "nombre": "Tomás O'Connor",
            "edad": 22,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 151,
            "nombre": "Facundo Lencioni",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 152,
            "nombre": "Esteban Fernández",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.25,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 153,
            "nombre": "Luciano Cingolani",
            "edad": 25,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.075,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 154,
            "nombre": "Ignacio Sabatini",
            "edad": 27,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Mendoza)",
            "valor_mercado": 0.175,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 155,
            "nombre": "Hernán Galíndez",
            "edad": 39,
            "posicion": "Portero",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 0.3,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 156,
            "nombre": "Lucas Blondel",
            "edad": 30,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 157,
            "nombre": "Martín Nervo",
            "edad": 35,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 158,
            "nombre": "Máximo Palazzo",
            "edad": 21,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 159,
            "nombre": "César Ibáñez",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 160,
            "nombre": "Facundo Kalinger",
            "edad": 21,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 0.35,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 161,
            "nombre": "Rodrigo Fernández Cedrés",
            "edad": 30,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 162,
            "nombre": "Facundo Waller",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 1.7,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 163,
            "nombre": "Leonardo Gil",
            "edad": 35,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 0.375,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 164,
            "nombre": "Óscar Cortés",
            "edad": 22,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 165,
            "nombre": "Jordy Caicedo",
            "edad": 28,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Huracán",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 11
        },
        {
            "id": 166,
            "nombre": "Rodrigo Rey",
            "edad": 35,
            "posicion": "Portero",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 167,
            "nombre": "Leonardo Godoy",
            "edad": 31,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 168,
            "nombre": "Juan Miguel Arrayago",
            "edad": 17,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 169,
            "nombre": "Juan Manuel Fedorco",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 170,
            "nombre": "Facundo Zabala",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 171,
            "nombre": "Mateo Pérez Curci",
            "edad": 20,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 172,
            "nombre": "Iván Marcone",
            "edad": 36,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 173,
            "nombre": "Maximiliano Meza",
            "edad": 33,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 174,
            "nombre": "Santiago Montiel",
            "edad": 26,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 175,
            "nombre": "Felipe Tempone",
            "edad": 20,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 176,
            "nombre": "Matías Abaldo",
            "edad": 22,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Independiente",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 5
        },
        {
            "id": 177,
            "nombre": "Nicolás Bolcato",
            "edad": 22,
            "posicion": "Portero",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 178,
            "nombre": "Alejo Osella",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 179,
            "nombre": "Iván Villalba",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 180,
            "nombre": "Leonard Costa",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 1.3,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 181,
            "nombre": "Juan Elordi",
            "edad": 32,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 182,
            "nombre": "Gonzalo Ríos",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 183,
            "nombre": "Tomás Bottari",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 184,
            "nombre": "José Florentín",
            "edad": 30,
            "posicion": "Mediocampista",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 2.7,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 185,
            "nombre": "Matías Fernández",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 186,
            "nombre": "Fabrizio Sartori",
            "edad": 24,
            "posicion": "Delantero",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 9
        },
        {
            "id": 187,
            "nombre": "Álex Arce",
            "edad": 31,
            "posicion": "Delantero centro",
            "club_actual": "Club Sportivo Independiente Rivadavia",
            "valor_mercado": 5.5,
            "categoria": "Liga Profesional",
            "goles": 16
        },
        {
            "id": 188,
            "nombre": "Marcos Ledesma",
            "edad": 30,
            "posicion": "Portero",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 189,
            "nombre": "Giuliano Cerato",
            "edad": 28,
            "posicion": "Lateral derecho",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 190,
            "nombre": "Jonathan Galván",
            "edad": 34,
            "posicion": "Defensa central",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 191,
            "nombre": "Fernando Alarcón",
            "edad": 32,
            "posicion": "Defensa central",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 192,
            "nombre": "Leonel Mosevich",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 193,
            "nombre": "Diego Sosa",
            "edad": 29,
            "posicion": "Lateral izquierdo",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 194,
            "nombre": "Álex Luna",
            "edad": 22,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 6
        },
        {
            "id": 195,
            "nombre": "Gustavo Abregú",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 196,
            "nombre": "Matías Gallardo",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 197,
            "nombre": "Jhon Córdoba",
            "edad": 26,
            "posicion": "Delantero",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 198,
            "nombre": "Matías Tissera",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Instituto Atlético Central Córdoba",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 199,
            "nombre": "Nahuel Losada",
            "edad": 33,
            "posicion": "Portero",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 200,
            "nombre": "Tomás Guidara",
            "edad": 30,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 201,
            "nombre": "Carlos Izquierdoz",
            "edad": 38,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 202,
            "nombre": "José Canale",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 203,
            "nombre": "Sasha Marcich",
            "edad": 28,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 204,
            "nombre": "Felipe Peña Biafore",
            "edad": 25,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 205,
            "nombre": "Agustín Cardozo",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 206,
            "nombre": "Eduardo Salvio",
            "edad": 36,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 207,
            "nombre": "Franco Watson",
            "edad": 24,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 208,
            "nombre": "Lucas Besozzi",
            "edad": 23,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 209,
            "nombre": "Allan Wlk",
            "edad": 23,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Lanús",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 210,
            "nombre": "Josué Reinatti",
            "edad": 23,
            "posicion": "Portero",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 211,
            "nombre": "Martín Ortega",
            "edad": 27,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 212,
            "nombre": "Lautaro Giannetti",
            "edad": 32,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 213,
            "nombre": "Lucas Carrizo",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 214,
            "nombre": "Franco Escobar",
            "edad": 31,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 215,
            "nombre": "Rodrigo Herrera",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 216,
            "nombre": "Luca Regiardo",
            "edad": 20,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 217,
            "nombre": "Facundo Guch",
            "edad": 19,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 218,
            "nombre": "Walter Mazzantti",
            "edad": 30,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 1.3,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 219,
            "nombre": "Santiago Solari",
            "edad": 28,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 220,
            "nombre": "Matías Cóccaro",
            "edad": 29,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Newell's Old Boys",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 6
        },
        {
            "id": 221,
            "nombre": "Juan Pablo Cozzani",
            "edad": 27,
            "posicion": "Portero",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 3.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 222,
            "nombre": "Agustín Lagos",
            "edad": 24,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 223,
            "nombre": "Ignacio Vázquez",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 224,
            "nombre": "Víctor Cuesta",
            "edad": 38,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 0.4,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 225,
            "nombre": "Tomás Silva",
            "edad": 23,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 226,
            "nombre": "Guido Mainero",
            "edad": 31,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 227,
            "nombre": "Pablo Ferreira",
            "edad": 21,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 0.35,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 228,
            "nombre": "Martín Barrios",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 229,
            "nombre": "Gastón Togni",
            "edad": 28,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 230,
            "nombre": "Bruno Sepúlveda",
            "edad": 33,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 0.245,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 231,
            "nombre": "Nicolás Retamar",
            "edad": 27,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Platense",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 232,
            "nombre": "Facundo Cambeses",
            "edad": 29,
            "posicion": "Portero",
            "club_actual": "Racing Club",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 233,
            "nombre": "Ezequiel Cannavo",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Racing Club",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 234,
            "nombre": "Matías Pérez",
            "edad": 21,
            "posicion": "Defensa central",
            "club_actual": "Racing Club",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 235,
            "nombre": "Marcos Rojo",
            "edad": 36,
            "posicion": "Defensa central",
            "club_actual": "Racing Club",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 236,
            "nombre": "Ignacio Rodríguez",
            "edad": 24,
            "posicion": "Lateral izquierdo",
            "club_actual": "Racing Club",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 237,
            "nombre": "Ulises Ortegoza",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Racing Club",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 238,
            "nombre": "Leonel Pérez",
            "edad": 22,
            "posicion": "Mediocampista",
            "club_actual": "Racing Club",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 239,
            "nombre": "Matko Miljevic",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Racing Club",
            "valor_mercado": 5.0,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 240,
            "nombre": "Tomás Conechny",
            "edad": 28,
            "posicion": "Extremo",
            "club_actual": "Racing Club",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 241,
            "nombre": "Adrián Martínez",
            "edad": 34,
            "posicion": "Delantero centro",
            "club_actual": "Racing Club",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 9
        },
        {
            "id": 242,
            "nombre": "Lautaro Díaz",
            "edad": 28,
            "posicion": "Delantero",
            "club_actual": "Racing Club",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 243,
            "nombre": "Santiago Beltrán",
            "edad": 22,
            "posicion": "Portero",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 244,
            "nombre": "Gonzalo Montiel",
            "edad": 29,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 5.0,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 245,
            "nombre": "Lucas Martínez Quarta",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 6.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 246,
            "nombre": "Nicolás Otamendi",
            "edad": 38,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 247,
            "nombre": "Marcos Acuña",
            "edad": 34,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 248,
            "nombre": "Federico Vera",
            "edad": 28,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 3.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 249,
            "nombre": "Tomás Andrada",
            "edad": 21,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 250,
            "nombre": "Thiago Almada",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 25.0,
            "categoria": "Liga Profesional",
            "goles": 5
        },
        {
            "id": 251,
            "nombre": "Tomás Galván",
            "edad": 26,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 252,
            "nombre": "Ángel Correa",
            "edad": 31,
            "posicion": "Delantero",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 10.0,
            "categoria": "Liga Profesional",
            "goles": 7
        },
        {
            "id": 253,
            "nombre": "Sebastián Driussi",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético River Plate",
            "valor_mercado": 8.0,
            "categoria": "Liga Profesional",
            "goles": 7
        },
        {
            "id": 254,
            "nombre": "Jeremías Ledesma",
            "edad": 33,
            "posicion": "Portero",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 255,
            "nombre": "Emanuel Coronel",
            "edad": 29,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 256,
            "nombre": "Ignacio Ovando",
            "edad": 21,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 257,
            "nombre": "Gastón Ávila",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 258,
            "nombre": "Agustín Sández",
            "edad": 25,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 259,
            "nombre": "Franco Ibarra",
            "edad": 25,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 260,
            "nombre": "Vicente Pizarro",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 4.5,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 261,
            "nombre": "Alan Rodríguez",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 262,
            "nombre": "Ángel Di María",
            "edad": 38,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 8
        },
        {
            "id": 263,
            "nombre": "Jaminton Campaz",
            "edad": 26,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 6.0,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 264,
            "nombre": "Enzo Copetti",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Rosario Central",
            "valor_mercado": 3.5,
            "categoria": "Liga Profesional",
            "goles": 5
        },
        {
            "id": 265,
            "nombre": "José Devecchi",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 266,
            "nombre": "Ezequiel Herrera",
            "edad": 22,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 267,
            "nombre": "Danilo Arboleda",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 268,
            "nombre": "Emiliano Amor",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 269,
            "nombre": "Teo Rodríguez Pagano",
            "edad": 19,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 270,
            "nombre": "Manuel Insaurralde",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 271,
            "nombre": "Ignacio Perruzzi",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 272,
            "nombre": "Nicolás Tripichio",
            "edad": 30,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 273,
            "nombre": "Facundo Farías",
            "edad": 24,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 3.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 274,
            "nombre": "Alexis Cuello",
            "edad": 26,
            "posicion": "Delantero",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 7
        },
        {
            "id": 275,
            "nombre": "Rodrigo Auzmendi",
            "edad": 25,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético San Lorenzo de Almagro",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 276,
            "nombre": "Thyago Ayala",
            "edad": 22,
            "posicion": "Portero",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 277,
            "nombre": "Ulises Giménez",
            "edad": 20,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 278,
            "nombre": "Renzo Orihuela",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 279,
            "nombre": "Juan Manuel Insaurralde",
            "edad": 41,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.1,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 280,
            "nombre": "Lucas Suárez",
            "edad": 31,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 281,
            "nombre": "Santiago Salle",
            "edad": 22,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 282,
            "nombre": "Mauricio Martínez",
            "edad": 33,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 283,
            "nombre": "Cristian Zabala",
            "edad": 28,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.6,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 284,
            "nombre": "Julián Mavilla",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 285,
            "nombre": "Jonathan Herrera",
            "edad": 34,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 286,
            "nombre": "Junior Marabel",
            "edad": 28,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Sarmiento (Junín)",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 11
        },
        {
            "id": 287,
            "nombre": "Ezequiel Unsain",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 288,
            "nombre": "Augusto Schott",
            "edad": 26,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 289,
            "nombre": "Matías Catalán",
            "edad": 34,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 290,
            "nombre": "Valentín Fascendini",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 291,
            "nombre": "Gastón Báez",
            "edad": 31,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 0.8,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 292,
            "nombre": "Juan Sforza",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 293,
            "nombre": "Matías Galarza",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 294,
            "nombre": "Valentín Depietri",
            "edad": 25,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 295,
            "nombre": "Franco Cristaldo",
            "edad": 30,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 296,
            "nombre": "Rick",
            "edad": 26,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 3.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 297,
            "nombre": "Agustín Álvarez Martínez",
            "edad": 25,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Talleres (Córdoba)",
            "valor_mercado": 3.5,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 298,
            "nombre": "Felipe Zenobio",
            "edad": 26,
            "posicion": "Portero",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 299,
            "nombre": "Valentín Moreno",
            "edad": 23,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 300,
            "nombre": "Alan Barrionuevo",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 301,
            "nombre": "Joaquín Villalba",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 302,
            "nombre": "Nahuel Banegas",
            "edad": 30,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 303,
            "nombre": "Santiago González",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 304,
            "nombre": "Bruno Leyes",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 305,
            "nombre": "Tomás Serrago",
            "edad": 21,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 306,
            "nombre": "Jabes Saralegui",
            "edad": 23,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 307,
            "nombre": "Santiago López",
            "edad": 22,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 308,
            "nombre": "Ignacio Russo",
            "edad": 25,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Tigre",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 309,
            "nombre": "Matías Mansilla",
            "edad": 30,
            "posicion": "Portero",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 310,
            "nombre": "Lautaro Vargas",
            "edad": 21,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 311,
            "nombre": "Maizon Rodríguez",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 312,
            "nombre": "Juan Pablo Ludueña",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 1.3,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 313,
            "nombre": "Lucas Ayala",
            "edad": 19,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 314,
            "nombre": "Julián Palacios",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 1.2,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 315,
            "nombre": "Lucas Menossi",
            "edad": 34,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 0.7,
            "categoria": "Liga Profesional",
            "goles": 4
        },
        {
            "id": 316,
            "nombre": "Mauro Luna Diale",
            "edad": 27,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 0.45,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 317,
            "nombre": "Emilio Giaccone",
            "edad": 21,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 0.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 318,
            "nombre": "Misael Aguirre",
            "edad": 18,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 0.2,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 319,
            "nombre": "Cristian Tarragona",
            "edad": 35,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Unión (Santa Fe)",
            "valor_mercado": 0.185,
            "categoria": "Liga Profesional",
            "goles": 6
        },
        {
            "id": 320,
            "nombre": "Tomás Marchiori",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 2.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 321,
            "nombre": "Joaquín García",
            "edad": 25,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 322,
            "nombre": "Thiago Silvero",
            "edad": 20,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 323,
            "nombre": "Lisandro Magallán",
            "edad": 32,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 324,
            "nombre": "Elías Gómez",
            "edad": 32,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 0
        },
        {
            "id": 325,
            "nombre": "Lucas Robertone",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 4.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 326,
            "nombre": "Rodrigo Aliendro",
            "edad": 35,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 327,
            "nombre": "Matías Pellegrini",
            "edad": 26,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 2.5,
            "categoria": "Liga Profesional",
            "goles": 2
        },
        {
            "id": 328,
            "nombre": "Manuel Lanzini",
            "edad": 33,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 1.5,
            "categoria": "Liga Profesional",
            "goles": 3
        },
        {
            "id": 329,
            "nombre": "Simón Escobar",
            "edad": 21,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 330,
            "nombre": "Thiago Aguirre",
            "edad": 22,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Vélez Sarsfield",
            "valor_mercado": 1.0,
            "categoria": "Liga Profesional",
            "goles": 1
        },
        {
            "id": 331,
            "nombre": "Mariano Monllor",
            "edad": 37,
            "posicion": "Portero",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 332,
            "nombre": "Santiago Bellatti",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 333,
            "nombre": "Joel Ghirardello",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 334,
            "nombre": "Álex Ruiz",
            "edad": 26,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 335,
            "nombre": "Franco Cortés",
            "edad": 24,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 336,
            "nombre": "Joaquín Postigo",
            "edad": 22,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 337,
            "nombre": "Nahuel Petillo",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 338,
            "nombre": "Ramiro Reynoso",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 339,
            "nombre": "Agustín Hermoso",
            "edad": 23,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 340,
            "nombre": "Lázaro Romero",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 341,
            "nombre": "Martín Schlotthauer",
            "edad": 26,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 342,
            "nombre": "Nicolás Carrizo",
            "edad": 34,
            "posicion": "Portero",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 343,
            "nombre": "Iván Zafarana",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 344,
            "nombre": "Alejo Tabares",
            "edad": 25,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 345,
            "nombre": "Hernán Grana",
            "edad": 41,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 346,
            "nombre": "Emiliano Purita",
            "edad": 29,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 347,
            "nombre": "Gustavo Turraca",
            "edad": 30,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 348,
            "nombre": "Alexis Melo",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 349,
            "nombre": "Matías Rodríguez",
            "edad": 33,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 350,
            "nombre": "Thiago Calone",
            "edad": 24,
            "posicion": "Segundo delantero",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 351,
            "nombre": "Santiago Apa",
            "edad": 26,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 352,
            "nombre": "Bruno Medina",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 353,
            "nombre": "Bruno Galván",
            "edad": 32,
            "posicion": "Portero",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 354,
            "nombre": "Agustín Dattola",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 355,
            "nombre": "Máximo Levi",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 356,
            "nombre": "Ramiro Fernández",
            "edad": 30,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 357,
            "nombre": "Enzo Cardozo",
            "edad": 20,
            "posicion": "Lateral derecho",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 358,
            "nombre": "Facundo Quignón",
            "edad": 33,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 359,
            "nombre": "Santiago Gauna",
            "edad": 23,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 360,
            "nombre": "Joaquín Velázquez",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 331,
            "nombre": "Mariano Monllor",
            "edad": 37,
            "posicion": "Portero",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 332,
            "nombre": "Santiago Bellatti",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 333,
            "nombre": "Joel Ghirardello",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 334,
            "nombre": "Álex Ruiz",
            "edad": 26,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 335,
            "nombre": "Franco Cortés",
            "edad": 24,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 336,
            "nombre": "Joaquín Postigo",
            "edad": 22,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 337,
            "nombre": "Nahuel Petillo",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 338,
            "nombre": "Ramiro Reynoso",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 339,
            "nombre": "Agustín Hermoso",
            "edad": 23,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 340,
            "nombre": "Lázaro Romero",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 341,
            "nombre": "Martín Schlotthauer",
            "edad": 26,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Acassuso",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 342,
            "nombre": "Nicolás Carrizo",
            "edad": 34,
            "posicion": "Portero",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 343,
            "nombre": "Iván Zafarana",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 344,
            "nombre": "Alejo Tabares",
            "edad": 25,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 345,
            "nombre": "Hernán Grana",
            "edad": 41,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 346,
            "nombre": "Emiliano Purita",
            "edad": 29,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 347,
            "nombre": "Gustavo Turraca",
            "edad": 30,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 348,
            "nombre": "Alexis Melo",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 349,
            "nombre": "Matías Rodríguez",
            "edad": 33,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 350,
            "nombre": "Thiago Calone",
            "edad": 24,
            "posicion": "Segundo delantero",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 351,
            "nombre": "Santiago Apa",
            "edad": 26,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 352,
            "nombre": "Bruno Medina",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético All Boys",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 353,
            "nombre": "Bruno Galván",
            "edad": 32,
            "posicion": "Portero",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 354,
            "nombre": "Agustín Dattola",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 355,
            "nombre": "Máximo Levi",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 356,
            "nombre": "Ramiro Fernández",
            "edad": 30,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 357,
            "nombre": "Enzo Cardozo",
            "edad": 20,
            "posicion": "Lateral derecho",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 358,
            "nombre": "Facundo Quignón",
            "edad": 33,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 359,
            "nombre": "Santiago Gauna",
            "edad": 23,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 360,
            "nombre": "Joaquín Velázquez",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 361,
            "nombre": "Tobías Zárate",
            "edad": 26,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 362,
            "nombre": "Santiago Vera",
            "edad": 27,
            "posicion": "Segundo delantero",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 363,
            "nombre": "Nazareno Bazán",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Almirante Brown",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 364,
            "nombre": "Enzo Vázquez",
            "edad": 25,
            "posicion": "Portero",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 365,
            "nombre": "Agustín Lamosa",
            "edad": 28,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 366,
            "nombre": "Pedro Sanz",
            "edad": 26,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 367,
            "nombre": "Mauricio Rosales",
            "edad": 34,
            "posicion": "Lateral derecho",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 368,
            "nombre": "Matías Villarreal",
            "edad": 34,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 369,
            "nombre": "Tomás Castro",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 370,
            "nombre": "Gianluca Mancuso",
            "edad": 28,
            "posicion": "Mediocampista",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 371,
            "nombre": "Maximiliano Ribero",
            "edad": 28,
            "posicion": "Mediocampista",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 372,
            "nombre": "Sergio Quiroga",
            "edad": 32,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 373,
            "nombre": "Joaquín Mateo",
            "edad": 28,
            "posicion": "Segundo delantero",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 374,
            "nombre": "Julián López",
            "edad": 29,
            "posicion": "Delantero centro",
            "club_actual": "Club Central Norte (Salta)",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 375,
            "nombre": "Nicolás Caprio",
            "edad": 37,
            "posicion": "Portero",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 376,
            "nombre": "Mathías Silvera",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.275,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 377,
            "nombre": "David Valdez",
            "edad": 33,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 378,
            "nombre": "Agustín Ojeda",
            "edad": 24,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 379,
            "nombre": "Alan Luque",
            "edad": 27,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 380,
            "nombre": "Brian Nievas",
            "edad": 28,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 381,
            "nombre": "Juan Carrizo",
            "edad": 25,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 382,
            "nombre": "Santiago Valenzuela",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 383,
            "nombre": "Brian Guerra",
            "edad": 30,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 384,
            "nombre": "Juan Cruz Cerrudo",
            "edad": 22,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 385,
            "nombre": "Matías Romero",
            "edad": 32,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Chaco For Ever",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 386,
            "nombre": "Agustín Rufinetti",
            "edad": 26,
            "posicion": "Portero",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 387,
            "nombre": "Ezequiel Navarro",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 388,
            "nombre": "Elías Martínez",
            "edad": 32,
            "posicion": "Defensa central",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 389,
            "nombre": "Nicolás Ihitz",
            "edad": 30,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 390,
            "nombre": "Agustín Paredes",
            "edad": 24,
            "posicion": "Lateral derecho",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 391,
            "nombre": "Facundo Mucignat",
            "edad": 27,
            "posicion": "Lateral derecho",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 392,
            "nombre": "Brian Quintana",
            "edad": 24,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 393,
            "nombre": "Maximiliano Gutiérrez",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 394,
            "nombre": "Brian Duarte",
            "edad": 27,
            "posicion": "Extremo derecho",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 395,
            "nombre": "Guillermo Sánchez",
            "edad": 31,
            "posicion": "Delantero centro",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 5
        },
        {
            "id": 396,
            "nombre": "Khalil Caraballo",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Ciudad de Bolívar",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 397,
            "nombre": "Matías Budiño",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.325,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 398,
            "nombre": "Sebastián Olmedo",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 399,
            "nombre": "Federico Rasmussen",
            "edad": 34,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 400,
            "nombre": "Leandro Allende",
            "edad": 29,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 401,
            "nombre": "Facundo Castet",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 402,
            "nombre": "Tomás Gallay",
            "edad": 21,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 403,
            "nombre": "Ignacio Lago",
            "edad": 23,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.6,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 404,
            "nombre": "Julián Marcioni",
            "edad": 28,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.55,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 405,
            "nombre": "Franco García",
            "edad": 29,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 406,
            "nombre": "Alan Bonansea",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.375,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 407,
            "nombre": "Jorge Sanguina",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Colón",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 408,
            "nombre": "Alejandro Medina",
            "edad": 39,
            "posicion": "Portero",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 409,
            "nombre": "Nicolás Morro",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 410,
            "nombre": "Diego Magallanes",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 411,
            "nombre": "Martín Rodríguez",
            "edad": 28,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 412,
            "nombre": "Juan De Tomaso",
            "edad": 33,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 413,
            "nombre": "Agustín Benítez",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.325,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 414,
            "nombre": "Ignacio Gutiérrez",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 415,
            "nombre": "Patricio Moyano",
            "edad": 23,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.275,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 416,
            "nombre": "Ezequiel Aguirre",
            "edad": 34,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 417,
            "nombre": "Leandro Ciccolini",
            "edad": 31,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 418,
            "nombre": "Joaquín Ardaiz",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Defensores de Belgrano",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 419,
            "nombre": "Yair Bonnín",
            "edad": 35,
            "posicion": "Portero",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 420,
            "nombre": "Facundo Giacopuzzi",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.55,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 421,
            "nombre": "Nicolás Ortiz",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 422,
            "nombre": "Lucas Diarte",
            "edad": 33,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 423,
            "nombre": "Agustín Sosa",
            "edad": 25,
            "posicion": "Lateral derecho",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.325,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 424,
            "nombre": "Yvo Calleros",
            "edad": 28,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.5,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 425,
            "nombre": "Facundo Ospitaleche",
            "edad": 30,
            "posicion": "Mediocampista",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 426,
            "nombre": "Marcelo Meli",
            "edad": 34,
            "posicion": "Mediocampista",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 427,
            "nombre": "Nazareno Solís",
            "edad": 32,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 428,
            "nombre": "Nicolás Servetto",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 429,
            "nombre": "Luis Silba",
            "edad": 36,
            "posicion": "Delantero centro",
            "club_actual": "Club Social y Deportivo Madryn",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 5
        },
        {
            "id": 430,
            "nombre": "Julio Salvá",
            "edad": 39,
            "posicion": "Portero",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 431,
            "nombre": "Francisco Flores",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.275,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 432,
            "nombre": "Braian Salvareschi",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 433,
            "nombre": "Joaquín Livera",
            "edad": 26,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 434,
            "nombre": "Emanuel Iñiguez",
            "edad": 29,
            "posicion": "Lateral derecho",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 435,
            "nombre": "Emiliano Franco",
            "edad": 31,
            "posicion": "Mediocampista",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 436,
            "nombre": "Maximiliano González",
            "edad": 32,
            "posicion": "Mediocampista",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 437,
            "nombre": "Santiago Kubiszyn",
            "edad": 23,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.45,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 438,
            "nombre": "Gonzalo Berterame",
            "edad": 29,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 439,
            "nombre": "Juan Cruz Esquivel",
            "edad": 25,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 440,
            "nombre": "Franco Fagúndez",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Deportivo Morón",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 441,
            "nombre": "Juan Manuel Lungarzo",
            "edad": 33,
            "posicion": "Portero",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 442,
            "nombre": "Nicolás Caro Torres",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 443,
            "nombre": "Martín Albarracín",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 444,
            "nombre": "Franco Quinteros",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 445,
            "nombre": "Facundo Ardiles",
            "edad": 27,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 446,
            "nombre": "Rodrigo Melo",
            "edad": 30,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 447,
            "nombre": "Federico Sena",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 448,
            "nombre": "Enzo Acosta",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 449,
            "nombre": "Jorge Correa",
            "edad": 33,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 450,
            "nombre": "Darío Rostagno",
            "edad": 24,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 451,
            "nombre": "Ezequiel Almirón",
            "edad": 23,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Estudiantes (Buenos Aires)",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 452,
            "nombre": "Fernando Monetti",
            "edad": 37,
            "posicion": "Portero",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 453,
            "nombre": "Federico Tévez",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 454,
            "nombre": "Gustavo Canto",
            "edad": 32,
            "posicion": "Defensa central",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 455,
            "nombre": "Sebastián Corda",
            "edad": 31,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 456,
            "nombre": "Nazareno Kihm",
            "edad": 21,
            "posicion": "Lateral derecho",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 457,
            "nombre": "Felipe Obradovich",
            "edad": 19,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 458,
            "nombre": "Matías Kabalin",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 459,
            "nombre": "Nicolás Gómez",
            "edad": 30,
            "posicion": "Mediocampista",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 460,
            "nombre": "Enzo Hoyos",
            "edad": 26,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 461,
            "nombre": "Ángel González",
            "edad": 32,
            "posicion": "Extremo derecho",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 462,
            "nombre": "Mateo Benegas",
            "edad": 20,
            "posicion": "Delantero centro",
            "club_actual": "Club Ferro Carril Oeste",
            "valor_mercado": 0.275,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 463,
            "nombre": "Roberto Ramírez",
            "edad": 30,
            "posicion": "Portero",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 464,
            "nombre": "Mateo Mendoza",
            "edad": 21,
            "posicion": "Defensa central",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 2.5,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 465,
            "nombre": "Nahuel Brunet",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.45,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 466,
            "nombre": "Juan Morán",
            "edad": 19,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.55,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 467,
            "nombre": "Lucas Arce",
            "edad": 28,
            "posicion": "Lateral derecho",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.9,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 468,
            "nombre": "Gastón Gil Romero",
            "edad": 33,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.275,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 469,
            "nombre": "Vicente Poggi",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 1.6,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 470,
            "nombre": "Felipe Cairus",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.7,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 471,
            "nombre": "Tomás Pozzo",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 472,
            "nombre": "Martín Pino",
            "edad": 28,
            "posicion": "Delantero centro",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 6
        },
        {
            "id": 473,
            "nombre": "Nahuel Ulariaga",
            "edad": 24,
            "posicion": "Delantero centro",
            "club_actual": "Club Deportivo Godoy Cruz Antonio Tomba",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 474,
            "nombre": "Sebastián López",
            "edad": 40,
            "posicion": "Portero",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.01,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 475,
            "nombre": "Daniel Franco",
            "edad": 34,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 476,
            "nombre": "Brian Leizza",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 477,
            "nombre": "Iván Grance",
            "edad": 26,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 478,
            "nombre": "Julián Navas",
            "edad": 32,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 479,
            "nombre": "Juan Manuel Vázquez",
            "edad": 31,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 480,
            "nombre": "Sergio Ortíz",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 481,
            "nombre": "Gabriel Cañete",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 482,
            "nombre": "Matías González",
            "edad": 27,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 483,
            "nombre": "Facundo Villarreal",
            "edad": 21,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 484,
            "nombre": "Mauricio Asenjo",
            "edad": 31,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Los Andes",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 485,
            "nombre": "Ignacio Pietrobono",
            "edad": 34,
            "posicion": "Portero",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 486,
            "nombre": "Iván Antunes",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 487,
            "nombre": "Pablo Minissale",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 488,
            "nombre": "Daniel Abello",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 489,
            "nombre": "Martín Vázquez",
            "edad": 27,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 490,
            "nombre": "Franco Ferrari",
            "edad": 33,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 491,
            "nombre": "Juan Alessandroni",
            "edad": 37,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 492,
            "nombre": "Claudio Salto",
            "edad": 31,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 493,
            "nombre": "Santiago Rosales",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 494,
            "nombre": "Marcos Machado",
            "edad": 25,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 9
        },
        {
            "id": 495,
            "nombre": "Juan Pablo Zárate",
            "edad": 23,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Mitre (Santiago del Estero)",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 496,
            "nombre": "Brian Olivera",
            "edad": 32,
            "posicion": "Portero",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 497,
            "nombre": "Gabriel Aranda",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 498,
            "nombre": "Matías Sánchez",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 499,
            "nombre": "Tomás Kummer",
            "edad": 21,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 500,
            "nombre": "Marcio Gómez",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 501,
            "nombre": "Gaspar Vega",
            "edad": 33,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 502,
            "nombre": "Matías Machado",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 503,
            "nombre": "Facundo Juárez",
            "edad": 32,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 504,
            "nombre": "Ricardo Centurión",
            "edad": 33,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 505,
            "nombre": "Leandro Córdoba",
            "edad": 21,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 5
        },
        {
            "id": 506,
            "nombre": "Sergio González",
            "edad": 31,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Racing (Córdoba)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 507,
            "nombre": "Matías Escobar",
            "edad": 23,
            "posicion": "Portero",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 508,
            "nombre": "Felipe Coronel",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 509,
            "nombre": "Facundo Cardozo",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.225,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 510,
            "nombre": "Alexis Cruz",
            "edad": 26,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 511,
            "nombre": "Damián Adín",
            "edad": 29,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 512,
            "nombre": "Fabrizio Almeida",
            "edad": 24,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 513,
            "nombre": "Mateo Serra",
            "edad": 22,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 514,
            "nombre": "Jorge Ferrero",
            "edad": 34,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.025,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 515,
            "nombre": "Lucas Brochero",
            "edad": 27,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 516,
            "nombre": "Daniel Juárez",
            "edad": 24,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 517,
            "nombre": "Bruno Nasta",
            "edad": 33,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético San Miguel",
            "valor_mercado": 0.275,
            "categoria": "Primera Nacional",
            "goles": 5
        },
        {
            "id": 518,
            "nombre": "Joaquín Enrico",
            "edad": 24,
            "posicion": "Portero",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 519,
            "nombre": "Leonel Pollacchi",
            "edad": 23,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 520,
            "nombre": "Emanuel Díaz",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.05,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 521,
            "nombre": "Gabriel Paredes",
            "edad": 22,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 522,
            "nombre": "Juan Ignacio Motroni",
            "edad": 27,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 523,
            "nombre": "Renzo Uriburu",
            "edad": 23,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.175,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 524,
            "nombre": "Elías Brítez",
            "edad": 25,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 525,
            "nombre": "Román Gamarra",
            "edad": 24,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.075,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 526,
            "nombre": "Jerónimo Porto",
            "edad": 25,
            "posicion": "Extremo izquierdo",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 527,
            "nombre": "Iñaki Larthirigoyen",
            "edad": 22,
            "posicion": "Extremo derecho",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 528,
            "nombre": "Nicolás Molina",
            "edad": 27,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético San Telmo",
            "valor_mercado": 0.125,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 529,
            "nombre": "L. Acosta",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 530,
            "nombre": "A. Perez",
            "edad": 26,
            "posicion": "Defensor",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 531,
            "nombre": "M. Ramos",
            "edad": 29,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 532,
            "nombre": "T. Lecanda",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 533,
            "nombre": "F. González",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 534,
            "nombre": "S. Gallucci",
            "edad": 34,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 535,
            "nombre": "R. Castro",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 536,
            "nombre": "B. Aranda",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 537,
            "nombre": "C. Auzqui",
            "edad": 35,
            "posicion": "Extremo",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 538,
            "nombre": "B. Blando",
            "edad": 31,
            "posicion": "Delantero centro",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 539,
            "nombre": "O. Belinetz",
            "edad": 31,
            "posicion": "Delantero",
            "club_actual": "Club Agropecuario Argentino",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 540,
            "nombre": "Emilio González",
            "edad": 28,
            "posicion": "Portero",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 541,
            "nombre": "Matías Cortave",
            "edad": 33,
            "posicion": "Defensa central",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 542,
            "nombre": "Lautaro Puñet",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 543,
            "nombre": "Gonzalo Asís",
            "edad": 30,
            "posicion": "Defensor",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 544,
            "nombre": "Franco Marco",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 545,
            "nombre": "Julián Marchioni",
            "edad": 33,
            "posicion": "Mediocampista",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 546,
            "nombre": "Julián Vitale",
            "edad": 31,
            "posicion": "Mediocampista",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 547,
            "nombre": "Franco Bustamante",
            "edad": 27,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 548,
            "nombre": "Joel Orlando",
            "edad": 28,
            "posicion": "Delantero",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 5
        },
        {
            "id": 549,
            "nombre": "Mateo Benegas",
            "edad": 26,
            "posicion": "Delantero centro",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 5
        },
        {
            "id": 550,
            "nombre": "Andrés Chávez",
            "edad": 35,
            "posicion": "Delantero centro",
            "club_actual": "Club Almagro",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 551,
            "nombre": "F. Rago",
            "edad": 31,
            "posicion": "Portero",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 552,
            "nombre": "P. Ostachuk",
            "edad": 26,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 553,
            "nombre": "R. Moreira",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 554,
            "nombre": "M. Garcia",
            "edad": 28,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 555,
            "nombre": "T. Rojas",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 556,
            "nombre": "N. Previtali",
            "edad": 31,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 557,
            "nombre": "B. Rivero",
            "edad": 28,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 558,
            "nombre": "T. Castro Ponce",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 559,
            "nombre": "L. Fedele",
            "edad": 24,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 560,
            "nombre": "F. Castro",
            "edad": 31,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 561,
            "nombre": "A. Quintana",
            "edad": 34,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Atlanta",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 562,
            "nombre": "M. Bergia",
            "edad": 27,
            "posicion": "Portero",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 563,
            "nombre": "G. Fernández",
            "edad": 29,
            "posicion": "Defensor",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 564,
            "nombre": "A. Solveyra",
            "edad": 25,
            "posicion": "Defensor",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 565,
            "nombre": "F. Ponce",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 566,
            "nombre": "U. Yegros",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 567,
            "nombre": "J. Capurro",
            "edad": 31,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 568,
            "nombre": "F. Soloa",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 569,
            "nombre": "J. Cavallaro",
            "edad": 32,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 570,
            "nombre": "M. Moreno",
            "edad": 27,
            "posicion": "Extremo",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 571,
            "nombre": "L. Albertengo",
            "edad": 35,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 572,
            "nombre": "M. Quiroga",
            "edad": 32,
            "posicion": "Delantero",
            "club_actual": "Club Atlético de Rafaela",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 573,
            "nombre": "Enrique Bologna",
            "edad": 44,
            "posicion": "Portero",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.1,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 574,
            "nombre": "Santiago Acosta",
            "edad": 24,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 575,
            "nombre": "Brian Calderara",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 576,
            "nombre": "Nicolás Chaves",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 577,
            "nombre": "Milton Leyendeker",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 578,
            "nombre": "Lucas Alfonzo",
            "edad": 25,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 579,
            "nombre": "Álvaro Cuello",
            "edad": 31,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 580,
            "nombre": "Luciano Perdomo",
            "edad": 30,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 581,
            "nombre": "Cristian Guanca",
            "edad": 33,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.5,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 582,
            "nombre": "Mauricio Cuero",
            "edad": 33,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 583,
            "nombre": "Francisco Cristaldo",
            "edad": 26,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Chacarita Juniors",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 584,
            "nombre": "E. Di Fulvio",
            "edad": 30,
            "posicion": "Portero",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 585,
            "nombre": "F. Rivero",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 586,
            "nombre": "F. Hanashiro",
            "edad": 27,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 587,
            "nombre": "L. Ortiz",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 588,
            "nombre": "L. Martínez Montagnoli",
            "edad": 30,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 589,
            "nombre": "G. Chiavetto",
            "edad": 25,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 590,
            "nombre": "F. Montiel",
            "edad": 26,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 591,
            "nombre": "F. Zicarelli",
            "edad": 24,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 592,
            "nombre": "L. Castillo",
            "edad": 29,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 593,
            "nombre": "M. Albertengo",
            "edad": 35,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 594,
            "nombre": "N. Toloza",
            "edad": 27,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Colegiales",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 595,
            "nombre": "N. Galardi",
            "edad": 27,
            "posicion": "Portero",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 596,
            "nombre": "L. Arnijas",
            "edad": 27,
            "posicion": "Defensor",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 597,
            "nombre": "J. de la Reta",
            "edad": 25,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 598,
            "nombre": "L. Faggioli",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 599,
            "nombre": "A. R. Aguero Gimenez",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 600,
            "nombre": "G. Mansilla",
            "edad": 33,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 601,
            "nombre": "F. Montero",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 602,
            "nombre": "T. Silva",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 603,
            "nombre": "L. Cabrera",
            "edad": 29,
            "posicion": "Delantero centro",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 604,
            "nombre": "J. M. Sanchez",
            "edad": 27,
            "posicion": "Delantero",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 605,
            "nombre": "V. Barrera",
            "edad": 24,
            "posicion": "Delantero",
            "club_actual": "Club Deportivo Maipú",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 606,
            "nombre": "M. Alvarez",
            "edad": 30,
            "posicion": "Portero",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 607,
            "nombre": "G. Cosaro",
            "edad": 37,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 608,
            "nombre": "M. Lazarte",
            "edad": 29,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 609,
            "nombre": "F. Camargo",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 610,
            "nombre": "N. Dematei",
            "edad": 38,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.15,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 611,
            "nombre": "H. Soria",
            "edad": 35,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 612,
            "nombre": "F. Molina",
            "edad": 31,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 613,
            "nombre": "C. Pombo",
            "edad": 30,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 614,
            "nombre": "O. Bianchi",
            "edad": 30,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 615,
            "nombre": "C. Menendez",
            "edad": 38,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 616,
            "nombre": "A. Arganaraz",
            "edad": 28,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Gimnasia y Esgrima (Jujuy)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 617,
            "nombre": "J. Papaleo",
            "edad": 32,
            "posicion": "Portero",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 618,
            "nombre": "M. Guanini",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 619,
            "nombre": "J. Galetto",
            "edad": 30,
            "posicion": "Defensor",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 620,
            "nombre": "G. Díaz",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 621,
            "nombre": "L. Montoya",
            "edad": 31,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 622,
            "nombre": "F. Sivetti",
            "edad": 28,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 623,
            "nombre": "W. Montoya",
            "edad": 33,
            "posicion": "Mediocampista",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 624,
            "nombre": "T. Banega",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 625,
            "nombre": "N. Rinaldi",
            "edad": 32,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 626,
            "nombre": "F. Rojas",
            "edad": 29,
            "posicion": "Delantero",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 627,
            "nombre": "L. Contín",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club de Gimnasia y Tiro (Salta)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 628,
            "nombre": "L. Finochietto",
            "edad": 29,
            "posicion": "Portero",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 629,
            "nombre": "W. Juarez",
            "edad": 28,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 630,
            "nombre": "T. Oneto",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 631,
            "nombre": "O. Vanegas",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 632,
            "nombre": "F. Galvan",
            "edad": 31,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 633,
            "nombre": "F. Godoy",
            "edad": 29,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 634,
            "nombre": "F. Bergés",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 635,
            "nombre": "M. Quiroz",
            "edad": 31,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 636,
            "nombre": "S. G. Sala",
            "edad": 28,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 637,
            "nombre": "J. Sanchez",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 638,
            "nombre": "T. Amilivia",
            "edad": 28,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Güemes",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 639,
            "nombre": "M. Leguiza",
            "edad": 29,
            "posicion": "Portero",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 640,
            "nombre": "P. Castorani",
            "edad": 27,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 641,
            "nombre": "G. Cepeda",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 642,
            "nombre": "L. Díaz Laharque",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 643,
            "nombre": "L. Recalde",
            "edad": 31,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 644,
            "nombre": "N. Violini",
            "edad": 26,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 645,
            "nombre": "M. Roseti",
            "edad": 27,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 646,
            "nombre": "V. Gargiulo",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 647,
            "nombre": "D. Bulacio",
            "edad": 27,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 648,
            "nombre": "A. Campana",
            "edad": 29,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 649,
            "nombre": "Santino Primante",
            "edad": 21,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Ferrocarril Midland",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 650,
            "nombre": "Facundo Masuero",
            "edad": 25,
            "posicion": "Portero",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 651,
            "nombre": "Bruno Palazzo",
            "edad": 25,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 652,
            "nombre": "Román Zalazar",
            "edad": 25,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 653,
            "nombre": "Dylan Gissi",
            "edad": 35,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 654,
            "nombre": "Diego Arroyo",
            "edad": 24,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 655,
            "nombre": "Emiliano Méndez",
            "edad": 37,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 656,
            "nombre": "Alejo González",
            "edad": 24,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 657,
            "nombre": "Maximiliano Rogoski",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 658,
            "nombre": "Thiago Ocampo",
            "edad": 22,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 659,
            "nombre": "Diego Barros",
            "edad": 21,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 660,
            "nombre": "Simón Pérez",
            "edad": 24,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Nueva Chicago",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 661,
            "nombre": "Franco Rivasseau",
            "edad": 28,
            "posicion": "Portero",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 662,
            "nombre": "Fernando Moreyra",
            "edad": 36,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 663,
            "nombre": "Franco Meritello",
            "edad": 30,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 664,
            "nombre": "Santiago Piccioni",
            "edad": 23,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 665,
            "nombre": "Juan Salas",
            "edad": 28,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 666,
            "nombre": "Federico Bravo",
            "edad": 32,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 667,
            "nombre": "Agustín Araujo",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 668,
            "nombre": "Brandon Cortés",
            "edad": 25,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 669,
            "nombre": "Emanuel Maciel",
            "edad": 29,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 670,
            "nombre": "Franco Soldano",
            "edad": 32,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 671,
            "nombre": "Renzo Reynaga Llarena",
            "edad": 27,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Patronato",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 672,
            "nombre": "Gonzalo Marinelli",
            "edad": 37,
            "posicion": "Portero",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 673,
            "nombre": "Raúl Lozano",
            "edad": 29,
            "posicion": "Lateral derecho",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 674,
            "nombre": "Ian Rasso",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 675,
            "nombre": "Ariel Kippes",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 676,
            "nombre": "Agustín Bindella",
            "edad": 25,
            "posicion": "Lateral izquierdo",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 677,
            "nombre": "Agustín Bolívar",
            "edad": 30,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 678,
            "nombre": "Ramiro Luna",
            "edad": 23,
            "posicion": "Mediocampista",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.45,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 679,
            "nombre": "Facundo Yozwiak",
            "edad": 22,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 680,
            "nombre": "Agustín Lavezzi",
            "edad": 30,
            "posicion": "Extremo",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 681,
            "nombre": "Aaron Spetale",
            "edad": 26,
            "posicion": "Delantero centro",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.45,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 682,
            "nombre": "Mauro Fernandez",
            "edad": 36,
            "posicion": "Delantero",
            "club_actual": "Quilmes Atlético Club",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 683,
            "nombre": "S. Diaz Robles",
            "edad": 26,
            "posicion": "Portero",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 684,
            "nombre": "M. Osores",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 685,
            "nombre": "H. Zuliani",
            "edad": 24,
            "posicion": "Defensor",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 686,
            "nombre": "N. Paz",
            "edad": 28,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 687,
            "nombre": "F. Murillo",
            "edad": 31,
            "posicion": "Defensor",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 688,
            "nombre": "D. A. Mercado Carrizo",
            "edad": 28,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 689,
            "nombre": "G. Hachen",
            "edad": 36,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 690,
            "nombre": "L. Veron",
            "edad": 27,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 691,
            "nombre": "S. Gonzalez",
            "edad": 27,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 692,
            "nombre": "G. Rossi",
            "edad": 29,
            "posicion": "Delantero",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 693,
            "nombre": "N. Funez",
            "edad": 29,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético San Martín (San Juan)",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 694,
            "nombre": "D. Sand",
            "edad": 38,
            "posicion": "Portero",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 695,
            "nombre": "A. Galvan",
            "edad": 31,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 696,
            "nombre": "V. Salazar",
            "edad": 33,
            "posicion": "Lateral derecho",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 697,
            "nombre": "E. Parnisari",
            "edad": 36,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.2,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 698,
            "nombre": "L. Diarte",
            "edad": 33,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 699,
            "nombre": "M. Ríos",
            "edad": 34,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 700,
            "nombre": "G. Carabajal",
            "edad": 35,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.35,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 701,
            "nombre": "J. Soraire",
            "edad": 37,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 702,
            "nombre": "L. Ovando",
            "edad": 26,
            "posicion": "Extremo",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 703,
            "nombre": "F. Pons",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.45,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 704,
            "nombre": "B. Cabrera",
            "edad": 29,
            "posicion": "Delantero",
            "club_actual": "Club Atlético San Martín (Tucumán)",
            "valor_mercado": 0.4,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 705,
            "nombre": "E. Mastrolia",
            "edad": 35,
            "posicion": "Portero",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 706,
            "nombre": "O. Pacheco",
            "edad": 28,
            "posicion": "Defensor",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 707,
            "nombre": "M. Calzon",
            "edad": 25,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 708,
            "nombre": "V. Aguinagalde",
            "edad": 27,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 709,
            "nombre": "G. Nardelli",
            "edad": 26,
            "posicion": "Defensa central",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 710,
            "nombre": "L. Monti",
            "edad": 27,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 711,
            "nombre": "A. Arregui",
            "edad": 34,
            "posicion": "Mediocampista",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 712,
            "nombre": "G. Tomasetti",
            "edad": 27,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 713,
            "nombre": "Gabriel Hauche",
            "edad": 39,
            "posicion": "Extremo",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 714,
            "nombre": "F. Kruger",
            "edad": 26,
            "posicion": "Delantero centro",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 715,
            "nombre": "F. Brandan",
            "edad": 36,
            "posicion": "Delantero",
            "club_actual": "Club Atlético Temperley",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 3
        },
        {
            "id": 716,
            "nombre": "J. Bigo",
            "edad": 28,
            "posicion": "Portero",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 717,
            "nombre": "B. Aguilar",
            "edad": 27,
            "posicion": "Defensor",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 718,
            "nombre": "A. Sánchez",
            "edad": 30,
            "posicion": "Lateral izquierdo",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 719,
            "nombre": "M. Guzman",
            "edad": 29,
            "posicion": "Defensa central",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 720,
            "nombre": "A. Baldi",
            "edad": 24,
            "posicion": "Defensa central",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 721,
            "nombre": "M. Enrique",
            "edad": 27,
            "posicion": "Mediocampista defensivo",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 0
        },
        {
            "id": 722,
            "nombre": "N. Del Priore",
            "edad": 29,
            "posicion": "Mediocampista",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.25,
            "categoria": "Primera Nacional",
            "goles": 1
        },
        {
            "id": 723,
            "nombre": "D. Becker",
            "edad": 28,
            "posicion": "Mediocampista ofensivo",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 724,
            "nombre": "S. Ramirez",
            "edad": 26,
            "posicion": "Extremo",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 2
        },
        {
            "id": 725,
            "nombre": "A. Gallo",
            "edad": 30,
            "posicion": "Delantero centro",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 4
        },
        {
            "id": 726,
            "nombre": "R. Conechny",
            "edad": 25,
            "posicion": "Delantero",
            "club_actual": "Club Social y Deportivo Tristán Suárez",
            "valor_mercado": 0.3,
            "categoria": "Primera Nacional",
            "goles": 3
        },
    ]

    return jugadores