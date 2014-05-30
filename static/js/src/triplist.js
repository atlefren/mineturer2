var MT = MT || {};
(function (ns) {
    'use strict';

    var Trip = SpatialBB.MarkerModel.extend({

        defaults: {
            'highlighted': false
        },

        initialize: function () {
            this.on('change:highlighted', this.highlightedChange, this);
        },

        highlightedChange: function () {
            if (this.get('highlighted')) {
                this.marker.setZIndexOffset(1000);
            } else {
                this.marker.setZIndexOffset(0);
            }
        },

        createMarker: function () {
            SpatialBB.MarkerModel.prototype.createMarker.apply(this, arguments);
            this.marker.on('mouseover', this.markerEvent, this);
            this.marker.on('mouseout', this.markerEvent, this);
            this.marker.on('click', this.markerEvent, this);
        },

        markerEvent: function (e) {
            if (e.type === 'mouseover') {
                this.set('highlighted', true);
            }

            if (e.type === 'mouseout') {
                this.set('highlighted', false);
            }

            if (e.type === 'click') {
                console.log('click!', this.id);
            }
        }

    });

    ns.Trips = SpatialBB.MarkerCollection.extend({

        model: Trip,

        getLayerGroup: function () {
            if (!this.layerGroup.getLayers().length) {
                this.each(this.modelAdded, this);
            }
            return this.layerGroup;
        }
    });

    var TripItemView = Backbone.View.extend({

        template: $('#triplistitem_template').html(),

        events: {
            'mouseenter': 'mouseenter',
            'mouseleave': 'mouseleave',
        },

        initialize: function () {
            this.model.on('change:highlighted', this.changeHighlight, this);
        },

        render: function () {
            this.setElement(_.template(this.template, this.model.toJSON()));
            return this;
        },

        mouseenter: function () {
            this.model.set('highlighted', true);
        },

        mouseleave: function () {
            this.model.set('highlighted', false);
        },

        changeHighlight: function () {
            if (this.model.get('highlighted')) {
                this.$el.addClass('highlighted');
            } else {
                this.$el.removeClass('highlighted');
            }
        }

    });

    ns.TripListView = Backbone.View.extend({

        className: 'list-group triplist',

        render: function () {

            this.$el.append(this.collection.map(function (trip) {
                return new TripItemView({model: trip}).render().$el;
            }));

            return this;
        }
    });

    ns.createMap = function (div, trips) {

        L.Icon.Default.imagePath = '/static/css/lib/leaflet-0.7.3/images/';

        var map = L.map(div[0]).setView([64.5, 15], 5);

        L.tileLayer(
            'http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=norges_grunnkart&zoom={z}&x={x}&y={y}',
            {
                attribution: "&copy; <a href='http://statkart.no'>Kartverket</a>"
            }
        ).addTo(map);
        var lg = trips.getLayerGroup();

        map.addLayer(lg);
    };

}(MT));