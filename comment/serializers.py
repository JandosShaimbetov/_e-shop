from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "rate",
            "content",
            "date_creation",
            "replies",
            "products",
        ]

        extra_kwargs = {
            "rate": {"required": True},
            "content": {"required": True},
            "date_creation": {"required": False},
            "replies": {"required": False},
        }
