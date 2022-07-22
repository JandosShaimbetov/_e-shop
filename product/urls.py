from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register(r"product", ProductModelViewSet, basename="product")
router.register(r"category", CategoryModelViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
