# -*- coding: utf-8 -*-

from shapely.geometry import Point
import xml.etree.ElementTree as ET

from models import Point as MTPoint
from xml_code.gpx11 import parseString as parse11
from xml_code.gpx10 import parseString as parse10


def parse_gpx_11(data):
    gpx = parse11(data, True)
    points = []
    for track in gpx.get_trk():
        for segment in track.get_trkseg():
            for track_point in segment.get_trkpt():
                points.append(MTPoint(
                    geom=Point(track_point.get_lon(), track_point.get_lat()),
                    time=track_point.get_time(),
                    ele=track_point.get_ele()
                ))
    return points


def parse_gpx_10(data):
    gpx = parse10(data, True)
    points = []
    for track in gpx.get_trk():
        for segment in track.get_trkseg():
            for track_point in segment.get_trkpt():
                #print track_point.get_lon(), track_point.get_lat()
                #print type(track_point.get_lon()), type(track_point.get_lat())
                points.append(MTPoint(
                    geom=Point(float(track_point.get_lon()), float(track_point.get_lat())),
                    time=track_point.get_time(),
                    ele=track_point.get_ele()
                ))
    return points


def parse_gpx(file):    
    data = file.read()    
    root = ET.fromstring(data)
    print root.tag
    if root.tag == '{http://www.topografix.com/GPX/1/0}gpx':
        return parse_gpx_10(data)
    elif root.tag == '{http://www.topografix.com/GPX/1/1}gpx':
        return parse_gpx_11(data)
    print "??"
