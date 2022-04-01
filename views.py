from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import ArtistRegistrationForm
from .models import Artist, User


@csrf_exempt
def user_registration(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "registration/user_registration.html", {"form": form})

    elif request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            reg = login(request, user)

            artist = Artist.save(user)
            print(artist)
            '''if user in Artist.person:
                artist_form = ArtistRegistrationForm(request.POST)
                if artist_form is not None:
                    artist_form.save()
                    print("You are an artist")
                else:
                    return HttpResponse("NOT")
            else:
                return HttpResponse("YOU ARE NOT IN ARTIST TABLE !")'''

            print("AUTHENTICATE", user)
            print("USERNAME", username)
            print("PASSWORD", password)
            return redirect("artist_registration")

        else:
            return HttpResponse("NO")


@csrf_exempt
def artist_registration(request):
    if request.method == "GET":
        return render(request, "registration/artist_registration.html")

    elif request.method == "POST":
        artist_form = ArtistRegistrationForm(request.POST)
        if artist_form is not None:
            artist_form.save()
            print("You are an artist")
        else:
            return HttpResponse("NOT")