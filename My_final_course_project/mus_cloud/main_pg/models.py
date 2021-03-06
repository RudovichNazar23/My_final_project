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

class User_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_link = models.URLField(max_length=500, null=True)
    second_link = models.URLField(max_length=500, null=True)
    email = models.EmailField(max_length=500, null=True)

    def __str__(self):
        return f"{self.user}"

class User_wall_post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(null=True, default="")
    date_of_post = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"

class Main_page_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(null=True, default="")
    date_post = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"