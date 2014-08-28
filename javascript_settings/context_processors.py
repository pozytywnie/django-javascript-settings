import json

from configuration_builder import DEFAULT_CONFIGURATION_BUILDER


def get_config(request):
    return {
        'javascript_settings': json.dumps(
            DEFAULT_CONFIGURATION_BUILDER.get_configuration()
        )
    }
