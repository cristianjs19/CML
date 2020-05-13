from django.urls import path

from . import views
from rest_framework import routers


urlpatterns = [

    path('', views.index, name='makeBooking'),
    path('index', views.index, name='index'),
    path('lama', views.BookSerializer),
    path('list', views.snippet_list),
    path('list/<int:pk>/', views.snippet_detail)
]

#router = routers.DefaultRouter()
#router.register('lama', views.BookViewSet)