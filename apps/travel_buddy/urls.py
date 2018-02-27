from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.travels),#needs rework
    url(r'^add$', views.add),
    url(r'^adding_trip$', views.adding_trip),
    url(r'^logout$', views.logout),
    url(r'^destination$', views.destination),
    url(r'^join$', views.join),
]
