from django.test import TestCase
from django.contrib.auth.models import User


class UserModelCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="Max",
            password="123"
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.user.username, str)
        self.assertIsInstance(self.user.password, str)

