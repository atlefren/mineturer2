var MT = MT || {};
(function (ns) {
  'use strict';

  var Trip = SpatialBB.MarkerModel.extend({
    /*
    initialize: function (attributes, options) {

            if (options && options.collection) {
                options.requirePosition = options.collection.requirePosition;
            }

            options = options || {};

            if (!_.has(options, "initPos")) {
                options.initPos = true;
            }
            if (_.has(options, "requirePosition")) {
                this.requirePosition = options.requirePosition;
            }
            if (options.initPos) {
              console.log(this.parsePosition())
                this.createMarker(this.parsePosition());
            }
        },

        parsePosition: function () {

            var position = null;
            if (this.has("position")) {
                position = {
                    "lon": this.get("position").lon || null,
                    "lat": this.get("position").lat || null
                };
            }
            if ((!position || !position.lon || !position.lat) && this.requirePosition) {
                throw new ns.MissingPositionError();
            }
            return position;
        }
    */
  });

  ns.Trips = SpatialBB.MarkerCollection.extend({
    model: Trip,

    getLayerGroup: function () {
      if (!this.layerGroup.getLayers().length) {
        this.each(this.modelAdded, this);
      }
      return this.layerGroup;
    },
  });

  var TripItemView = Backbone.View.extend({

    template: $('#triplistitem_template').html(),

    render: function () {
      this.setElement(_.template(this.template, this.model.toJSON()));
      return this;
    }

  });

  ns.TripListView = Backbone.View.extend({

    className: 'list-group',

    render: function () {

      this.$el.append(this.collection.map(function (trip) {
        return new TripItemView({model: trip}).render().$el;
      }));

      return this;
    },
  });

  ns.createMap = function (div, trips) {

    L.Icon.Default.imagePath = '/static/css/lib/leaflet-0.7.3/images/';
    
    var map = L.map(div[0]).setView([64.5, 15], 5);
    console.log(trips);
    L.tileLayer(
      'http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=norges_grunnkart&zoom={z}&x={x}&y={y}',
      {
        attribution: "&copy; <a href='http://statkart.no'>Kartverket</a>"
      }
    ).addTo(map);
    var lg = trips.getLayerGroup();
    console.log(lg);
    map.addLayer(lg);
  };

}(MT));