from rest_framework import serializers, fields, exceptions
from books.models import Book, BookImage, LendingAgreement

class FilterByUserSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        try:
            data = data.filter(user=self.context['request'].user)
        except:
            data = Book.objects.all() #Una vez establecidos permisos, cambiar a raiseError.
        return super(FilterByUserSerializer, self).to_representation(data)


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        list_serializer_class = FilterByUserSerializer
        fields = '__all__'

class BookImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = '__all__'

class LendingAgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = LendingAgreement
        list_serializer_class = FilterByUserSerializer
        # fields = [
        #     'id',
        #     'description',
        #     'acepted',
        #     'deliver',
        #     'deliver_date',
        #     'give_back',
        #     'give_back_date',
        #     'extra',
        #     'extendable',
        #     'book_id',
        #     'owner_id',
        #     'user_id',
        #     'title',
        #     # 'lending_request_set',
        # ]                  
        fields = '__all__'

