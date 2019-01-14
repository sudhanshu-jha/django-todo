from django.conf.urls import url

from . import views


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^add", views.add, name="add"),
    url(r"^details/(?P<id>\w{0,50})/$", views.details),
    # url(r'^details/(?P<id>\)/$', views.details),
    url(r"^edit/(?P<pk>\d+)/detail/$", views.edit),
    url(r"^delete/(?P<pk>\d+)/detail/$", views.delete),
]
