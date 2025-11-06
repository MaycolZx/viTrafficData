// Crear el mapa centrado en Piedmont
var map = L.map("map").setView([37.8249, -122.2316], 14);

// Capa base
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

// Cargar el GeoJSON del backend Flask
fetch("/graph")
  .then((response) => response.json())
  .then((data) => {
    L.geoJSON(data, {
      style: { color: "blue", weight: 2 },
    }).addTo(map);
  });
