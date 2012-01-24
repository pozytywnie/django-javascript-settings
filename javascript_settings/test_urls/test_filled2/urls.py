

def javascript_settings():
    """
    Testing object for javascript-configuration module.
    """
    js_conf_level2_test3 = {
        'level3 test1': 1,
        'level3 test2': 2,
        'level3 test3': 3,
    }
    js_conf = {
        'level1 test1': 1,
        'level1 test2': {
            'level2 test1': 1,
            'level2 test2': 2,
            'level2 test3': js_conf_level2_test3,
        },
        'level1 test3': 2,
    }

    return js_conf
