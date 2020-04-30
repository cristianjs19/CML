from rest_framework import serializers, fields, exceptions
from books.models import Book, BookImage, LendingAgreement, LendingRequest

class FilterByUserSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        try:
            data = data.filter(user=self.context['request'].user)
        except:
            data = LendingAgreement.objects.all() #Una vez establecidos permisos, cambiar a raiseError.
        return super(FilterByUserSerializer, self).to_representation(data)


class BookSerializer(serializers.ModelSerializer):
    # list_serializer = serializers.SerializerMethodField()

    # def get_list_serializer(self, data):
    #     serializer = FilterByUserSerializer()
    #     try:
    #         data = serializer.to_representation()
    #     except:
    #         data = Book.objects.all()
    #     return super(BookSerializer, self).get_list_serializer()

    class Meta:
        model = Book
        list_serializer_class = FilterByUserSerializer
        fields = '__all__'

class BookImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = '__all__'


class LendingAgreementSerializer(serializers.ModelSerializer):
    #lending_request = LendingRequestSerializer(many=True)

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

class LendingRequestSerializer(serializers.ModelSerializer):
    lending_agreement_set = LendingAgreementSerializer(many=True)

    class Meta:
        model = LendingRequest
        list_serializer_class = FilterByUserSerializer
        fields = '__all__'