from django.test import TestCase
from ..models import CustomUser


class TestCustomUserModel(TestCase):
    def test_model(self):
        user = CustomUser.objects.create_user(
            email="email@gmail.com", password="password"
        )
        self.assertEqual(user.__str__(), user.email)
