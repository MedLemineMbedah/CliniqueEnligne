
function initMap() {
    var options = {center : new L.LatLng(51.930156,7.189230), zoom : 7 };
    
    var osmUrl = 'http://{s}.tile.openstreetmap.org/mapnik_tiles/{z}/{x}/{y}.png',
                osmAttribution = 'Map data &copy; 2012 OpenStreetMap contributors',
                osm = new L.TileLayer(osmUrl, {maxZoom: 18, attribution: osmAttribution});
    
    var mapLayer = new L.TileLayer(osmUrl);
    
    this.map = new L.Map('map', options).addLayer(mapLayer);
 }
 
 function locateUser() {
    this.map.locate({setView : true});
 }
 
 var map = null;
 
 initMap();
 
 $('#actions').find('a').on('click', function() {
   locateUser();
 });
 function initMap() {
    var options = {center : new L.LatLng(51.930156,7.189230), zoom : 7 };
    
    var osmUrl = 'http://{s}.tile.openstreetmap.org/mapnik_tiles/{z}/{x}/{y}.png',
                osmAttribution = 'Map data &copy; 2012 OpenStreetMap contributors',
                osm = new L.TileLayer(osmUrl, {maxZoom: 18, attribution: osmAttribution});
    
    var mapLayer = new L.TileLayer(osmUrl);
    
    this.map = new L.Map('map', options).addLayer(mapLayer);
 }
 
 function locateUser() {
    this.map.locate({setView : true});
 }
 
 var map = null;
 
 initMap();
 
 $('#actions').find('a').on('click', function() {
   locateUser();
 });