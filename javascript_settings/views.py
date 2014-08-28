import json

from django.http import HttpResponse

from configuration_builder import DEFAULT_CONFIGURATION_BUILDER


def load_configuration(request):
    return HttpResponse(
        "var configuration = %s;" % json.dumps(
            DEFAULT_CONFIGURATION_BUILDER.get_configuration()
        )
    )
