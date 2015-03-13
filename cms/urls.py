from django.conf.urls import patterns, url, include
from cms import views

urlpatterns = patterns('',
    url(r'^intruder/$', views.intruder_list, name='intruder_list'),
    url(r'^intruder/add/$', views.intruder_edit, name='intruder_add'),
    url(r'^intruder/mod/(?P<intruder_id>\d+)/$', views.intruder_edit, name='intruder_mod'),
    url(r'^intruder/del/(?P<intruder_id>\d+)/$', views.intruder_del, name='intruder_del'),
)