from django import forms
from .models import Album, Song


class SongForm(forms.Form):
    name_song = forms.CharField(max_length=100)
    song = forms.FileField()


class AlbumForm(forms.Form):
    name_album = forms.CharField(max_length=100)
    album = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

class SearchUserForm(forms.Form):
    username = forms.CharField(max_length=100)

class Add_more_info(forms.Form):
    telegram_link = forms.URLField(max_length=1000)
    instagram_link = forms.URLField(max_length=1000)