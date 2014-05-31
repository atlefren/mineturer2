var MT = this.MT || {};
(function (ns) {
    'use strict';

    ns.createMap = function (div) {

        var map = L.map(div[0]).setView([64.5, 15], 5);

        L.tileLayer(
            'http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=norges_grunnkart&zoom={z}&x={x}&y={y}',
            {
                attribution: "&copy; <a href='http://statkart.no'>Kartverket</a>"
            }
        ).addTo(map);
        return map;
    };

}(MT));