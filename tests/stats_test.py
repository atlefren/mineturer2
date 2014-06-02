# -*- coding: utf-8 -*-
import unittest
import dateutil.parser

from shapely.geometry import Point

from models import Trip, Point as MTPoint


class TripStatTest(unittest.TestCase):

    def setUp(self):
        self.trip = Trip()
        p1 = MTPoint(
            self.trip,
            Point(10.434591, 63.399736),
            dateutil.parser.parse('2012-10-10T17:06:27.000Z'),
            ele=94.6,
        )
        self.trip.points.append(p1)
        p2 = MTPoint(
            self.trip,
            Point(10.434781, 63.40054),
            dateutil.parser.parse('2012-10-10T17:07:10.000Z'),
            ele=193.4,
        )
        self.trip.points.append(p2)
        p3 = MTPoint(
            self.trip,
            Point(10.430045, 63.401501),
            dateutil.parser.parse('2012-10-10T17:09:02.000Z'),
            ele=213.7,
        )
        self.trip.points.append(p3)
        p4 = MTPoint(
            self.trip,
            Point(10.446138, 63.405615),
            dateutil.parser.parse('2012-10-10T17:45:04.000Z'),
            ele=52.8
        )
        self.trip.points.append(p4)

    def test_get_time_info(self):
        stats = self.trip.stats
        self.assertEquals(stats['start'], '2012-10-10T17:06:27+00:00')
        self.assertEquals(stats['stop'], '2012-10-10T17:45:04+00:00')
        self.assertEquals(stats['total_time'].total_seconds(), 2317.0)
        self.assertEquals(stats['active_time'].total_seconds(), 2317.0)
        self.assertEquals(stats['flat_time'].total_seconds(), 0.0)
        self.assertEquals(stats['asc_time'].total_seconds(), 155.0)
        self.assertEquals(stats['desc_time'].total_seconds(), 2162.0)

    def test_compute_distance(self):
        stats = self.trip.stats
        self.assertEquals(round(stats['distance_2d'], 2), 1275.68)
        self.assertEquals(round(stats['distance_3d'], 2), 1333.96)
        self.assertEquals(stats['distance_flat'], 0.0)
        self.assertEquals(round(stats['distance_asc'], 2), 394.32)
        self.assertEquals(round(stats['distance_desc'], 2), 939.64)

    def test_compute_speeds(self):
        stats = self.trip.stats
        self.assertEquals(round(stats['avg_speed'], 4), 0.5757)
        self.assertEquals(round(stats['avg_moving_speed'], 4), 0.5757)

    def test_compute_heights(self):
        stats = self.trip.stats
        self.assertEquals(stats['total_ascent'], 119.1)
        self.assertEquals(round(stats['total_descent'], 2), -160.9)
        self.assertEquals(stats['max_height'], 213.7)
        self.assertEquals(stats['min_height'], 52.8)
        self.assertEquals(round(stats['elev_diff'], 2), 160.9)
