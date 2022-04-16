from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_song = models.CharField(max_length=100, default="")
    song = models.FileField(upload_to="media/", default=None)

    def __str__(self):
        return f"{self.user} : {self.name_song}"

class Album(models.Model):
    album_editor = models.ForeignKey(User, on_delete=models.CASCADE)
    name_album = models.CharField(max_length=100)
    album = models.FileField(upload_to="media/albums", default=None)

    def __str__(self):
        return f"{self.album_editor} : {self.name_album}"
