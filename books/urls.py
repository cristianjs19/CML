from django.urls import path
from rest_framework import routers
# enrrollment resources
from books.views import BookView, BookRequestView, PublicRequestView


router = routers.DefaultRouter()

router.register('books', BookView)
router.register('bookrequest', BookRequestView)
router.register('publicrequest', PublicRequestView)


urlpatterns = router.urls