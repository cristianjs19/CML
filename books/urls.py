from django.urls import path
from rest_framework import routers
# enrrollment resources
from books.views import BookViewSet, LendingAgreementViewSet, LendingRequestViewSet


router = routers.DefaultRouter()

router.register('books', BookViewSet)
router.register('acuerdo', LendingAgreementViewSet)
router.register('solicitarlibro', LendingRequestViewSet)


urlpatterns = router.urls