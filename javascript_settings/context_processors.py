from configuration_builder import DEFAULT_CONFIGURATION_BUILDER

from django.utils import simplejson

def get_config(request):
    return { 'javascript_settings': simplejson.dumps(DEFAULT_CONFIGURATION_BUILDER.get_configuration()) }
