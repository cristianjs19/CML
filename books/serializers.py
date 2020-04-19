from rest_framework import serializers, fields, exceptions
from books.models import Book, BookImage, LendingAgreement, LendingRequest




class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class BookImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = '__all__'

class LendingAgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = LendingAgreement
        fields = '__all__'                

class LendingRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

        