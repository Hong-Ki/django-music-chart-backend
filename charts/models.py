from django.db import models


class Song(models.Model):
    rank = models.IntegerField()
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
