#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='tb-common',
    version='0.1',
    author='Thong Dong',
    author_email='thongdong7@gmail.com',
    packages=find_packages(),
    install_requires=[
        'six==1.10.0',
    ],
    entry_points={
        'console_scripts': [
        ],
    }
)


