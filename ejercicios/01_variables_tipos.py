equipo_local = "Argentina"
equipo_visitante = "Colombia"
tiros_argentina = 8
tiros_colombia = 12
xg_argentina = 1.75
xg_colombia = 0.92
tiros_jugadores = 0
tiros_jugadores_argentina = 0
jugadores_argentina = [
    "Messi",
    "Alvarez",
    "De Paul",
    "Mac Allister",
    "Enzo Fernandez"
]

jugadores = [
    {
        "nombre": "Messi",
        "equipo": "Argentina",
        "tiros": 4,
        "xg": 0.82
    },
    {
        "nombre": "Alvarez",
        "equipo": "Argentina",
        "tiros": 2,
        "xg": 0.14
    },
    {
        "nombre": "Luis Diaz",
        "equipo": "Colombia",
        "tiros": 2,
        "xg": 0.2
    }
]


argentina_tuvo_mas_tiros = tiros_argentina > tiros_colombia

tiros_totales = tiros_argentina + tiros_colombia
diferencia_tiros = tiros_argentina - tiros_colombia

xg_total = xg_argentina + xg_colombia

xg_por_tiro_argentina = xg_argentina / tiros_argentina
xg_por_tiro_colombia = xg_colombia / tiros_colombia

if tiros_argentina > tiros_colombia:
    print("Argentina tuvo mas tiros")
elif tiros_colombia > tiros_argentina:
    print("Colombia tuvo mas tiros")
else:
    print("Ambos equipos tuvieron la misma cantidad de tiros")

if xg_por_tiro_argentina > xg_por_tiro_colombia:
    print("Argentina tuvo mayor xG promedio por tiro")
elif xg_por_tiro_colombia > xg_por_tiro_argentina:
    print("Colombia tuvo mayor xG promedio por tiro")
else:
    print("Ambos equipos tuvieron el mismo xG promedio por tiro")

if xg_argentina > xg_colombia:
    print("Argentina genero mas xG")
elif xg_colombia > xg_argentina:
    print("Colombia genero mas xG")
else:
    print("Ambos equipos generaron el mismo xG")

for jugador in jugadores:
    if jugador["equipo"] == "Argentina":
        print(jugador["nombre"])
        tiros_jugadores_argentina += jugador["tiros"]




print(tiros_jugadores_argentina)