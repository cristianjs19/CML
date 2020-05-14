from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from books.serializers import BookSerializer
from qualifierApp.models import Qualifier

# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from books.models import Book
from qualifierApp.serializers import  QualifierSerializer


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def makeBooking(request):
    return HttpResponse('Hello, world. You\'re at the polls index.')


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