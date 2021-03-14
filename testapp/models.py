from django.db import models

# Create your models here.

class Library(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=40)
    book=models.CharField(max_length=100)
    date_of_issue=models.DateField()
    return_date=models.DateField()
