from component import Component
from django.conf.urls.defaults import patterns, include, url
from django.core import urlresolvers
from package_installer import Package


class JavaScriptConfigurationPackage(Package):
    INSTALL_APPS = ('javascript_configuration',)
    def get_urls(self):
        return patterns('',
            url('^javascript_configuration/', include('javascript_configuration.urls'))
        )

PACKAGE = JavaScriptConfigurationPackage()

class JavaScriptConfiguration(Component):
    REQUIRE_PACKAGES = ['javascript_configuration']
    def javascript(self):
        file = urlresolvers.reverse('javascript-configuration')
        return '<script type="text/javascript" src="%s"></script>\n' % file
