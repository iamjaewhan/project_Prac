from django.urls import path
from . import views as map_views

app_name="map"

urlpatterns=[
    path('',map_views.showmap,name='showmap'),
]