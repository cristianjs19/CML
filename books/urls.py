from django.urls import path
from rest_framework import routers
# enrrollment resources
from books.views import BookView, LendingAgreementView


router = routers.DefaultRouter()

router.register('books', BookView)
router.register('lendingagreement', LendingAgreementView)


urlpatterns = router.urls