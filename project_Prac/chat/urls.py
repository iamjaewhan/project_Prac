from django.urls import path
from . import views as chat_views

app_name="chat"

urlpatterns=[
    path('',chat_views.chatpage),
]