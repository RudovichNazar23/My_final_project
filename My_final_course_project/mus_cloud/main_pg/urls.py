from django.urls import path
from .views import main_page, your_profile, post_song, search_user, post_album, other_user_profile, add_more_information, delete_song, deleting_process, view_songs, view_albums
from .views import other_user_songs, other_user_albums
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("main_page", main_page, name="main_page"),
    path("your_profile", your_profile, name="your_profile"),
    path("post_song", post_song, name="post_song"),
    path("search_user", search_user, name="search_user"),
    path("post_album", post_album, name="post_album"),
    path("user/<int:id_user>", other_user_profile, name="other_user_profile"),
    path("add_more_information", add_more_information, name="add_more_information"),
    path("delete_song", delete_song, name="delete_song"),
    path("deleting_song/<int:id_song>", deleting_process, name="deleting_song"),
    path("view_songs",  view_songs, name="view_songs"),
    path("view_albums", view_albums, name="view_albums"),
    path("user/<int:id_user>/songs", other_user_songs, name="songs"),
    path("user/<int:id_user>/albums", other_user_albums, name="albums")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )