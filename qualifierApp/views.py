from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from qualifierApp.models import Qualifier, Qualification, ScoreByQualification
from rest_framework.parsers import JSONParser
from books.models import Book
from qualifierApp.serializers import QualifierSerializer, QualificationSerializer, ScoreByQualificationSerializer


@csrf_exempt
def qualifier_list(request):
    if request.method == 'GET':
        qualifier = Qualifier.objects.all()
        serializer = QualifierSerializer(qualifier, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QualifierSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def qualifier_detail(request, pk):
    try:
        qualifier = Qualifier.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QualifierSerializer(qualifier)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QualifierSerializer(qualifier, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        qualifier.delete()
        return HttpResponse(status=204)



@csrf_exempt
def qualification(request):
    if request.method == 'GET':
        qualifier = Qualification.objects.all()
        serializer = QualificationSerializer(qualifier, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QualificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


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
        serializer = QualificationSerializer(qualification)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QualificationSerializer(qualification, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        qualification.delete()
        return HttpResponse(status=204)
