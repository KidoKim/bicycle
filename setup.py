# -*- coding:utf-8 -*-
from setuptools import setup

install_requires = [
    'flask==0.10.1',
    'sqlalchemy==0.9.9',
    'alembic==0.7.4',
    'gunicorn==19.3.0',
    'fabric==1.10.1',
    'flask-sqlalchemy==0.16',
]

setup(
    name='bicycle',
    version='0.1',
    install_requires=install_requires,
)
