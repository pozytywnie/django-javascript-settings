from django.test import TestCase

from javascript_settings.configuration_builder import ConfigurationBuilder
from javascript_settings import settings


class VariousUrlsTest(TestCase):
    """
        This class represents tests with various urls.py
        injected to the settings.SCAN_MODULES
    """

    def setUp(self):
        """
            Clearing SCAN_MODULES
        """
        self.SCAN_MODULES = settings.SCAN_MODULES
        settings.SCAN_MODULES = {}

    def tearDown(self):
        """
            Restoring SCAN_MODULES
        """
        settings.SCAN_MODULES = self.SCAN_MODULES

    def assertBuildConfiguration(self, scan_modules, expected):
        """
            Check whether ConfigurationBuilder return what is expected.
        """
        settings.SCAN_MODULES = scan_modules

        conf_builder = ConfigurationBuilder()
        generated_conf = conf_builder.get_configuration()
        self.assertEqual(generated_conf, expected)

    def test_without_urls(self):
        """
            Test with no urls.py defined. It should return an empty
            dict.
        """
        self.assertBuildConfiguration({}, {})

    def test_with_correct_empty_urls(self):
        """
            Test with urls.py specified, but each without relevant
            javascript_settings function.
        """
        empty_test_module = 'javascript_settings.test_urls.test_empty.urls'
        empty_test_module_name = 'test_empty'
        test_scan_modules = {empty_test_module_name: empty_test_module}
        expected = {empty_test_module_name: {}}

        self.assertBuildConfiguration(test_scan_modules, expected)

    def test_with_correct_urls(self):
        """
            Test with correct urls.py defined in SCAN_MODULES.
        """
        test_module = 'javascript_settings.test_urls.test_filled2.urls'
        test_module_name = 'test_filled2'
        test_scan_modules = {test_module_name: test_module}

        from javascript_settings.test_urls.test_filled2.urls import \
            javascript_settings
        test_content = javascript_settings()

        expected = {test_module_name: test_content}

        self.assertBuildConfiguration(test_scan_modules, expected)

    def test_with_many_correct_urls(self):
        """
            Test with correct and simple urls.py defined in SCAN_MODULES.
        """
        test_modules = {
            'test_filled1': 'javascript_settings.test_urls.test_filled1.urls',
            'test_filled2': 'javascript_settings.test_urls.test_filled2.urls',
        }

        from javascript_settings.test_urls.test_filled1.urls import \
            javascript_settings
        test_content1 = javascript_settings()

        from javascript_settings.test_urls.test_filled2.urls import \
            javascript_settings as javascript_settings2
        test_content2 = javascript_settings2()

        expected = {
            'test_filled1': test_content1,
            'test_filled2': test_content2,
        }

        self.assertBuildConfiguration(test_modules, expected)
