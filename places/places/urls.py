from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^variables/', views.PlaceList, name='placeList'),
    url(r'^variablecreate/$', csrf_exempt(views.PlaceCreate), name='placeCreate'),
]