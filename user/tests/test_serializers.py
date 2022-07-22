from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import CustomUser


class TestCustomUserRegisterSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("register-list")
        CustomUser.objects.create_user(email="email@gmail.com", password="password")

    def test_user_create(self):
        data = {
            "first_name": "jandos",
            "last_name": "shaimbetov",
            "email": "email@gmail.com",
            "password": "password",
            "check_password": "password",
            "address": "kol'baeva 32",
            "phone": "0500000000",
        }
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_invalid_password(self):
        data = {
            "first_name": "jandos",
            "last_name": "shaimbetov",
            "email": "email@gmail.com",
            "password": "not password",
            "check_password": "password",
            "address": "kol'baeva 32",
            "phone": "0500000000",
        }
        self.response = self.client.post(self.url, data, format="json")
        self.assertContains(self.response, text="invalid password", status_code=400)


class TestChangePasswordSerializer(APITestCase):
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

    def test_changed_password(self):
        data = {"old_password": "password", "new_password": "new password"}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)


class TestLogoutSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(email="email@gmail.com", password="password")
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "email@gmail.com", "password": "password"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="bearer " + access_token)
        self.url = reverse("auth_logout")

    def test_logout(self):
        refresh_token = self.res.data["refresh"]
        data = {"refresh": refresh_token}
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logout_unsuccessful(self):
        data = {"refresh": "1"}
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
