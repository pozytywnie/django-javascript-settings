from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('javascript_configuration.views',
    url(r'^configuration.js$', 'load_configuration', name='javascript-configuration'),
)
