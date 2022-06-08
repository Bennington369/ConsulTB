const mylatlng= {lng:-96.3564,lat:18.4472 };
const latitud = document.getElementById('latitud');
const longitud = document.getElementById('longitud');




    mapboxgl.accessToken = 'pk.eyJ1IjoiYmVubmluZ3RvbiIsImEiOiJjbDI5a3JhaDYwMDVzM2NvNjJzOGt0bGZjIn0.4Yohr0bYdPLqpiekKEuGQw';
    const map = new mapboxgl.Map({
        
        container: 'map', // container ID
        style: 'mapbox://styles/mapbox/streets-v11', // style URL
        center:[longitud.value,latitud.value], // starting position [lng, lat]
        zoom: 17// starting zoom
       
    });
    
     
    
    const nav = new mapboxgl.NavigationControl({
        visualizePitch: true
    });
    map.addControl(nav, 'bottom-right');
    
    // Initialize the GeolocateControl.
    const geolocate = new mapboxgl.GeolocateControl({
        positionOptions: {
            enableHighAccuracy: true
        },
        trackUserLocation: true
    });
    // Add the control to the map.
    map.addControl(geolocate);
    // Set an event listener that fires
    // when a geolocate event occurs.
    


    
    
window.addEventListener('DOMContentLoaded', () => {
    const marker = new mapboxgl.Marker({
        draggable: false
        })
        .setLngLat([longitud.value,latitud.value])
        .addTo(map);
        });
