from rest_framework import viewsets, mixins
from .serializers import BookSerializer, BookImageSerializer, LendingAgreementSerializer
from accounts.models import User
from books.models import Book, LendingAgreement

class BookView(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class LendingAgreementView(viewsets.ModelViewSet):
	queryset = LendingAgreement.objects.all()
	serializer_class = LendingAgreementSerializer


