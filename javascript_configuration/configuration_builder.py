import sys

from javascript_configuration import settings

class ConfigurationBuilder:
    """
        Get javascript configurations from urls.py files from all installed apps.
    """
    def __init__(self):
        self.configuration = None

    def fetch(self):
        configuration = {}
        for app_name, module_name in settings.SCAN_MODULES.iter_items():
            try:
                __import__(module_name)
                urls = sys.modules[module_name]
                if hasattr(urls, 'javascript_configuration'):
                    configuration[app_name] = urls.javascript_configuration()
            except ImportError:
                pass
        return configuration

    def get_configuration(self):
        if self.configuration is None:
            self.configuration = self.fetch()
        return self.configuration

DEFAULT_CONFIGURATION_BULDIER = ConfigurationBuilder()
