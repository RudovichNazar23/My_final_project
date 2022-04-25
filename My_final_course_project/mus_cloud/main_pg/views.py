from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import SongForm, AlbumForm
from .models import Song, User, Album
from django.contrib import messages

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
            "posts": Song.objects.filter(user=request.user),
            "albums": Album.objects.filter(album_editor=request.user)
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
        files = request.FILES.getlist("album")
        name_album = form.data.get("name_album")
        if form.is_valid():
            for file in files:
                album = Album(album_editor=request.user, album=file, name_album=name_album)
                album.save()
            messages.success(request, "saved successfully")
            return redirect("post_album")

        else:
            messages.error(request, "please, try again")
            return redirect("post_album")


def search_user(request):
    if request.method == "POST":

        username = request.POST["username"]
        result = User.objects.filter(
            username__contains=username
        )
        return render(request, "main_pg/search_user.html", {"username": username,
                                                            "results": result})

    else:

        all_users = {
            "users": User.objects.all()
        }
        return render(request, "main_pg/search_user.html", all_users)


@csrf_exempt
def other_user_profile(request, id_user: int):
    user = get_object_or_404(User, id=id_user)
    user_post = Song.objects.filter(user=user)
    user_album = Album.objects.filter(album_editor=user)
    context = {
        "user": user,
        "user_posts": user_post,
        "user_album": user_album
    }
    print(context)
    return render(request, "main_pg/other_user_profile.html", context)
