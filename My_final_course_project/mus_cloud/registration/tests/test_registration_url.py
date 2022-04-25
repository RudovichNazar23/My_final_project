from django.test import SimpleTestCase
from registration.views import registration, user_log_in, main
from django.urls import reverse, resolve
from django.contrib.auth.models import User

class TestRegistrationUrls(SimpleTestCase):
    def test_registration_url(self):
        url = reverse("registration")
        self.assertEqual(resolve(url).func, registration)

    def test_login_url(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func, user_log_in)

    def test_main_url(self):
        url = reverse("main")
        self.assertEqual(resolve(url).func, main)
