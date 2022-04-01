from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")

class Song(models.Model):
    song_name = models.CharField(max_length=100, default="")
    editor_song = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Album(models.Model):
    album_name = models.CharField(max_length=100, default="")
    editor_album = models.ForeignKey(Artist, on_delete=models.CASCADE)

