#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages


def read(name):
    return open(path.join(path.dirname(__file__), name)).read()

def runtests():
    from django.conf import settings
    from django.core.management import call_command

    if not settings.configured:
        settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS=(
                'javascript_settings',
            ),
        )
    call_command('test', 'javascript_settings')

setup(
    name='django-javascript-settings',
    description=("django-javascript-settings is a Django application that "
                 "provides a way of passing settings for Django applications "
                 "to JavaScript."),
    long_description=read("README.rst"),
    version='1.1.1',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
    ),
    packages=find_packages(),
    test_suite='javascript_settings.runtests',
)
