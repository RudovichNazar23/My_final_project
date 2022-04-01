from django import forms
from .models import Artist

class ArtistRegistrationForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ["person", "nickname", "city"]
