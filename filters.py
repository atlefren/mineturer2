# -*- coding: utf-8 -*-

import arrow


def create_filters(app):
    @app.template_filter('strftime')
    def _jinja2_filter_datetime(date, format=None):

        # TODO: fix format to norwegian with no leadign zero
        if format is None:
            format = 'D. MMMM YYYY'
        return arrow.get(date).format(format, locale='nb')

    @app.template_filter('format_timedelta')
    def _jinja2_format_timedelta(delta):
        total_seconds = int(delta.total_seconds())
        hours, remainder = divmod(total_seconds, 60 * 60)
        minutes, seconds = divmod(remainder, 60)

        if hours > 0:
            return '%s:%s:%s' % (hours, minutes, seconds)
        return '%s:%s' % (minutes, seconds)

    @app.template_filter('display_length')
    def _jinja2_display_length(length):
        return '{0:.2f} km'.format(length / 1000)

    @app.template_filter('display_speed')
    def _jinja2_display_speed(speed):
        return '{0:.2f} km/t'.format(speed * 3.6)
