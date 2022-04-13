from django.urls import path
from .views import registration, user_log_in, main

urlpatterns = [
    path('registration', registration, name="registration"),
    path('login', user_log_in, name="login"),
    path('', main, name="main"),
]
