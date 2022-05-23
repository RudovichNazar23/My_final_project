from django import forms
from .models import Album, Song, User_profile, User_wall_post


class SongForm(forms.Form):
    name_song = forms.CharField(max_length=100)
    song = forms.FileField()


class AlbumForm(forms.Form):
    name_album = forms.CharField(max_length=100)
    album = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))

class SearchUserForm(forms.Form):
    username = forms.CharField(max_length=100)

class Add_more_info(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ["first_link", "second_link", "email"]

class SearchToDeleteSong(forms.Form):
    name_song = forms.CharField(max_length=100)

class DeleteSongForm(forms.Form):
    song = forms.CharField(max_length=100)

class Add_Text_Post(forms.ModelForm):
    class Meta:
        model = User_wall_post
        fields = ["post"]