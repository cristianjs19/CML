from accounts.models import User

from django.db import models
from django.db.models import CASCADE
import datetime



GENRES = [
	('action', 'Action'),
	('novel', 'Novel'),
	('fiction', 'Fiction'),
]
BOOK_STATUS = [
	('available', 'Available'),
	('unavailable', 'Unavailable'),
	('hidden', 'Hidden'),
]
REQUEST_STATUS = [
	('onArrange', 'On Arrange'),
	('accepted', 'Accepted'),
	('ended', 'Ended'),
]
EXTENDABLE = [
	('yes', 'Yes'),
	('no', 'No'),
	('later', 'Later'),
]
CONDITION = [
	('offer', 'Offer'),
	('request', 'Request'),
]

class Book(models.Model):
	user = models.ForeignKey(User, on_delete=CASCADE)
	author = models.CharField(max_length=150, null=True, blank=False)
	title = models.CharField(max_length=150, null=True, blank=False)
	description = models.CharField(max_length=200,null=True, blank=True)
	message = models.CharField(max_length=200,null=True, blank=True)
	condition = models.CharField(max_length=30 , null=False, blank=False, choices=CONDITION)
	genre = models.CharField(max_length=30 , null=True, blank=True, choices=GENRES)
	status = models.CharField(max_length=30 , null=True, blank=False, choices=BOOK_STATUS)
	cover = models.ImageField(upload_to='images/book_images', null=True, blank=True)

	def __str__(self):
		return self.title	


class BookImage(models.Model):
	book = models.ForeignKey(Book, null=False, blank=False, related_name='images', on_delete=CASCADE)
	image = models.ImageField(upload_to='images/book_images', null=True, blank=True)

	def __str__(self):
		return self.book

	class Meta:
		verbose_name_plural = "BookImages"

class LendingAgreement(models.Model):
	user = models.ForeignKey(User, on_delete=CASCADE, related_name='user')
	owner = models.ForeignKey(User, on_delete=CASCADE, related_name='owner')
	book = models.ForeignKey(Book, on_delete=CASCADE)
	status = models.CharField(max_length=30 , null=False, blank=False, default="onArrange", choices=REQUEST_STATUS)
	request_date = models.DateField(auto_now_add=True, editable=False)
	acceptance_date = models.DateField(null=True)
	message = models.TextField(blank=False, default="")
	deliver = models.CharField(max_length=50) # especifica como se hará la entrega.
	deliver_date = models.DateField(blank=False)
	give_back = models.CharField(max_length=50) # especifica como se hará la devolución.
	give_back_date = models.DateField(blank=False)
	extra = models.CharField(max_length=50, null=True, blank=True) # posibilidad de solicitar extra ej, copia de dni.
	extendable = models.CharField(max_length=30 , null=True, blank=True, choices=EXTENDABLE)

	def __str__(self):
		return self.book.title