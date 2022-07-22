from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import CustomUser


class TestCardModelViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(email="email@gmail.com", password="password")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "email@gmail.com", "password": "password"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="bearer " + access_token)
        self.url = reverse("card-list")


class TestUpdatePassword(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(email="email@gmail.com", password="password")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "email@gmail.com", "password": "password"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="bearer " + access_token)
        self.url = reverse("change-password")

    def test_invalid_old_password(self):
        data = {"old_password": "not password", "new_password": "new password"}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_serializer(self):
        data = {}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
