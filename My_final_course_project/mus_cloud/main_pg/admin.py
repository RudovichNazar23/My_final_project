from django.contrib import admin
from .models import Song, Album, User_profile, User_wall_post

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(User_profile)
admin.site.register(User_wall_post)