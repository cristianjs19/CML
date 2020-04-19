from accounts.models import User

from django.db import models
from django.db.models import CASCADE
import datetime



GENRES = [
	('action', 'Action'),
	('novel', 'Novel'),
	('fiction', 'Fiction'),
]
STATUS = [
	('available', 'Available'),
	('lended', 'Lended'),
	('hidden', 'Hidden'),
]
EXTENDABLE = [
	('yes', 'Yes'),
	('no', 'No'),
	('later', 'Later'),
]

class Book(models.Model):
	user = models.ForeignKey(User, on_delete=CASCADE)
	author = models.CharField(max_length=150, null=True, blank=False)
	title = models.CharField(max_length=150, null=True, blank=False)
	description = models.CharField(max_length=200,null=True, blank=True)
	genre = models.CharField(max_length=30 , null=True, blank=True, choices=GENRES)
	status = models.CharField(max_length=30 , null=True, blank=False, choices=STATUS)
	cover = models.ImageField(upload_to='images/book_images', null=True, blank=True)	


class BookImage(models.Model):
	product = models.ForeignKey(Book, null=False, blank=False, related_name='images', on_delete=CASCADE)
	image = models.ImageField(upload_to='images/book_images', null=True, blank=True)

	def __str__(self):
		return self.product

	class Meta:
		verbose_name_plural = "BookImages"

class LendingAgreement(models.Model):
	user = models.ForeignKey(User, on_delete=CASCADE, related_name='user')
	owner = models.ForeignKey(User, on_delete=CASCADE, related_name='owner')
	book = models.ForeignKey(Book, on_delete=CASCADE)
	description = models.TextField(blank=False, default="")
	acepted = models.DateField(auto_now_add=True, editable=False)
	deliver = models.CharField(max_length=50) # especifica como se hará la entrega.
	deliver_date = models.DateField(blank=False)
	give_back = models.CharField(max_length=50) # especifica como se hará la devolución.
	give_back_date = models.DateField(blank=False)
	extra = models.CharField(max_length=50, null=True, blank=True) # posibilidad de solicitar extra ej, copia de dni.
	extendable = models.CharField(max_length=30 , null=True, blank=True, choices=EXTENDABLE)

	def __str__(self):
		return self.product

class LendingRequest(models.Model):
	title = models.CharField(max_length=100)
	message = models.TextField(max_length=300)
	agreement = models.ForeignKey(LendingAgreement, on_delete=CASCADE)