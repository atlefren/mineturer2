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
        self.assertEquals(stats['total_time'], '38:37')
        #self.assertEquals(stats['active_time'], '38:37')

    def test_compute_distance(self):
        stats = self.trip.stats
        self.assertEquals(stats['distance_2d'], 1.28)
        self.assertEquals(stats['distance_3d'], 1.33)
        self.assertEquals(stats['distance_flat'], 0.0)
        self.assertEquals(stats['distance_asc'], 0.94)
        self.assertEquals(stats['distance_desc'], 0.39)