from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^registration$', views.registration),
    url(r'^$', views.index),
    url(r'^loggedin$', views.loggedin),#for testing purposes
]
