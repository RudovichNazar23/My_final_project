from django.shortcuts import render, redirect, get_object_or_404
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


'''class AlbumFormView(FormView):
    form_class = AlbumForm
    template_name = 'post_album.html'  # Replace with your template.
    success_url = 'post_album'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('album')
        if form.is_valid():
            for f in files:
                f.save()  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)'''


@csrf_exempt
def find_other_users(request):
    all_users = {
        "users": User.objects.all()
    }
    search_form = SearchUserForm(request.GET)

    return render(request, "main_pg/find_other_users.html", all_users)


@csrf_exempt
def other_user_profile(request, id_user: int):
    user = get_object_or_404(User, id=id_user)
    user_posts = {
        "posts": Song.objects.filter(user=user)
    }
    return render(request, "main_pg/other_user_profile.html", {"posts": user_posts,
                                                               "user": user}, )
