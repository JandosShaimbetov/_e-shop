from rest_framework import serializers
from .models import Cart, CartItem, Order


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            "id",
            "product",
            "cart",
            "quantity",
            "cart_item_price",
        ]

        extra_kwargs = {
            "product": {"required": True},
            "cart": {"required": False},
            "quantity": {"required": True},
            "cart_item_price": {"required": False},
        }


class CartSerializer(serializers.ModelSerializer):

    cart_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "user", "cart_price", "date_creation", "is_paid"]

        extra_kwargs = {
            "user": {"required": False},
            "cart_price": {"required": False},
            "date_creation": {"required": False},
            "is_paid": {"required": False},
            "cart_price_sum": {"required": False},
        }

    def get_cart_price(self, obj):
        cart_price_sum = 0
        cart_id = obj.id
        cart_items = CartItem.objects.filter(cart=cart_id)
        for item in cart_items:
            if item.product.discount > 0:
                cart_price_sum += (
                    item.cart_item_price
                    - item.cart_item_price * item.product.discount
                )
            else:
                cart_price_sum += item.cart_item_price
        obj.cart_price = cart_price_sum
        obj.save()
        return obj.cart_price


class OrderSerializer(serializers.ModelSerializer):

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "cart", "user", "total_price", "date_creation"]

        extra_kwargs = {
            "cart": {"required": True},
            "user": {"required": False},
            "total_price": {"required": False},
            "date_creation": {"required": False},
        }

    def get_total_price(self, obj):
        obj.total_price = obj.cart.cart_price
        obj.save()
        return obj.total_price
