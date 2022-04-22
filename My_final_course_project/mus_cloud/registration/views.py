from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages

@csrf_exempt
def main(request):
    if request.user.is_authenticated:
        print(request.user)
        return redirect("main_page")
    else:
        return redirect("registration")


@csrf_exempt
def registration(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "registration/registration.html", {"form": form})

    elif request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            print(username)

            password_1 = form.cleaned_data.get("password1")
            print(password_1)

            password_2 = form.cleaned_data.get("password2")
            print(password_2)

            if password_1 == password_2:
                user = authenticate(username=username, password=password_1)

                login(request, user)

                return redirect("login")

            else:
                return messages.error(request, "passwords don't match")

        else:
            messages.error(request, "username or password are not correct: "
                                    "check password or username")
            return redirect("registration")


@csrf_exempt
def user_log_in(request):
    if request.method == "GET":
        log_in_form = LoginForm()
        return render(request, "registration/login.html", {"log_in_form": log_in_form})

    elif request.method == "POST":

        log_in_form = LoginForm(request.POST)

        username = log_in_form.data.get("username")
        print(username)

        password = log_in_form.data["password"]
        print(password)

        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)

                return redirect("main_page")
            else:
                messages.error("your account disabled !") # CHECK IT !!!!!

                return redirect("login")

        else:
            messages.error(request, "username or password are not correct")
            return redirect("login")


@csrf_exempt
def user_log_out(request):
    user = request.user
    logout(request)
    print(user)
    return redirect("login")

