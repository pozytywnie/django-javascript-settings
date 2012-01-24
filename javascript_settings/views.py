from django.http import HttpResponse
from django.utils import simplejson

from configuration_builder import DEFAULT_CONFIGURATION_BUILDER

def load_configuration(request):
    return HttpResponse("var configuration = %s;" % simplejson.dumps(
        DEFAULT_CONFIGURATION_BUILDER.get_configuration()
    ))

