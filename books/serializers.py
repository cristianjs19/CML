from rest_framework import serializers, fields, exceptions
from books.models import Book, BookImage, LendingAgreement, LendingRequest

class FilterBookByUserSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        try:
            data = data.filter(user=self.context['request'].user)
        except:
            data = Book.objects.all()
        return super(FilterBookByUserSerializer, self).to_representation(data)


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         list_serializer_class = FilteredOrderSerializer


# class ProductSerializer(serializers.ModelSerializer):
#     order_set = OrderSerializer(many=True, read_only=True)

#     class Meta:
#         model = Product


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
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

        