from django.urls import path
from .views import main_page, your_profile, post_song, find_other_users, post_album, other_user_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("main_page", main_page, name="main_page"),
    path("your_profile", your_profile, name="your_profile"),
    path("post_song", post_song, name="post_song"),
    path("find_other_users", find_other_users, name="find_other_users"),
    path("post_album", post_album, name="post_album"),
    path("user/<int:id_user>", other_user_profile, name="other_user_profile")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )