javascript-configuration
========================

javascript-configuration is a Django application that provides
way of passing settings for Django applications to JavaScript.

Installation
------------

Package
_______

javascript-configuration can be installet as normal Python package.

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

urls.py
_______

Add javascript-configuration to urlpatterns::

    urlpatterns = patterns('',
        ...
        (r'^javascript_configuration/', include('javascript_configuration.urls')),
        ...
    )

template
________

Add javascript-configuration to your main template::

    <script type="text/javascript" src="{% url javascript-configuration %}"></script>

Usage
-----

Configuration is defined by adding ``javascript_configuration`` function to urls.py of app.
``javascript_configuration`` should take no arguments and return json-serializable object.
Serialized object is then avaliable in Javascript as ``configuration['app_name']``.

Example
-------

TODO
