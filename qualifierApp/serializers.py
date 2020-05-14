from rest_framework import serializers
from qualifierApp.models import Qualifier

class QualifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualifier
        fields = '__all__' # ['id', 'title', 'code', 'linenos']

    def create(self, validated_data):
        return Qualifier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #instance.title = validated_data.get('title', instance.title)
        #instance.autor = validated_data.get('autor', instance.autor)
        #instance.description = validated_data.get('description', instance.description)
        instance.agreement = 1
        instance.save()
        return instance