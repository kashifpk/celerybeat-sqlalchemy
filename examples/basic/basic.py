"""
Basic scheduling example
"""

import os.path
from os.path import abspath
from sqlabeat.db import get_db_engine, create_tables, get_db_session
from sqlabeat.schedulers import SQLAlchemyScheduler
from celery import Celery

app = Celery('basic', broker='amqp://guest@localhost//')


here = os.path.dirname(abspath(__file__))
db_path = here + "/pycktestproject.db"
SQLALCHEMY_URL = 'sqlite:///' + db_path


class MyScheduler(SQLAlchemyScheduler):
    sqlalchemy_db_url = SQLALCHEMY_URL


@app.task
def task1():
    print("Hello from task 1")


@app.task
def say_hello(name):
    print("Hello " + name)


if __name__ == '__main__':
    engine = None
    if not os.path.exists(db_path):
        engine = get_db_engine(SQLALCHEMY_URL)
        create_tables(engine)
        print("DB created!")

