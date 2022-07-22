from django.db import models
from user.models import CustomUser
from product.models import Product


class Comment(models.Model):
    choices = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=choices, blank=True, null=True)
    content = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    replies = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"author:{self.author} comment:{self.content}"
