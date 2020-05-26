from django.urls import path

from . import views

urlpatterns = [

    path('', views.qualifier_list),
    path('all', views.qualification),
    path('score', views.scoreByQualification),
    path('all/<int:pk>', views.qualification_byId),
    path('<int:pk>', views.qualifier_detail)
]
