import os
import sys

from setuptools import setup, find_packages

setup(
    name='sqlabeat',
    version='0.1',
    description='SQLAlchemy Celery Beat Scheduler',
    long_description='Celery beat scheduler using SQLAlcehmy for allowing use of relational databases for celery scheduling',
    author='Kashif Iftikhar',
    author_email='kashif@compulife.com.pk',
    url='https://github.com/kashifpk/celerybeat-sqlalchemy',
    keywords='Celery Beat SQLAlchemy Scheduler',
    license='GPLv2',
    classifiers=[
        "Development Status :: 4 - Beta",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['sqlalchemy'],
)
