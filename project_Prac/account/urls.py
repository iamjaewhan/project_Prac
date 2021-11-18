from django.urls import path
from . import views as account_views

app_name="account"

urlpatterns=[
    path('',account_views.getaddress,name='getaddress'),
]