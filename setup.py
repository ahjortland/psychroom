#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY').read().replace('.. :changelog:', '')

setup(
    name='psychroom',
    version='0.0.1',
    description='Herrick Laboratory Psychrometric Room Toolkit.',
    long_description=readme + '\n\n' + history,
    author='Andrew Hjortland',
    author_email='hjortlanda@gmail.com',
    url='https://github.com/ahjortland/psychroom',
    packages=[
        'psychroom',
    ],
    package_data={
        'psychroom': ['defaults.ini']
    },
    package_dir={'psychroom': 'psychroom'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=True,
    keywords='HVAC psychrometry experiments',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
