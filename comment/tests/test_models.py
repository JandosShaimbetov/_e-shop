from django.test import TestCase
from ..models import Comment
from user.models import CustomUser
from product.models import Product, ProductCategory


class TestCommentModel(TestCase):
    def test_model(self):
        author = CustomUser.objects.create_user(
            email="email@gmail.com", password="password"
        )
        category = ProductCategory.objects.create(name="tea")
        product = Product.objects.create(
            title="lipton", supplier=author, category=category
        )
        comment = Comment.objects.create(
            author=author, content="comment", products=product
        )
        self.assertEqual(
            comment.__str__(), f"author:{comment.author} comment:{comment.content}"
        )
