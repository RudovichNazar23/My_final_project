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