from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^v1/intruders/list/$', views.intruder_list, name='intruder_list'),
    url(r'^v1/intruders/add/$', views.arduino_post, name='arduino_post'),
)