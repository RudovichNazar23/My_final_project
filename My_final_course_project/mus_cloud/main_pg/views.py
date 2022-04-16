from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SongForm, AlbumForm, SearchUserForm
from .models import Song, User, Album
from django.contrib import messages
from django.views.generic.edit import FormView


@csrf_exempt
def main_page(request):
    if request.method == "GET":
        return render(request, "main_pg/main_page.html")

    elif request.method == "POST":
        pass


@csrf_exempt
def your_profile(request):
    if request.method == "GET":
        user_post = {
            "posts": Song.objects.filter(user=request.user)
        }
        print(user_post)
        return render(request, "main_pg/your_profile.html", user_post)

    elif request.method == "POST":
        pass


@csrf_exempt
def post_song(request):
    if request.method == "GET":
        return render(request, "main_pg/post_song.html")

    elif request.method == "POST":
        song_form = SongForm(request.POST, request.FILES)

        if song_form.is_valid():
            user = Song(user=request.user, **song_form.cleaned_data)
            user.save()
            messages.success(request, "OK")
            return redirect("post_song")

        else:
            messages.error(request, "please, try again")
            return redirect("post_song")

@csrf_exempt
def post_album(request):
    if request.method == "GET":
        form = AlbumForm()
        return render(request, "main_pg/post_album.html", {"form": form})

    elif request.method == "POST":

        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():

            album = Album(album_editor=request.user, **form.cleaned_data)
            album.save()
            messages.success(request, "saved successfully")
            return redirect("post_album")

        else:
            messages.error(request, "please, try again")
            return redirect("post_album")


@csrf_exempt
def find_other_users(request):
    if request.method == "GET":
        all_users = {
            "users": User.objects.all()
        }
        print(all_users)
        return render(request, "main_pg/find_other_users.html", all_users)


