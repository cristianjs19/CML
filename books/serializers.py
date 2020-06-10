from rest_framework import serializers, fields, exceptions
from books.models import Book, BookImage, LendingAgreement

class FilterByUserSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        try:
            data = data.filter(user=self.context['request'].user)
        except:
            data = LendingAgreement.objects.all() #Una vez establecidos permisos, cambiar a raiseError.
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
        #     'message',
        #     'acceptance_date',
        #     'request_date',
        #     'deliver_date',
        #     'give_back',
        #     'give_back_date',
        #     'extra',
        #     'extendable',
        #     'book',
        #     'owner',
        #     'user',
        #     'status',
        #     'deliver',
        #     # 'lending_request_set',
        # ]                  
        fields = '__all__'

