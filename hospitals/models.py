from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hospital(models.Model):
	nom = models.CharField(max_length=200)
	quartier = models.CharField(max_length=75)
	adresse = models.TextField(null=True)
	email = models.EmailField(max_length=254)
	phone_number1 = models.CharField(max_length=16)
	phone_number2 = models.CharField(max_length=16)
	specialite = models.CharField(max_length=50)
