from pyexpat import model
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name