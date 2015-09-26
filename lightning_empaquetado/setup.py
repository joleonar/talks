#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='demo_empaquetado_junin_2015',
    version='0.1',
    description=u'A demo of python packaging',
    long_description=open('README.rst').read(),
    author=u'Juan Pedro Fisanotti',
    author_email='fisadev@gmail.com',
    url='http://github.com/fisadev/talks',
    packages=['demo_empaquetado_junin_2015', ],
    license='LICENSE.txt',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
