from django.conf.urls import url
from . import views

urlpatterns = [
    #/game/
    url(r'^$', views.index, name='index'),

    #/game/1/
    url(r'^(?P<shelfNum>[0-9]+)/$', views.detail, name='detail'),

    #/game/1/3
    url(r'^(?P<shelfNum>[0-9]+)/(?P<compartmentNum>[0-9]+)/$', views.moredetail, name='moredetail'),
]