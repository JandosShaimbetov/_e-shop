from django.db import models
from user.models import CustomUser
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    cart_price = models.FloatField(default=1)
    date_creation = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"cart price: {self.cart_price}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart")
    quantity = models.PositiveIntegerField(default=1)
    cart_item_price = models.FloatField(default=0, blank=True)

    def save(self, *args, **kwargs):
        self.cart_item_price = self.quantity * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"cart item price: {self.cart_item_price}"


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    total_price = models.FloatField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"total price:{self.total_price}"
