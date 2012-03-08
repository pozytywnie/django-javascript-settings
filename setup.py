#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

def read(name):
    return open(path.join(path.dirname(__file__), name)).read()

setup(
    name='django-javascript-settings',
    description="django-javascript-settings is a Django application that provides a way of passing settings for Django applications to JavaScript.",
    long_description=read("README.rst"),
    version='1.0.1',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
    ),
    packages=find_packages(),
)
