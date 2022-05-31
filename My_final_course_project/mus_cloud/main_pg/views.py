from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .forms import SongForm, AlbumForm, Add_more_info, Add_Text_Post, Add_Post_at_Main_Page
from .models import Song, User, Album, User_profile, User_wall_post, Main_page_Post
from django.contrib import messages
from django.core.paginator import Paginator


@csrf_exempt
def add_post_at_main_page(request):
    if request.method == "GET":
        form = Add_Post_at_Main_Page()
        return render(request, "main_pg/add_post.html", {"form": form})

    elif request.method == "POST":
        form = Add_Post_at_Main_Page(request.POST)
        if form.is_valid():
            data = Main_page_Post(user=request.user, **form.cleaned_data)
            data.save()
            messages.success(request, "Ok")
            return redirect("add_post")

        else:
            messages.error(request, "something is going wrong")
            return redirect("add_post")


@csrf_exempt
def main_page(request):
    if request.method == "GET":
        posts = Main_page_Post.objects.all()

        pag_posts = Paginator(posts, 2)

        page = request.GET.get("page")

        view_posts = pag_posts.get_page(page)

        return render(request, "main_pg/main_page.html", {"view_posts": view_posts})


@csrf_exempt
def add_more_information(request):
    if request.method == "GET":
        form = Add_more_info()
        return render(request, "main_pg/add_more_info.html", {"form": form})

    elif request.method == "POST":
        info_form = Add_more_info(request.POST)
        if info_form.is_valid():
            info = User_profile(user=request.user, **info_form.cleaned_data)
            info.save()
            messages.success(request, "added !")
            return redirect("add_more_information")

        else:
            messages.error(request, "not valid")
            return redirect("add_more_information")


@csrf_exempt
def your_profile(request):
    if request.method == "GET":
        info = User_profile.objects.filter(user=request.user)
        posts = User_wall_post.objects.filter(user=request.user)

        p_posts = Paginator(posts, 1)

        page = request.GET.get("page")

        post = p_posts.get_page(page)

        return render(request, "main_pg/your_profile.html", {"info": info,
                                                             "posts": post})


@csrf_exempt
def post_news(request):
    if request.method == "GET":
        form = Add_Text_Post()
        return render(request, "main_pg/add_text_post.html", {"form": form})

    elif request.method == "POST":
        form = Add_Text_Post(request.POST)
        if form.is_valid():
            user_post = User_wall_post(user=request.user, **form.cleaned_data)
            user_post.save()
            messages.success(request, "saved successfully")
            return redirect("post_news")

        else:
            messages.error(request, "try again, your form is not valid")
            return redirect("post_news")


@csrf_exempt
def view_songs(request):
    if request.method == "GET":
        songs = Song.objects.filter(user=request.user)

        p_songs = Paginator(songs, 1)

        page = request.GET.get("page")

        song = p_songs.get_page(page)

        return render(request, "main_pg/song_page.html", {"songs": song})


@csrf_exempt
def view_albums(request):
    if request.method == "GET":
        albums = Album.objects.filter(album_editor=request.user)

        p_albums = Paginator(albums, 1)

        page = request.GET.get("page")

        album = p_albums.get_page(page)

        return render(request, "main_pg/album_page.html", {"albums": album})


@csrf_exempt
def post_song(request):
    if request.method == "GET":
        return render(request, "main_pg/post_song.html")

    elif request.method == "POST":
        song_form = SongForm(request.POST, request.FILES)

        if song_form.is_valid():
            user = Song(user=request.user, **song_form.cleaned_data)
            user.save()
            messages.success(request, "Saved successfully")
            return redirect("post_song")

        else:
            messages.error(request, "please, try again")
            return redirect("post_song")


@csrf_exempt
def delete_song(request):
    if request.method == "POST":

        name_song = request.POST["name_song"]
        result = Song.objects.filter(
            name_song__contains=name_song
        )
        return render(request, "main_pg/delete_song.html", {"results": result})

    else:
        user_songs = Song.objects.filter(user=request.user)
        return render(request, "main_pg/delete_song.html", {"songs": user_songs})


@csrf_exempt
def deleting_process(request, id_song: int):
    if request.method == "GET":
        song = Song.objects.filter(id=id_song)
        return render(request, "main_pg/deleting_song.html", {"song": song})

    elif request.method == "POST":
        song = Song.objects.filter(id=id_song)
        song.delete()
        return redirect("your_profile")


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
            messages.success(request, "Saved successfully")
            return redirect("post_album")

        else:
            messages.error(request, "please, try again")
            return redirect("post_album")

@csrf_exempt
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
    user_posts = User_wall_post.objects.filter(user=user)

    p_user_posts = Paginator(user_posts, 1)

    page = request.GET.get("page")

    posts_of_user = p_user_posts.get_page(page)

    context = {
        "user": user,
        "posts_of_user": posts_of_user
    }

    return render(request, "main_pg/other_user_profile.html", context)

@csrf_exempt
def other_user_songs(request, id_user: int):
    if request.method == "GET":
        user = User.objects.filter(id=id_user)
        songs = Song.objects.filter(user__id__in=user)

        p_songs = Paginator(songs, 1)

        page = request.GET.get("page")

        song = p_songs.get_page(page)

        return render(request, "main_pg/other_user_songs.html", {"g": song})


@csrf_exempt
def other_user_albums(request, id_user: int):
    if request.method == "GET":
        user = User.objects.filter(id=id_user)

        albums = Album.objects.filter(album_editor__id__in=user)

        p_albums = Paginator(albums, 1)

        page = request.GET.get("page")

        album = p_albums.get_page(page)

        return render(request, "main_pg/other_user_albums.html", {"al": album})