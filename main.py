from flask import Flask, render_template, request, jsonify
from markupsafe import escape
from flask import render_template
import osmnx as ox
import networkx as nx

app = Flask(__name__)


@app.route("/")
def p_main(name=None):
    return render_template("index.html")


@app.route("/graph")
def get_graph():
    G = ox.graph.graph_from_place("Piedmont, California, USA", network_type="drive")
    nodes, edges = ox.graph_to_gdfs(G)
    return edges.to_json()


@app.route("/map")
def hello():
    name = request.args.get("name", "Flask")
    return render_template("indx_t.html", nombre="map")


@app.route("/secondP")
def second_page():
    return "segunda ruta"


# if __name__ == "__main__":
# app.run(debug=True)
