from django.conf.urls import url, include
from . import views
from rest_framework import routers

urlpatterns = [
    #/
    url(r'^$', views.index, name='game'),


    #/game/1/
    url(r'^(?P<shelfNum>[0-9]+)/$', views.detail, name='detail'),

    #/game/1/3
    url(r'^(?P<shelfNum>[0-9]+)/(?P<compartmentNum>[0-9]+)/$', views.moredetail, name='moredetail'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]