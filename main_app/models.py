from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Spec(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Gear(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    # spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
    spec = models.CharField(max_length=50)

    def __str__(self):
        return self.name