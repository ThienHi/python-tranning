from django.db import models
from django.utils import timezone

# Create your models here.


class Music(models.Model):
    nameSong = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(
        default=timezone.datetime.now, widget=models.TextInput(attrs={'class': 'create-at'}))


# class Singers(models.Model):
#     nameSong = models.CharField(max_length=100)
#     nameSinger = models.CharField(max_length=50)
