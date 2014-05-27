# -*- coding: utf-8 -*-
import hashlib
import bcrypt

from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'mineturer'}
    id = Column('userid', Integer, primary_key=True)
    username = Column('username', String(20), unique=True, index=True)
    password = Column('password', String(50), nullable=True)
    bcrypt_pwd = Column('bcrypt_pwd', String)
    fullname = Column('fullname', String(50))
    enabled = Column('enabled', Boolean)
    email = Column('email', String(50), unique=True, index=True)

    def __init__(self, username, password, email, fullname):
        self.username = username
        self.fullname = fullname
        self.set_password(password)
        self.email = email

    def set_password(self, password):
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

    def __repr__(self):
        return '<User %r>' % (self.username)


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default=False)

    def __init__(self, name):
        self.name = name
