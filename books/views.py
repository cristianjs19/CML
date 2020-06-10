from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .serializers import BookSerializer, BookImageSerializer, LendingAgreementSerializer
from accounts.models import User
from books.models import Book, LendingAgreement

class BookView(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class LendingAgreementView(viewsets.ModelViewSet):
	queryset = LendingAgreement.objects.all()
	serializer_class = LendingAgreementSerializer

	@action(detail=True, url_name='accept-agreement', serializer_class=LendingAgreementSerializer)
	def accept_agreement(self, request, pk=None):
		agreement = self.get_object()
		agreement.accept_agreement()
		content = {
		'message': 'acuerdo aceptado exitosamente'
		}
		return Response(content, status=status.HTTP_200_OK)



