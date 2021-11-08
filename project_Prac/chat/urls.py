from django.urls import path
from . import views as chat_views

app_name="chat"

urlpatterns=[
    path('',chat_views.chatpage),
    path('<str:room_name>/',chat_views.chatroom, name='chatroom'),
]