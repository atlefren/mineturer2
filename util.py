# -*- coding: utf-8 -*-


def format_timedelta(delta):
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds, 60 * 60)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        return '%s:%s:%s' % (hours, minutes, seconds)
    return '%s:%s' % (minutes, seconds)


def to_km_2dec(meters):
    return round(meters / 1000, 2)
