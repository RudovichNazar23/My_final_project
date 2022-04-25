from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main_pg.views import main_page, your_profile, post_song, post_album, search_user, other_user_profile

class TestUrls(SimpleTestCase):
    def test_main_page_view(self):
        url = reverse("main_page")
        self.assertEqual(resolve(url).func, main_page)

    def test_your_profile_view(self):
        url = reverse("your_profile")
        self.assertEqual(resolve(url).func, your_profile)

    def test_post_song_view(self):
        url = reverse("post_song")
        self.assertEqual(resolve(url).func, post_song)

    def test_post_album_view(self):
        url = reverse("post_album")
        self.assertEqual(resolve(url).func, post_album)

    def test_search_user_view(self):
        url = reverse("search_user")
        self.assertEqual(resolve(url).func, search_user)

