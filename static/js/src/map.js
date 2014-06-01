var MT = this.MT || {};
(function (ns) {
    'use strict';

    function createTileLayer(url, attribution) {
        return L.tileLayer(url, {attribution: attribution});
    }

    function createSkLayer(layername) {
        var url = 'http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=' + layername + '&zoom={z}&x={x}&y={y}';
        return createTileLayer(
            url,
            '&copy; <a href="http://statkart.no">Kartverket</a>'
        );
    }

    function createCycleMapLayer() {
        return createTileLayer(
            'http://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png',
            '&copy; Gravitystorm Limited &amp; OpenStreetMap'
        );
    }

    function createOSMLayer() {
        return createTileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            'Map data &copy <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
        );
    }

    function skLayers() {
        var layers = {
            norges_grunnkart: 'Norges grunnkart',
            topo2: 'Topo 2',
            topo2graatone: 'Topo 2 grå',
            toporaster2: 'Toporaster',
            sjo_hovedkart2: 'Sjø hovedkart'
        };
        return _.reduce(layers, function (layers, title, layername) {            
            layers[title] = createSkLayer(layername);
            return layers;
        }, {});
    }

    ns.createMap = function (div) {
        var baseMaps = skLayers();

        baseMaps = _.extend(baseMaps, {
            'OpenStreetMap': createOSMLayer(),
            'OpenCycleMap': createCycleMapLayer()
        });

        var map = L.map(
            div[0],
            {
                layers: _.first(_.values(baseMaps))
            }
        ).setView([64.5, 15], 5);

        L.control.layers(baseMaps).addTo(map);

        return map;
    };

}(MT));