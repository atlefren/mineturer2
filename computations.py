# -*- coding: utf-8 -*-

import math
from itertools import izip, islice
from datetime import timedelta

from geopy import distance, Point as GpPoint
from geoalchemy2.shape import to_shape


def vincenty_distance(point1, point2):
    distance.VincentyDistance.ELLIPSOID = 'WGS 84'
    distance.distance = distance.VincentyDistance
    p1 = GpPoint(point1.y, point1.x)
    p2 = GpPoint(point2.y, point2.x)

    return distance.distance(p1, p2).meters


def get_stats(points):
    total_distance_2d = 0.0
    total_distance_3d = 0.0
    flat_distance = 0.0
    asc_distance = 0.0
    desc_distance = 0.0

    total_descent = 0.0
    total_ascent = 0.0

    #total_time = 0.0
    active_time = 0.0
    for current_point, next_point in izip(points, islice(points, 1, None)):
        distance_2d = vincenty_distance(
            to_shape(current_point.geom),
            to_shape(next_point.geom)
        )
        distance_vertical = next_point.ele - current_point.ele
        distance_3d = math.sqrt(
            math.pow(distance_2d, 2) + math.pow(distance_vertical, 2)
        )

        delta_time = next_point.time - current_point.time
        time = delta_time.total_seconds()
        m = distance_3d / time

        total_distance_2d += distance_2d
        total_distance_3d += distance_3d

        if m > 0.1:
            active_time += time

        if distance_vertical == 0.0:
            flat_distance += distance_3d
        elif distance_vertical > 0.0:
            asc_distance += distance_3d
            total_ascent += float(distance_vertical)
        elif distance_vertical < 0.0:
            desc_distance += distance_3d
            total_descent += float(distance_vertical)

    heights = [point.ele for point in points if point.ele]
    return {
        'distance_2d': total_distance_2d,
        'distance_3d': total_distance_3d,
        'distance_flat': flat_distance,
        'distance_asc': asc_distance,
        'distance_desc': desc_distance,
        'total_descent': total_descent,
        'total_ascent': total_ascent,
        'max_height': max(heights),
        'min_height': min(heights),
        'active_time': timedelta(seconds=active_time),
    }
