import json
import os.path
from tempfile import mkdtemp

from django.contrib.staticfiles.finders import BaseFinder
from django.contrib.staticfiles import utils
from django.core.files.storage import FileSystemStorage

from javascript_settings.configuration_builder import \
    DEFAULT_CONFIGURATION_BUILDER


class JavascriptSettingsFinder(BaseFinder):
    def __init__(self):
        self.file = JavascriptSettingsFile()
        self.file.create()

    def find(self, path, all=False):
        if path == self.file.get_name():
            static_path = self.file.get_path()
            if all:
                return [static_path]
            return static_path
        return []

    def list(self, ignore_patterns):
        storage = self._get_storage()
        for path in utils.get_files(storage, ignore_patterns):
            yield path, storage

    def _get_storage(self):
        return FileSystemStorage(location=self.file.get_directory())


class JavascriptSettingsFile(object):
    name = 'javascript-settings.js'
    tmp_directory_prefix = 'javascript-settings'

    def __init__(self):
        self.directory = self._create_tmp_directory()

    def _create_tmp_directory(self):
        return mkdtemp(prefix=self.tmp_directory_prefix)

    def get_directory(self):
        return self.directory

    def create(self):
        path = self.get_path()
        with open(path, 'w') as javascript_file:
            javascript_file.write(self._get_javascript_content())

    def get_path(self):
        return os.path.join(self.directory, self.name)

    def _get_javascript_content(self):
        configuration = self._get_javascript_configuration()
        return 'var configuration = %s;' % configuration

    def _get_javascript_configuration(self):
        configuration_dict = DEFAULT_CONFIGURATION_BUILDER.get_configuration()
        return json.dumps(configuration_dict)

    def get_name(self):
        return self.name
