from rest_framework import serializers, fields, exceptions
from books.models import Book, BookImage, LendingAgreement, LendingRequest
from qualifierApp.models import Snippet

class FilterBookByUserSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        try:
            data = data.filter(user=self.context['request'].user)
        except:
            data = Book.objects.all()
        return super(FilterBookByUserSerializer, self).to_representation(data)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book.objects.all()
        list_serializer_class = FilterBookByUserSerializer
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



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # ['id', 'title', 'code', 'linenos']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(">>>>>>>> 2")
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        #instance.title = validated_data.get('title', instance.title)
        #instance.autor = validated_data.get('autor', instance.autor)
        #instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance