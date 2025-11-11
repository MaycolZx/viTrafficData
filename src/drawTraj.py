# DataFrame, Date (days)
_df, _day = None, None
base_path = py_file_location


def get_day_info_data(day):
    # Objetos globales
    global _df, _day
    if day != _day:
        _day = day
        path = os.path.join(base_path, f"{_day}.csv")
        _df = pd.read_csv(path, encoding="utf-8")

    return _df


valor = get_day_info_data("daTR")

print("\n--- Primeras 5 filas del DataFrame (valor.head()) ---")
print(valor.head(1))

print("\n--- Información general del DataFrame (valor.info()) ---")
valor.info()

pr_row = valor.iloc[0]

lonSalida = pr_row["LongitudSalida"]
latSalida = pr_row["LatitudSalida"]
lonLlegada = pr_row["LongitudLlegada"]
latSalida = pr_row["LatitudLlegada"]

carretAtravesadas = pr_row["NumCarreterasTravesadas"]
secPointTraj = pr_row["SecuenciaPuntosTrayectoria"]

print(secPointTraj)

from shapely import wkt

line_strings_series = pr_row["SecuenciaPuntosTrayectoria"]
line = wkt.loads(line_strings_series)
coords = list(line.coords)
print(coords)
print(line.length)

import osmnx as ox
import matplotlib.pyplot as plt

df_puntos = pd.DataFrame(coords)
centro_lat = df_puntos[1].mean()
centro_lon = df_puntos[0].mean()

radio = 3000  # 3 km

G = ox.graph_from_point((centro_lat, centro_lon), dist=radio, network_type="drive")

fig, ax = ox.plot_graph(
    G,
    bgcolor="white",
    node_size=0,
    edge_color="gray",
    edge_linewidth=0.8,
    show=False,
    close=False,
)

ax.scatter(
    df_puntos[0],
    df_puntos[1],
    c="red",  # color de los puntos
    s=50,  # tamaño
    edgecolors="black",
    linewidth=0.5,
    zorder=5,  # encima del mapa
    label="Puntos de interés",
)

# 6. (Opcional) Añadir etiquetas a los puntos
# for idx, row in df_puntos.iterrows():
#     ax.text(
#         row['lon'] + 0.001,  # pequeño desplazamiento
#         row['lat'] + 0.001,
#         row['nombre'],
#         fontsize=9,
#         ha='left',
#         bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2)
#     )

ax.set_title("Mapa con puntos trayectoria", fontsize=14)
ax.legend(loc="upper right")

plt.tight_layout()
plt.show()
