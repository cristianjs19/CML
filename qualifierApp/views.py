from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from qualifierApp.models import Qualification, ScoreByQualification
from rest_framework.parsers import JSONParser
from books.models import Book
from qualifierApp.serializers import QualificationSerializerGET, ScoreByQualificationSerializer, \
    QualificationSerializerPOST


@csrf_exempt
def qualification(request):
    if request.method == 'GET':
        qualifier = Qualification.objects.all()
        serializer = QualificationSerializerGET(qualifier, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QualificationSerializerPOST(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def qualification_byQualifiedUser(request, userId):
    if request.method == 'GET':
        try:
            qualification = Qualification.objects.filter(evaluated=userId)
        except Qualification.DoesNotExist:
            return HttpResponse(status=404)
        serializer = QualificationSerializerGET(qualification, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def scoreByQualification(request):
    if request.method == 'GET':
        scoreByQualification_data = ScoreByQualification.objects.all()
        scoreByQualification_set = ScoreByQualificationSerializer(scoreByQualification_data, many=True)
        return JsonResponse(scoreByQualification_set.data, safe=False)

    elif request.method == 'POST':
        scoreByQualification_data = JSONParser().parse(request)
        scoreByQualification_set = ScoreByQualificationSerializer(data=scoreByQualification_data)
        if scoreByQualification_set.is_valid():
            scoreByQualification_set.save()
            calculateOveroll(scoreByQualification_data)
            return JsonResponse(scoreByQualification_set.data, status=201)
        return JsonResponse(scoreByQualification_set.errors, status=400)

def calculateOveroll(scoreByQualification_data):
    qualification = Qualification.objects.get(pk=scoreByQualification_data.get('qualification_id'))
    scores = qualification.scorebyqualification_set.all()
    total = 0
    for score in scores:
        total = total+ score.score
    qualification.overall = total/scores.count()
    qualification.save(update_fields=['overall'])

@csrf_exempt
def qualification_byId(request, pk):
    try:
        qualification = Qualification.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QualificationSerializerGET(qualification)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QualificationSerializerGET(qualification, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        qualification.delete()
        return HttpResponse(status=204)

