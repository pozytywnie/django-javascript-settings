javascript-configuration
========================

javascript-configuration is a Django application that provides
a way of passing settings for Django applications to JavaScript.

Installation
------------

Package
_______

javascript-configuration can be installed as a normal Python package.

Example instalation for pip::

    $ pip install javascript-configuration

Example instalation from file::

    $ pip install javascript-configuration-1.1.tar.gz

Configuration
-------------

settings.py
___________

Add javascript-configuration to INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'javascript_configuration',
        ...
    )

template
________

Add javascript-configuration tag to your main template::

    {% load javascript_configuration_tags %}
    <script type="text/javascript">{% javascript-configuration %}</script>

Usage
-----

Configuration is defined by adding ``javascript_configuration`` function to urls.py of app.
``javascript_configuration`` should take no arguments and return json-serializable object.
Serialized object is then avaliable in Javascript as ``configuration['app_name']``.

If you want to place ``javascript_configuration`` in different location, then you can
define ``JAVASCRIPT_CONFIGURATION_SCAN_MODULES`` as a dictionary of ``'app_name': 'module_location'``.

Example
-------

Template::

    {% load javascript_configuration_tags %}
    <script type="text/javascript">{% javascript_configuration %}</script>

urls.py in an app::

    def javascript_configuration():
        js_conf = {
                'page_title': 'Home',
                'page_version': '1.9.20',
                'css': {
                    'white': './css/white.css',
                    'black': './css/black.css',
                    'print': './css/print.css',
                },
                'default_css': 'white',
        }
        return js_conf

For example the app is named "home".

Result::

    <script type="text/javascript">var configuration = {'home': {'page_title': 'Home', 'page_version': '1.9.20', 'css': {'white': './css/white.css', 'black': './css/black.css', 'print': './css/print.css'}, 'default_css': 'white'}};</script>
