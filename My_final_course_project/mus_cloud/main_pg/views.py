from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SongForm, AlbumForm
from .models import Song, User
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
class FileFieldView(FormView):
    form_class = AlbumForm
    template_name = 'post_album.html'  # Replace with your template.
    success_url = 'main_page'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('album')
        if form.is_valid():
            for f in files:
                f.save()
            return messages.success(request, "saved successfully")
        else:
            return messages.error(request, "something is going wrong , please, try again")

'''def post_album(request):
    if request.method == "GET":
        return render(request, "main_pg/post_album.html")

    elif request.method == "POST":
        album_form = AlbumForm(request.POST)

        if album_form.is_valid():
            files = album_form.cleaned_data["album"]

            for f in files:
                f.save()
            messages.success(request, "saved successfully")
            return redirect("post_album")

        else:
            messages.error(request, "something is going wrong , please, try again")
            return redirect("post_album")'''

@csrf_exempt
def find_other_users(request):
    if request.method == "GET":
        all_users = {
            "users": User.objects.all()
        }
        print(all_users)
        return render(request, "main_pg/find_other_users.html", all_users)

    elif request.method == "POST":
        pass
