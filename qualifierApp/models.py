from decimal import Decimal

from django.db import models
from django.db.models import CASCADE
from accounts.models import User
from books.models import LendingAgreement, Book

class Qualifier(models.Model):
    veracity_evaluation = models.CharField(max_length=30, null=True, blank=True)
    communication_evaluation = models.CharField(max_length=30, null=True, blank=True)
    cleaning_evaluation = models.CharField(max_length=30, null=True, blank=True)
    delivery_evaluation = models.CharField(max_length=30, null=True, blank=True)
    puntuality_evaluation = models.CharField(max_length=30, null=True, blank=True)

    # agreement = models.ForeignKey(LendingAgreement, on_delete=CASCADE)
    description = models.TextField(blank=False, default="")
    created = models.DateTimeField(auto_now_add=True)

    qualifying_user= models.ForeignKey(User, on_delete=CASCADE, related_name='qualifying_user')
    book = models.ForeignKey(Book, on_delete=CASCADE)

    class Meta:
        ordering = ['created']


class Qualification(models.Model):
    agreement_id = models.ForeignKey(LendingAgreement, on_delete=CASCADE)
    description = models.TextField(blank=False, default="")
    created = models.DateTimeField(auto_now_add=True)
    evaluated = models.ForeignKey(User, on_delete=CASCADE, related_name='evaluated')
    overall = models.DecimalField(max_digits=0, decimal_places=2, default=Decimal(0.00))
    class Meta:
        ordering = ['created']

cualificationType = [
    ('compliant', 'Compliant'),
    ('communication', 'Communication'),
    ('description', 'Description'),
    ('bookCare', 'BookCare'),
    #veracity
    #puntuality
    #delivery
]

class ScoreByQualification(models.Model):
    type = models.CharField(max_length=30, null=True, blank=True, choices=cualificationType)
    score = models.IntegerField(default=0)
    qualification_id = models.ForeignKey(Qualification, on_delete=CASCADE)