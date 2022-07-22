from rest_framework import viewsets, permissions
from .serializers import CommentSerializer
from .models import Comment


class CommentModelViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
