from django.urls import path
from .views import main_page, your_profile, post_song, find_other_users, FileFieldView
urlpatterns = [
    path("main_page", main_page, name="main_page"),
    path("your_profile", your_profile, name="your_profile"),
    path("post_song", post_song, name="post_song"),
    path("find_other_users", find_other_users, name="find_other_users"),
    path("post_album", FileFieldView, name="post_album")
]

