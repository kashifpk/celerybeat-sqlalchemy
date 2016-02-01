"""
Database related code like SQLAlchemy engine and session creation etc.
"""

from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


def get_db_engine(db_url):
    return create_engine(db_url, echo=True)


def get_db_session(engine):
    "Given a DB engine return a DB session bound to that engine"

    db = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
    db.configure(bind=engine)
    db.autoflush = True

    return db


def create_tables(engine):
    Base.metadata.create_all(engine)
