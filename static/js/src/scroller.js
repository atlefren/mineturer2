var MT = this.MT || {};
(function (ns) {
    'use strict';

    ns.Scroller = Backbone.View.extend({

        events: {
            'mousedown #newer': 'startScrollUp',
            'mouseup #newer': 'stopScroll',
            'mousedown #older': 'startScrollDown',
            'mouseup #older': 'stopScroll'
        },

        initialize: function () {
            this.scrollList = this.$('.triplist');
            var parentHeight = this.scrollList.parent().height();
            this.maxMargin = this.scrollList[0].scrollHeight - parentHeight;
        },

        getMargin: function () {
            return parseInt(
                this.scrollList.css('margin-top').replace('px', ''),
                10
            );
        },

        startScrollUp: function () {
            this.scrollUp();
            this.interval = setInterval(
                _.bind(this.scrollUp, this),
                200
            );
        },

        scrollUp: function () {
            var margin = this.getMargin();
            if (margin < 0) {
                this.scrollList.css(
                    'margin-top',
                    margin + this.scrollList.find('a:first').outerHeight()
                );
            }
        },

        startScrollDown: function () {
            this.scrollDown();
            this.interval = setInterval(
                _.bind(this.scrollDown, this),
                200
            );
        },

        stopScroll: function () {
            clearInterval(this.interval);
        },

        scrollDown: function () {
            var margin = this.getMargin();
            if (Math.abs(margin) < this.maxMargin) {
                this.scrollList.css(
                    'margin-top',
                    margin - this.scrollList.find('a:first').outerHeight()
                );
            }
        }
    });

}(MT));