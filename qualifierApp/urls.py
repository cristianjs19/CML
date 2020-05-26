from django.urls import path

from . import views

urlpatterns = [

    path('', views.qualifier_list),
    path('<int:pk>', views.qualifier_detail)
]
