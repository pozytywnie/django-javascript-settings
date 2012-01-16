from configuration_builder import DEFAULT_CONFIGURATION_BULDIER

from django.utils import simplejson

def get_config(request):
    return { 'javascript_configuration': simplejson.dumps(DEFAULT_CONFIGURATION_BULDIER.get_configuration()) }
