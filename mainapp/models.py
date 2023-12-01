import os.path
import uuid

from django.db import models


# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(null=True)
    number_of_people = models.IntegerField()
    message = models.TextField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'
        ordering = ["name"]
