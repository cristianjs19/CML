from django.urls import path
from rest_framework import routers
# enrrollment resources
from books.views import BookViewSet


router = routers.DefaultRouter()

router.register('', BookViewSet)


urlpatterns = router.urls