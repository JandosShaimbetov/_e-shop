from ..models import Product, ProductCategory
from user.models import CustomUser
from django.test import TestCase


class TestProductModel(TestCase):
    def test_model(self):
        user = CustomUser.objects.create_user(
            email="email@gmail.com", password="password"
        )
        category = ProductCategory.objects.create(name="tea")
        product = Product.objects.create(
            title="lipton", supplier=user, category=category, price=100
        )
        self.assertEqual(product.__str__(), product.title)


class TestProductCategoryModel(TestCase):
    def test_model(self):
        category = ProductCategory.objects.create(name="tea")
        self.assertEqual(category.__str__(), category.name)
