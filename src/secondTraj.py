import os
import pandas as pd

with open(py_file_location + "20181024_d1_0830_0900.csv", encoding="utf-8") as f:
    lineas = [linea.strip().split(";") for linea in f]


def imprimir_fila(n):
    if 0 <= n < len(lineas):
        print(f"\n--- Fila {n} ({len(lineas[n])} campos) ---")
        cont = 1
        print(f"UI->", end=" ")
        for j, valor in enumerate(lineas[n], 1):
            if j == 1 or j == 2 or j == 3 or j == 4:
                print(f"{valor}", end="; ")
                if j == 4:
                    print()
                continue
            if j == len(lineas[n]):
                break
            print(f"{valor}", end="; ")
            if cont == 6:
                print("\n")
                cont = 0
            cont += 1
    else:
        print("Fila no existe")


imprimir_fila(1)

df_puntos = pd.DataFrame(puntos)

centro_lat = df_puntos["lat"].mean()
centro_lon = df_puntos["lon"].mean()

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
    df_puntos["lon"],
    df_puntos["lat"],
    c="red",  # color de los puntos
    s=50,  # tamaño
    edgecolors="black",
    linewidth=0.5,
    zorder=5,  # encima del mapa
    label="Puntos de interés",
)

for idx, row in df_puntos.iterrows():
    ax.text(
        row["lon"] + 0.001,  # pequeño desplazamiento
        row["lat"] + 0.001,
        row["nombre"],
        fontsize=9,
        ha="left",
        bbox=dict(facecolor="white", alpha=0.7, edgecolor="none", pad=2),
    )

ax.set_title("Mapa con puntos personalizados (OSMnx)", fontsize=14)
ax.legend(loc="upper right")

plt.tight_layout()
plt.show()
