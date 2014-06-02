var MT = this.MT || {};
(function (ns) {
    'use strict';

    function createIcon(filename) {
        return L.icon({
            iconUrl: '/static/images/icons/' + filename,
            iconSize: [21, 25], // size of the icon            
            iconAnchor: [2, 25] // point of the icon which will correspond to marker's             
        });
    }

    ns.showTrip = function (geoJson) {
        L.Icon.Default.imagePath = '/static/css/lib/leaflet-0.7.3/images/';
        var map = ns.createMap($('.map'));
        var layer = L.geoJson(
            geoJson,
            {
                color: '#17A417'
            }
        ).addTo(map);

        var first = _.first(_.first(layer.getLayers()).getLatLngs());
        var last = _.last(_.last(layer.getLayers()).getLatLngs());
        L.marker(first, {icon: createIcon('start.png')}).addTo(map);
        L.marker(last, {icon: createIcon('finish.png')}).addTo(map);

        map.fitBounds(layer.getBounds());
    };

}(MT));