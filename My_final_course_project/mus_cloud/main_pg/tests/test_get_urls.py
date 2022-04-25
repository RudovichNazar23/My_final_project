from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main_pg.views import main_page, your_profile

class TestUrls(SimpleTestCase):
    def test_main_page_view(self):
        url = reverse("main_page")
        self.assertEqual(resolve(url).func, main_page)

    def test_your_profile_view(self):
        url = reverse("your_profile")
        self.assertEqual(resolve(url).func, your_profile)