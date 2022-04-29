from django.urls import path
from . import views as views

app_name="payment"

urlpatterns=[
    path('', views.payment, name='payment'),
    path('approval/', views.approval, name='approval')
]