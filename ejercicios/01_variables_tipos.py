import pandas as pd

equipo_local = "Argentina"
equipo_visitante = "Colombia"
tiros_argentina = 8
tiros_colombia = 12
xg_argentina = 1.75
xg_colombia = 0.92
tiros_jugadores = 0
tiros_jugadores_argentina = 0
cantidad_jugadores_argentina = 0
xg_jugadores_argentina = 0
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

df_jugadores = pd.DataFrame(jugadores)
df_argentina = df_jugadores[df_jugadores["equipo"] == "Argentina"]
tiros_argentina_df = df_argentina["tiros"].sum()
xg_argentina_df = df_argentina["xg"].sum()
cantidad_argentinos_df = len(df_argentina)

resumen_equipos = df_jugadores.groupby("equipo").agg(
    jugadores=("nombre", "count"),
    tiros=("tiros", "sum"),
    xg=("xg", "sum"),
    xg_promedio=("xg", "mean")
)

resumen_equipos["xg_por_tiro"] = (
    resumen_equipos["xg"] / resumen_equipos["tiros"]
)

df_ordenado = df_jugadores.sort_values(
    by=["equipo", "tiros"],
    ascending=[True, True]
)

df_xg = df_jugadores.sort_values(
    by="xg",
    ascending=False
)

top_2_xg = df_xg.head(2)

top_tiros = df_jugadores.sort_values(
    by="tiros",
    ascending=False
).head(3)

top_tiros_reducido = top_tiros[["nombre", "equipo", "tiros"]]

print(top_tiros_reducido)




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
        tiros_jugadores_argentina += jugador["tiros"]
        xg_jugadores_argentina += jugador["xg"]
        cantidad_jugadores_argentina += 1

def calcular_xg_por_tiro(xg, tiros):
    if tiros == 0:
        return 0
    return xg / tiros

def analizar_equipo (jugadores, equipo):
    cantidad_jugadores = 0
    cantidad_tiros = 0
    xg_totales = 0
    xg_por_tiro_totales = 0
    for jugador in jugadores:
        if jugador["equipo"] == equipo:
            cantidad_jugadores += 1
            cantidad_tiros += jugador["tiros"]
            xg_totales += jugador["xg"]
    xg_por_tiro_totales = calcular_xg_por_tiro(xg_totales, cantidad_tiros)
    resumen = {
        "jugadores" : cantidad_jugadores,
        "tiros" : cantidad_tiros,
        "xg" : xg_totales,
        "xg_por_tiro" : xg_por_tiro_totales
    }
    return resumen

resumen_argentina = analizar_equipo(jugadores, "Argentina")
resultado_argentina = calcular_xg_por_tiro(xg_argentina, tiros_argentina)
resultado_colombia = calcular_xg_por_tiro(xg_colombia, tiros_colombia)
test_con_0 = calcular_xg_por_tiro(0,0)




