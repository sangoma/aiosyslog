#!/usr/bin/env python

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='aiosyslog',
    version='0.1.0',
    author='Simon Gomizelj',
    author_email='sgomizelj@sangoma.com',
    packages=find_packages(exclude=('tests')),
    license='Apache 2',
    url='https://github.com/sangoma/aiosyslog',
    install_requires=['attrs'],
    description='Asyncio syslog server',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
)
