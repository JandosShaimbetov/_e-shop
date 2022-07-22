from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from user.models import CustomUser
from ..models import Cart, CartItem, Order
from product.models import Product, ProductCategory


class TestCartSerializer(APITestCase):
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

    def test_cart_price(self):
        category = ProductCategory.objects.create(name="tea")
        product = Product.objects.create(
            title="lipton", supplier=self.user, category=category, price=100
        )
        self.cart = self.client.post(self.url, format="json")
        url = reverse("cart-item")
        self.cart_item = self.client.post(url, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


class TestOrderSerializer(APITestCase):
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
        category = ProductCategory.objects.create(name="tea")
        product = Product.objects.create(
            title="lipton", supplier=self.user, category=category, price=100
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(
            product=product, cart=self.cart, quantity=100
        )
        self.cart_res = self.client.get(reverse("cart-detail", args=[self.cart.id]))
        self.order = Order.objects.create(user=self.user, cart=self.cart)

    def test_total_price(self):
        self.url = reverse("cart-detail", args=[self.order.id])
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
