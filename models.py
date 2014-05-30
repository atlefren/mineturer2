# -*- coding: utf-8 -*-
import hashlib
import bcrypt


from sqlalchemy import (Column, Integer, String, Text, Boolean, DateTime,
                        Numeric, ForeignKey)
from sqlalchemy.orm import relationship
from geoalchemy2.types import Geometry
from geoalchemy2.shape import to_shape

from database import Base


def serialize_trip(trip, first_point):
    start = to_shape(first_point.geom)
    return {
        'position': {'lon': start.x, 'lat': start.y},
        'id': trip.id,
        'type': trip.type,
        'date': trip.start.isoformat(),
        'title': trip.title
    }


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
        order_by='desc(Point.time)',
        lazy='dynamic'
    )

    def serialize(self):
        start = to_shape(self.points.first().geom)
        return {
            'position': {'lon': start.x, 'lat': start.y},
            'id': self.id,
            'type': self.type,
            'date': self.start.isoformat(),
            'title': self.title
        }

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

    def __repr__(self):
        return '<Point %r>' % (self.pid)


def get_user_by_username(username):
    return User.query.filter_by(
        username=username,
    ).first()
