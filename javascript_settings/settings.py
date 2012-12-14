from django.conf import settings

SCAN_MODULES = getattr(
    settings,
    'JAVASCRIPT_SETTINGS_SCAN_MODULES',
    dict([(app_name.split('.')[-1], app_name + ".urls")
          for app_name in settings.INSTALLED_APPS])
)
