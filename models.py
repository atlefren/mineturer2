# -*- coding: utf-8 -*-
import hashlib
import bcrypt


from sqlalchemy import (Column, Integer, String, Text, Boolean, DateTime,
                        Numeric, ForeignKey)
from sqlalchemy.orm import relationship
from geoalchemy2.types import Geometry
from geoalchemy2.shape import to_shape, from_shape
from shapely.geometry import LineString

from database import Base
from computations import get_stats, compute_speed


class User(Base):
    validation_errors = None
    __tablename__ = 'users'
    __table_args__ = {'schema': 'mineturer'}
    id = Column('userid', Integer, primary_key=True)
    username = Column('username', String(20), unique=True, index=True)
    password = Column('password', String(50), nullable=True)
    bcrypt_pwd = Column('bcrypt_pwd', String)
    fullname = Column('fullname', String(50))
    enabled = Column('enabled', Boolean)
    email = Column('email', String(50), unique=True, index=True)
    trips = relationship(
        'Trip',
        backref='mineturer.user',
        order_by='desc(Trip.start)'
    )

    def __init__(self, username=None, password=None, password2=None,
                 email=None, fullname=None):
        self.validation_errors = {}
        self.username = username
        self.fullname = fullname
        self.set_password(password, password2)
        self.email = email

    def set_password(self, password, password2):
        if not self.validation_errors:
            self.validation_errors = {}

        if not password and not self.id:
            self.validation_errors['password'] = 'Fyll inn passord'
        if not password2 and not self.id:
            self.validation_errors['password2'] = 'Sett passord igjen'
        if password != password2:
            self.validation_errors['password2'] = 'Passordene er ulike'
        if self.validation_errors:
            return

        if password:
            sha1_hashed = hashlib.sha1(password).hexdigest()
            self.bcrypt_pwd = bcrypt.hashpw(sha1_hashed, bcrypt.gensalt())

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.enabled

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def password_ok(self, password):

        sha1_hashed = hashlib.sha1(password).hexdigest()

        bcrypt_hashed = bcrypt.hashpw(
            sha1_hashed,
            self.bcrypt_pwd.encode('utf-8')
        )
        return bcrypt_hashed == self.bcrypt_pwd

    def validate(self):

        if not self.validation_errors:
            self.validation_errors = {}

        if not self.id and not self.username:
            self.validation_errors['username'] = 'Fyll inn brukernavn'

        if not self.id and not self.fullname:
            self.validation_errors['fullname'] = 'Fyll inn navn'

        if not self.id and not self.email:
            self.validation_errors['email'] = 'Fyll inn epost'

        if not self.id and get_user_by_username(self.username):
            self.validation_errors['username'] = 'Brukernavnet er opptatt'

        if self.validation_errors:
            return False
        return True

    def __repr__(self):
        return '<User %r>' % (self.username)


class Trip(Base):
    __tablename__ = 'trips'
    __table_args__ = {'schema': 'mineturer'}
    id = Column('tripid', Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', Text)
    start = Column('start', DateTime)
    stop = Column('stop', DateTime)
    type = Column('triptype', String)
    userid = Column(Integer, ForeignKey('mineturer.users.userid'))
    user = relationship(User, primaryjoin=userid == User.id)
    points = relationship(
        'Point',
        backref='mineturer.trips',
        order_by='asc(Point.time)',
        lazy='dynamic'
    )

    stored_points_list = None
    stats_dict = None

    def serialize(self):
        return {
            'id': self.id,
            'type': self.type,
            'date': self.start.isoformat(),
            'title': self.title
        }

    def serialize_with_point(self):
        data = self.serialize()
        start = to_shape(self.points.first().geom)
        data['position'] = {'lon': start.x, 'lat': start.y}
        return data

    @property
    def stored_points(self):
        if not self.stored_points_list:
            self.stored_points_list = self.points.all()
        return self.stored_points_list

    @property
    def geom(self):
        points = [to_shape(point.geom) for point in self.stored_points]
        return LineString(points)

    @property
    def stats(self):

        if not self.stats_dict:
            points = self.stored_points

            start_time = points[0].time
            end_time = points[-1].time

            stats = get_stats(points)

            total_time = end_time - start_time

            avg_speed = compute_speed(stats['distance_3d'], total_time)
            avg_moving_speed = compute_speed(
                stats['distance_3d'],
                stats['active_time']
            )

            asc_speed = compute_speed(stats['distance_asc'], stats['asc_time'])
            desc_speed = compute_speed(
                stats['distance_desc'],
                stats['desc_time']
            )
            flat_speed = compute_speed(
                stats['distance_flat'],
                stats['flat_time']
            )

            self.stats_dict = {
                'start': start_time.isoformat(),
                'stop': end_time.isoformat(),
                'total_time': total_time,
                'active_time': stats['active_time'],
                'distance_2d': stats['distance_2d'],
                'distance_3d': stats['distance_3d'],
                'distance_flat': stats['distance_flat'],
                'distance_asc': stats['distance_asc'],
                'distance_desc': stats['distance_desc'],
                'asc_speed': asc_speed,
                'desc_speed': desc_speed,
                'flat_speed': flat_speed,
                'avg_speed': avg_speed,
                'avg_moving_speed': avg_moving_speed,
                'total_descent': stats['total_descent'],
                'total_ascent': stats['total_ascent'],
                'max_height': stats['max_height'],
                'min_height': stats['min_height'],
                'flat_time': stats['flat_time'],
                'asc_time': stats['asc_time'],
                'desc_time': stats['desc_time'],
                'elev_diff': stats['max_height'] - stats['min_height'],
            }
        return self.stats_dict

        '''
        return {
            'start': '10.02.2013, kl 11:08',
            'stop': '10.02.2013, kl 12:26',
            'total_time': '1t 18m 1s',
            'active_time': '1t 13m 43s',
            'length_2d': '13.65 km',
            'length_3d': '13.92 km',
            'avg_speed': '10.71 km/t',
            'avg_moving_speed': '11.33 km/t',
            'ascent': '5.75 km, 0t 36m 21s, 9.5 km/t',
            'descent': '7.1 km, 0t 30m 42s, 13.89 km/t',
            'flat': '1.06 km, 0t 6m 40s, 9.57 km/t',
            'max_height': '476.1 m.o.h.',
            'min_height': '109.2 m.o.h.',
            'total_ascent': '1081.2 m',
            'total_descent': '861.8 m',
            'elev_diff': '366.9 m',
        }
        '''

    def __repr__(self):
        return '<Trip %r>' % (self.title)


class Point(Base):
    __tablename__ = 'points'
    __table_args__ = {'schema': 'mineturer'}
    pid = Column('pid', Integer, primary_key=True)
    geom = Column(Geometry(geometry_type='POINT', srid=4326))
    time = Column('time', DateTime)
    ele = Column('ele', Numeric)
    hr = Column('hr', Numeric)
    tripid = Column(Integer, ForeignKey('mineturer.trips.tripid'))
    trip = relationship(Trip, primaryjoin=tripid == Trip.id)

    def __init__(self, trip, geom, time, ele=None, hr=None):
        self.trip = trip
        self.geom = from_shape(geom, srid=4326)
        self.time = time
        self.ele = ele
        self.hr = hr

    def __repr__(self):
        return '<Point %r>' % (self.pid)


def get_user_by_username(username):
    return User.query.filter_by(
        username=username,
    ).first()
