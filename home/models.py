from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    desc = models.TextField(max_length=200)
       