from django.test import TestCase
from django.urls import reverse
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
        #self.product = Product.objects.create(title='product 1')
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
		#headers = {'Content-Type': 'application/json', 'Accept-Encoding': None}
		data = json.dumps(data)
		self.client.login(username=self.user.username,
						password=self.password)
		response = self.client.post(self.url, data, content_type='application/json')
		data_response = response.json()
		book = Book.objects.get(title='Best Novel')
		allBooks = Book.objects.all()
		expected_response = {
			'id' : book.id,
			'user': self.user.pk,
			'author': 'Test Author',
			'title': 'Best Novel',
			'description': 'book about a novel',
			'genre': 'novel',
			'status': 'available',
			'cover': None
		}
		print(data_response, " ", response.status_code)
		print("------")
		print(allBooks)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(data_response, expected_response)