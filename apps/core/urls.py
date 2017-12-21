from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'core'

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(), name='list'),
    url(
        r'^snippets/(?P<pk>[\d]+)/$',
        views.SnippetDetail.as_view(),
        name='detail'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
