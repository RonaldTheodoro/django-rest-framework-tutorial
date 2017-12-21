from django.conf.urls import url

from . import views


app_name = 'core'

urlpatterns = [
    url(r'^$', views.snippet_list, name='list'),
    url(r'^(?P<pk>[\d]+)/$', views.snippet_detail, name='detail'),
]