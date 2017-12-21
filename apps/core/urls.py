from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'core'

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet_list'),
    url(
        r'^snippets/(?P<pk>[\d]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet_detail'
    ),
    url(r'^users/$', views.UserList.as_view(), name='user_list'),
    url(
        r'^users/(?P<pk>[\d]+)/$',
        views.UserDetail.as_view(),
        name='user_detail'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
