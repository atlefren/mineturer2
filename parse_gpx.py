# -*- coding: utf-8 -*-

from datetime import datetime

from shapely.geometry import Point

from models import Point as MTPoint


def parse_gpx(file):

    p1 = MTPoint(
        geom=Point(10, 60),
        time=datetime.now()
    )
    p2 = MTPoint(
        geom=Point(11, 60),
        time=datetime.now()
    )

    return [p1, p2]
