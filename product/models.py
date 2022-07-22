from django.db import models
from user.models import CustomUser


class ProductCategory(models.Model):

    name = models.CharField(max_length=55, unique=True, verbose_name="name")

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(max_length=155, verbose_name="title")
    description = models.TextField()
    picture = models.ImageField(
        blank=True, null=True, upload_to="images/", default="default_product.png"
    )
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, null=True, related_name="category"
    )
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
