from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Spec(models.Model):
    character = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gear(models.Model):
    name = models.CharField(max_length=100)
    slot = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    enchant = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
