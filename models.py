# -*- coding: utf-8 -*-
from datetime import datetime
import hashlib

from sqlalchemy import Column, Integer, String, DateTime, Date, Time, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'mineturer'}
    id = Column('userid', Integer, primary_key=True)
    username = Column('username', String(20), unique=True, index=True)
    password = Column('password', String(10))
    fullname = Column('fullname', String(50))
    fullname = Column('enabled', Boolean)
    email = Column('email', String(50), unique=True, index=True)    
 
    def __init__(self, username, password, email, fullname):
        self.username = username
        self.fullname = fullname
        self.password = password
        self.email = email
    
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return self.enabled
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def password_ok(self, password):        
        return hashlib.sha1(password).hexdigest() == self.password
    def __repr__(self):
        return '<User %r>' % (self.username)        


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default=False)

    def __init__(self, name):        
        self.name = name