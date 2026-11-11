// Ayuda a obtener la ubicación del usuario actual
/* navigator es un objeto entregado por el navegador.
geolocation busca la ubicacion del dispositivo utilizado.
luego cuando la ubicación es encontrada recien corre la función
*/
const link = document.getElementById("compartirUbicacion");
link.addEventListener("click", function(event){
    /*Previene que <a id="compartirUbicacion" href="#"> navegue a el link de href y ejecuta la función en vez*/
    event.preventDefault(); 

    navigator.geolocation.getCurrentPosition(
        function(position){
            let latitud = position.coords.latitude;
            let longitud = position.coords.longitude;
            
            map.setView([latitud, longitud], 15);

            L.marker([latitud, longitud]).addTo(map);
        }
    );
});

/* Map section */
const mapa = document.getElementById("mapa");
let map;

if (mapa){
    /* L.map("id cualquiera") busca en los archivos html la id con el nombre "id cualquiera"
    y crea un mapa en la divisiónn (en este caso)
    setView() determina donde comienza el mapa y su nivel de zoom 
    (en este caso las cordenadas de santiago)*/
    map = L.map('mapa').setView(
        [-33.4489, -70.6693],
        13
    );
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19}).addTo(map);
}