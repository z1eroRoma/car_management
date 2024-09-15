from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    DoesNotExist = None
    objects = None
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

