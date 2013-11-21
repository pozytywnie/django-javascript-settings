import sys


def runtests():
    from django.conf import settings

    if not settings.configured:
        settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS=(
                'javascript_settings',
            ),
        )

    # get_runner cannot be imported before settings are configured
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner(interactive=False)
    failures = test_runner.run_tests(['javascript_settings'])
    sys.exit(failures)

