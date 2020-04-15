from django.db import models
from django.db.models import CASCADE
import datetime

from accounts.models import User


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

class Book(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=CASCADE)
	author = models.CharField(max_length=150, null=True, blank=False)
	title = models.CharField(max_length=150, null=True, blank=False)
	description = models.CharField(max_length=200,null=True, blank=True)
	genre = models.CharField(max_length=30 , choices=GENRES)
	status = models.CharField(max_length=30 , choices=STATUS)
	cover = models.ImageField(upload_to='images/book_images', null=True, blank=True)	


class BookImage(models.Model):
    product = models.ForeignKey(Book, null=False, blank=False, related_name='images', on_delete=CASCADE)
    image = models.ImageField(upload_to='images/book_images', null=True, blank=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name_plural = "BookImages"

class LendingAgreement(object):
	user = models.ForeignKey(User, on_delete=CASCADE)
	owner = models.ForeignKey(User, on_delete=CASCADE)
	book = models.ForeignKey(Book, on_delete=CASCADE)
	description = models.TextField(blank=False, default="")
	acepted = models.DateField(auto_now_add=True, default=datetime.date.today)
	deliver = models.Charfield(max_length=50)
	deliver_date = models.DateField(blank=False)
	give_back = models.Charfield(max_length=50)
	give_back_date = models.DateField(blank=False)
	extra = models.Charfield(max_length=50)

	def __str__(self):
        return self.product

class LendingRequest(object):
	title = models.Charfield(max_length=100)
	message = models.TextField(max_length=300)
	agreement = models.OneToOneField(LendingAgreement, on_delete=CASCADE)