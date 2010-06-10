from django.conf.urls.defaults import *

urlpatterns = patterns('taggit_autocomplete.views',
    url(r'^list$', 'list_tags', name='taggit_autocomplete-list'),
)
