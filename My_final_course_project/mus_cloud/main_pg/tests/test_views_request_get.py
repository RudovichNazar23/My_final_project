from django.test import TestCase, Client
from django.urls import reverse
from main_pg.views import main_page

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_Main_page_view(self):
        response = self.client.get(reverse("main_page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main_pg/main_page.html")