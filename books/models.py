from django.db import models
from django.db.models import CASCADE

from accounts.models import Account


GENRES = [
	('action', 'Action'),
	('novel', 'Novel'),
	('fiction', 'Fiction'),
]

# Create your models here.

class Book(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(Account, on_delete=CASCADE)
	author = models.CharField(max_length=150, null=True, blank=False)
	title = models.CharField(max_length=150, null=True, blank=False)
	description = models.CharField(max_length=200,null=True, blank=True)
	genre = models.CharField(max_length=30 , choices=GENRES)


class BookImage(models.Model):
    """
    Images for products
    """
    product = models.ForeignKey(Book, null=False, blank=False, related_name='images', on_delete=CASCADE)
    image = models.ImageField(upload_to='images/book_images', null=True, blank=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name_plural = "BookImages"