#!/usr/bin/env python
# coding=utf-8

from setuptools import setup
import adclick


try:
    long_description = open('README.md').read()
except:
    long_description = adclick.__description__


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='adclick',
    version=adclick.__version__,
    url='https://www.adbund.com',
    author=adclick.__author__,
    author_email=adclick.__email__,
    description=adclick.__description__,
    long_description=long_description,
    license=adclick.__license__,
    packages=['adclick'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=REQUIREMENTS
)
