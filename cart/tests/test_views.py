from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from user.models import CustomUser


class TestOrderView(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email="email@gmail.com", password="password"
        )
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"email": "email@gmail.com", "password": "password"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="bearer " + access_token)
        self.url = reverse("cart")

    def test_get_queryset_filter(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
