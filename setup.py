#!/usr/bin/env python
from os import path
from setuptools import setup

def read(name):
    return open(path.join(path.dirname(__file__), name)).read()

setup(
    name='javascript-configuration',
    description="javascript-configuration is a Django application that provides way of passing settings for Django applications to JavaScript.",
    long_description=read("README.rst"),
    version='1.1.2',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
    ),
    packages=[
        'javascript_configuration',
    ],
)
