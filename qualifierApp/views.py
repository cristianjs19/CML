from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, filters
from rest_framework.viewsets import ModelViewSet

from qualifierApp.models import Qualifier, Qualification, ScoreByQualification
from rest_framework.parsers import JSONParser
from books.models import Book
from qualifierApp.serializers import QualifierSerializer, QualificationSerializerGET, ScoreByQualificationSerializer, \
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
def qualification_byQualifiedUser(request):
    if request.method == 'GET':
        userId = request.GET.get('user_id', '')
        try:
            qualification = Qualification.objects.filter(evaluated=userId)
        except Qualification.DoesNotExist:
            return HttpResponse(status=404)
        serializer = QualificationSerializerGET(qualification, many=True)
        return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def scoreByQualification(request):
    if request.method == 'GET':
        scoreByQualification = ScoreByQualification.objects.all()
        serializer = ScoreByQualificationSerializer(scoreByQualification, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScoreByQualificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


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

