from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='makeBooking'),
    path('index', views.index, name='index'),
]