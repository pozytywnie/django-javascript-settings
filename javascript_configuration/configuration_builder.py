import sys

from django.conf import settings

class ConfigurationBuilder:
    """
        Get javascript configurations from urls.py files from all installed apps.
    """
    def __init__(self):
        self.configuration = None

    def fetch(self):
        configuration = {}
        for app in settings.INSTALLED_APPS:
            try:
                module_name = app + '.urls'
                __import__(module_name)
                urls = sys.modules[module_name]
                if hasattr(urls, 'javascript_configuration'):
                    configuration[app.split('.')[-1]] = urls.javascript_configuration()
            except ImportError:
                pass
        return configuration

    def get_configuration(self):
        if self.configuration is None:
            self.configuration = self.fetch()
        return self.configuration

DEFAULT_CONFIGURATION_BULDIER = ConfigurationBuilder()
