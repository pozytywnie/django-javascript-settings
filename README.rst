javascript-settings
========================

javascript-settings is a Django application that provides
a way of passing values backend from Django applications
to JavaScript in templates.

Installation
------------

Package
_______

javascript-settings can be installed as a normal Python package.

Example instalation for pip::

    $ pip install javascript-settings

Example instalation from file::

    $ pip install javascript-settings-1.1.tar.gz

Configuration
-------------

settings.py
___________

Add javascript-settings to INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'javascript_settings',
        ...
    )

Add javascript-settings.finders to STATICFILES_FINDERS::

    STATICFILES_FINDERS = (
        ...
        'javascript_settings.finders',
        ...
    )

template
________

You can use one of following ways to pass gathered data to template:

Option 1: Import
++++++++++++++++

Add javascript-settings.js to script imports::

    <script type="text/javascript" src="{{ STATIC_URL }}javascript-settings.js"></script>

Option 2: Template tag
++++++++++++++++++++++

Add javascript-settings tag to your main template::

    {% load javascript_settings_tags %}
    <script type="text/javascript">{% javascript_settings %}</script>

Usage
-----

Configuration is defined by adding ``javascript_settings`` function to urls.py of app.
``javascript_settings`` should take no arguments and return json-serializable object.
Serialized object is then avaliable in Javascript as ``configuration['app_name']``.

If you want to place ``javascript_settings`` in different location, then you can
define ``JAVASCRIPT_SETTINGS_SCAN_MODULES`` as a dictionary of ``'app_name': 'module_location'``.

Example
-------

Template::

    <script type="text/javascript" src="{{ STATIC_URL }}javascript-settings.js"></script>

urls.py in an app "home"::

    def javascript_settings():
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

Result in file javascript-settings.js::

    var configuration = {'home': {'page_title': 'Home', 'page_version': '1.9.20', 'css': {'white': './css/white.css', 'black': './css/black.css', 'print': './css/print.css'}, 'default_css': 'white'}};
