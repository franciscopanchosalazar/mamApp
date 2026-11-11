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
            console.log(position.coords.latitude);
            console.log(position.coords.longitude);
        }
    );
});
