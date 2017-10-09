from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^register', views.register),
        url(r'^login', views.login),
        url(r'^dashboard', views.dashboard),
        url(r'^logout', views.logout),
        url(r'^add$', views.add),
        url(r'^add/(?P<item_num>\d+)$', views.add_to),
        url(r'^create', views.create),
        url(r'^remove/(?P<item_num>\d+)$', views.remove),
        url(r'^delete/(?P<item_num>\d+)$', views.delete),
        url(r'^(?P<item_num>\d+)$', views.show),
]
