# WebTool para la visualizacion de trafico

![viTraffic](./img_r/pic01.png)

# Dependecias

```bash
Flask 3.1.2
osmnx 2.0.6
```

# Data

[Dataset](https://pan.baidu.com/s/10bw4kQrklEFRC-mik9Fv2g) empleado en el modelo de [RouteVis](https://github.com/mmccc/RouteVis) con el code:67w3 y el otro dataset empleado por pN[Dataset](https://open-traffic.epfl.ch/index.php/downloads) empleado por el el modelo [pNeuma](https://github.com/EPFL-ENAC/pNEUMA).


# Uso

1. Primero clonamos el repositorio

    ```$ git clone https://github.com/MaycolZx/viTrafficData```

   ```$ cd viTrafficData```

2. Creamos un entorno virtual con las dependencias del programa

    ```$ python -m venv .venv```

    ```$ . .venv/bin/activate```

    ```$ pip install -r requirements```

3. Corremos el servidor de Flask

    ```$ flask --app main run --debug```

    o

   ```$ ./run.sh```

4. Al mismo tiempo corremos un entorno que controla el fronted de la pagina

```npx @tailwindcss/cli -i ./input.css -o ./static/style.css --watch```

Ahora solo queda entrar a la pagina localhost:5000
