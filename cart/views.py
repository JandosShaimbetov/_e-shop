from .serializers import CartSerializer, CartItemSerializer, OrderSerializer
from .models import Cart, CartItem, Order
from rest_framework.response import Response
from rest_framework import generics, status


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(is_paid=False, user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartItemView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            cart = serializer.validated_data["cart"]
            if cart.is_paid:
                return Response({"Purchase is already done!"})
            cart.is_paid = True
            cart.save()
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
