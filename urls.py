from django.urls import path
from .views import user_registration, artist_registration
urlpatterns = [
    path("user_registration", user_registration, name="user_registration"),
    path("artist_registration", artist_registration, name="artist_registration")
]