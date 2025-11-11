import pandas as pd

archivo_entrada = "./chdata/20161101.csv"
archivo_salida = "./daTR.csv"
codificacion = "utf-8"  # O prueba 'gbk' si hay error

traduccion_cabecera = {
    "轨迹ID": "IDTrajectoria",  # 1
    "出发时间": "HoraSalida",  # 2
    "出发经度": "LongitudSalida",  # 3
    "出发纬度": "LatitudSalida",  # 4
    "出发道路ID": "IDCarreteraSalida",  # 5
    "到达时间": "HoraLlegada",  # 6
    "到达经度": "LongitudLlegada",  # 7
    "到达维度": "LatitudLlegada",  # 8 Nota: error tipográfico en chino
    "到达道路ID": "IDCarreteraLlegada",  # 9
    "时长(秒)": "Duracion(s)",  # 10
    "距离(米)": "Distancia(m)",  # 11
    "通过道路数": "NumCarreterasTravesadas",  # 12
    "其他道路数量": "CantidadCarreterasOtras",  # 13
    "residential道路数量": "CantidadCarreterasResidenciales",  # 14
    "unclassified道路数量": "CantidadCarreterasSinClasificar",  # 15
    "tertiary道路数量": "CantidadCarreterasTerciarias",  # 16
    "secondary道路数量": "CantidadCarreterasSecundarias",  # 17
    "primary道路数量": "CantidadCarreterasPrimarias",  # 18
    "trunk道路数量": "CantidadCarreterasTrunk",  # 19
    "motorway道路数量": "CantidadAutopistas",  # 20
    "道路序列": "SecuenciaCarreteras",  # 21
    "轨迹点序列": "SecuenciaPuntosTrayectoria",  # 22
    "轨迹点序列(百度)": "SecuenciaPuntos(Baidu)",  # 23
    "出发时刻": "MomentoSalida",  # 24
    "出发时段": "PeríodoSalida",  # 25
    "道路熟悉": "FamiliaridadCarretera",  # 26
    "平均速度": "VelocidadPromedio",  # 27
    "拥堵程度": "NivelCongestión",  # 28
}

# ==========================
# PROCESAMIENTO
# ==========================
try:
    # Leer el CSV (la primera fila es la cabecera china)
    df = pd.read_csv(archivo_entrada, encoding=codificacion)

    # Verificar que todas las columnas chinas estén en el diccionario
    columnas_faltantes = [col for col in df.columns if col not in traduccion_cabecera]
    if columnas_faltantes:
        print("Advertencia: Columnas no traducidas:", columnas_faltantes)

    # Renombrar columnas
    df.rename(columns=traduccion_cabecera, inplace=True)

    # Guardar el nuevo CSV con cabecera en español
    df.to_csv(archivo_salida, index=False, encoding="utf-8-sig")  # utf-8-sig para Excel

    print(f"¡Listo! Archivo guardado como: {archivo_salida}")
    print(f"   - Filas: {len(df)}")
    print(f"   - Columnas: {len(df.columns)}")
    print("\nPrimeras 2 filas de ejemplo:")
    print(df.head(2).to_string(index=False))

except FileNotFoundError:
    print(
        f"Error: No se encontró el archivo '{archivo_entrada}'. Verifica el nombre y la ruta."
    )
except Exception as e:
    print(f"Error inesperado: {e}")
    print(
        "   Consejo: Prueba con encoding='gbk' si el archivo es de origen chino antiguo."
    )
