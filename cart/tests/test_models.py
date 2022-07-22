from django.test import TestCase
from user.models import CustomUser
from product.models import Product, ProductCategory
from ..models import Cart, CartItem, Order


class TestCartModel(TestCase):
    def test_price_method(self):
        user = CustomUser.objects.create_user(
            email="email@gmail.com", password="password"
        )
        cart = Cart.objects.create(user=user)
        self.assertEqual(cart.__str__(), f"price:{cart.cart_price}")


class TestOrderModel(TestCase):
    def test_total_price_method(self):
        user = CustomUser.objects.create_user(
            email="email@gmail.com", password="password"
        )
        cart = Cart.objects.create(user=user)
        order = Order.objects.create(cart=cart, user=user)
        self.assertEqual(order.__str__(), f"total price:{order.total_price}")


class TestCartItemModel(TestCase):
    def test_cart_item_price(self):
        user = CustomUser.objects.create_user(
            email="email@gmail.com", password="password"
        )
        cart = Cart.objects.create(user=user)
        category = ProductCategory.objects.create(name="tea")
        product = Product.objects.create(
            title="lipton", supplier=user, category=category, price=100
        )
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=100)
        self.assertEqual(
            cart_item.cart_item_price_without_discount,
            product.price * cart_item.quantity,
        )
