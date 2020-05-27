from rest_framework import serializers
from qualifierApp.models import Qualifier, Qualification, ScoreByQualification


class QualifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualifier
        fields = '__all__'  # ['id', 'title', 'code', 'linenos']

    def create(self, validated_data):
        return Qualifier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        # instance.autor = validated_data.get('autor', instance.autor)
        # instance.description = validated_data.get('description', instance.description)
        instance.agreement = 1
        instance.save()
        return instance


class ScoreByQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreByQualification
        fields = '__all__'


    def readOnlyField(self):
        model = ScoreByQualification
        fields = ['type', 'score']

    def create(self, validated_data):
        return ScoreByQualification.objects.create(**validated_data)

    def update(self, scoreInstance, validated_data):
        scoreInstance.save()
        return scoreInstance


class QualificationSerializerGET(serializers.ModelSerializer):
    scores = ScoreByQualificationSerializer(source='scorebyqualification_set', many=True)
    class Meta:
        model = Qualification
        fields = ["id", "agreement_id", "description", "created", "overall", "evaluated", "scores"
                  ]
    def create(self, validated_data):
        return Qualification.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.agreement = 1
        instance.save()
        return instance

class QualificationSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ["id", "agreement_id", "description", "created", "overall", "evaluated"]
    def create(self, validated_data):
        return Qualification.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.agreement = 1
        instance.save()
        return instance
