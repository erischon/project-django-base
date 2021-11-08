from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from accounts.models import CustomUser


class CookbookModelsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='usertest',
            email='usertest@erischon.dev',
            password='testpass123'
        )

    def test_customuser_name(self):
        """ """
        custom_user = CustomUser.objects.last()
        custom_user__name = custom_user.email

        self.assertEquals(custom_user__name, str(custom_user))