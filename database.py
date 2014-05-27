# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(connection_string="sqlite://", echo=False):
    engine = create_engine(connection_string, convert_unicode=True, echo=echo)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))

    Base.query = db_session.query_property()

    return db_session, Base.metadata, engine
