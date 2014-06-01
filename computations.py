# -*- coding: utf-8 -*-

import math
from itertools import izip, islice

from geopy import distance, Point as GpPoint
from geoalchemy2.shape import to_shape


def vincenty_distance(point1, point2):
    distance.VincentyDistance.ELLIPSOID = 'WGS 84'
    distance.distance = distance.VincentyDistance
    p1 = GpPoint(point1.y, point1.x)
    p2 = GpPoint(point2.y, point2.x)

    return distance.distance(p1, p2).meters


def get_distances(points):
    total_distance_2d = 0.0
    total_distance_3d = 0.0
    flat_distance = 0.0
    asc_distance = 0.0
    desc_distance = 0.0
    for current_point, next_point in izip(points, islice(points, 1, None)):
        distance_2d = vincenty_distance(
            to_shape(current_point.geom),
            to_shape(next_point.geom)
        )
        distance_vertical = current_point.ele - next_point.ele
        distance_3d = math.sqrt(
            math.pow(distance_2d, 2) + math.pow(distance_vertical, 2)
        )

        total_distance_2d += distance_2d
        total_distance_3d += distance_3d

        if distance_vertical == 0.0:
            flat_distance += distance_3d
        elif distance_vertical > 0.0:
            asc_distance += distance_3d
        elif distance_vertical < 0.0:
            desc_distance += distance_3d

    return {
        'distance_2d': total_distance_2d,
        'distance_3d': total_distance_3d,
        'distance_flat': flat_distance,
        'distance_asc': asc_distance,
        'distance_desc': desc_distance
    }
