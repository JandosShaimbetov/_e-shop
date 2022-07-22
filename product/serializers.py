from rest_framework import serializers
from .models import ProductCategory, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "picture",
            "price",
            "discount",
            "category",
            "supplier",
            "date_creation",
        ]

        extra_kwargs = {
            "title": {"required": True},
            "description": {"required": True},
            "price": {"required": True},
            "category": {"required": True},
        }
