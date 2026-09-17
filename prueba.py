from clubes import cargar_clubes
from jugadores import cargar_jugadores

var = cargar_jugadores()

id_nuevo = max(var["id"]) + 1

print(id_nuevo)