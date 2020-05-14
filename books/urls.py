from django.urls import path
from rest_framework import routers
# enrrollment resources
from books.views import BookView, LendingAgreementView, LendingRequestView


router = routers.DefaultRouter()

router.register('books', BookView)
router.register('acuerdo', LendingAgreementView)
router.register('solicitarlibro', LendingRequestView)


urlpatterns = router.urls