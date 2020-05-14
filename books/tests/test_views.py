from django.test import TestCase
from django.urls import reverse
from django.core import serializers
#from model_bakery import baker
from books.models import Book, LendingAgreement, LendingRequest
from accounts.models import User
from rest_framework.test import APIClient
from rest_framework import status
import json

class BookViewTest(TestCase):
	url = "http://localhost:8000/books/books/"

	def setUp(self):
		self.password = "qwer1234"
		self.user = User.objects.create_user(username='cristian',
											password=self.password)
		self.book = Book.objects.create(title='book_test',
										user=self.user)
	def get_client(self):
		client = APIClient()
		client.login(username=self.user.username, password=self.password)
		return client

	def test_create_book(self):
		client = self.get_client()
		data = {
		'user': self.user.pk,
		'author': 'Test Author',
		'title': 'Best Novel',
		'description': 'book about a novel',
		'genre': 'novel',
		'status': 'available'
		}
		data = json.dumps(data)
		self.client.login(username=self.user.username,
						password=self.password)
		response = self.client.post(self.url, data, content_type='application/json')
		data_response = response.json()
		book = Book.objects.get(title='Best Novel')
		allBooks = Book.objects.all()
		allBooks_json = serializers.serialize('json', allBooks)
		expected_response = {
			'id' : book.id,
			'user': self.user.pk,
			'author': book.author,
			'title': book.title,
			'description': 'book about a novel',
			'genre': 'novel',
			'status': 'available',
			'cover': None
		}
		# print(data_response, "****", response.status_code)
		# print("------")
		# print(allBooks.values())
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(data_response, expected_response)

	def test_update_book(self):
		book_url = "http://localhost:8000/books/books/1/"
		client = self.get_client()
		data = {
		'user': self.user.pk,
		'author': 'Other Author',
		'title': 'Other Book',
		'description': 'book about a novel',
		'genre': 'novel',
		'status': 'available'
		}
		data = json.dumps(data)
		self.client.login(username=self.user.username,
						password=self.password)
		response = self.client.patch(book_url, data, content_type='application/json')
		book = self.client.get(book_url, content_type='application/json')
		book_response = book.json()
		expected_response = {
			'id' : book_response['id'],
			'user': self.user.pk,
			'author': 'Other Author',
			'title': 'Other Book',
			'description': 'book about a novel',
			'genre': 'novel',
			'status': 'available',
			'cover': None
		}
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(book_response, expected_response)