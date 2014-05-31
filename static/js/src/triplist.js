var MT = this.MT || {};
(function (ns) {
    'use strict';

    moment.lang('nb');

    function createIcon(type) {
        return L.icon({
            iconUrl: '/static/images/icons/' + type + '.png',
            //shadowUrl: 'leaf-shadow.png',
            iconSize:     [32, 37], // size of the icon
            //shadowSize:   [50, 64], // size of the shadow
            iconAnchor:   [15, 34], // point of the icon which will correspond to marker's location
            //shadowAnchor: [4, 62],  // the same for the shadow
            //popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
        });
    }

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

        createMarker: function (position) {

            if (position) {
                this.marker = new L.Marker(
                    [position.lat, position.lon],
                    {
                        icon: createIcon(this.get('type')),
                        title: this.get('title')
                    }
                );
                this.marker.on('mouseover', this.markerEvent, this);
                this.marker.on('mouseout', this.markerEvent, this);
                this.marker.on('click', this.markerEvent, this);
            }
        },

        markerEvent: function (e) {
            if (e.type === 'mouseover') {
                this.set('highlighted', true);
            }

            if (e.type === 'mouseout') {
                this.set('highlighted', false);
            }

            if (e.type === 'click') {
                window.location = '/trips/' + this.get('id');
            }
        },

        toDisplay: function () {
            return _.extend(
                this.toJSON(),
                {date: moment(this.get('date')).format('D. MMMM YYYY')}
            );
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
            this.setElement(_.template(this.template, this.model.toDisplay()));
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

    ns.createListMap = function (div, trips) {

        L.Icon.Default.imagePath = '/static/css/lib/leaflet-0.7.3/images/';

        var map = ns.createMap(div);
        var lg = trips.getLayerGroup();

        map.addLayer(lg);
    };

}(MT));