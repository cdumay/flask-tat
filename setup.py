# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>

"""

from setuptools import setup

setup(
    name='flask-tat',
    version=open('VERSION', 'r').read().strip(),
    description="Flask TAT client",
    long_description=open('README.md', 'r').read().strip(),
    classifiers=["Programming Language :: Python"],
    keywords='',
    author='Cedric DUMAY',
    author_email='cedric.dumay@gmail.com',
    url='https://github.com/cdumay/flask-tat',
    license='Apache License',
    py_modules=['flask_tat'],
    include_package_data=True,
    zip_safe=True,
    install_requires=open('requirements.txt', 'r').readlines(),
)