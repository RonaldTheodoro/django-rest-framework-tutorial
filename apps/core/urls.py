from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'core'

urlpatterns = [
    url(r'^snippets/$', views.snippet_list, name='list'),
    url(r'^snippets/(?P<pk>[\d]+)/$', views.snippet_detail, name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
