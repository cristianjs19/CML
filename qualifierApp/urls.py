from django.conf.urls import url
from django.urls import path, re_path

from . import views

urlpatterns = [

    path('', views.qualification),
    path('scores', views.scoreByQualification),
    path('<int:pk>', views.qualification_byId),
]
