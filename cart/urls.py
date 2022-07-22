from django.urls import path

from .views import *

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("cart/<int:pk>/", CartDetailView.as_view(), name="cart-detail"),
    path("cart-item/", CartItemView.as_view(), name="cart-item"),
    path("cart-item/<int:pk>/", CartItemDetailView.as_view(), name="cart-item-detail"),
    path("order/", OrderView.as_view(), name="cart"),
    path("order/<int:pk>/", OrderDetailView.as_view(), name="cart-detail"),
]
