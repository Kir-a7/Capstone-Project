from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework import generics, permissions
from .models import Product, Category, Wishlist, Order, OrderItem
from .serializers import ProductSerializer, CategorySerializer, WishlistSerializer, OrderSerializer, OrderItemSerializer
import logging
from rest_framework.response import Response
from rest_framework import status


def validate_stock_for_order(order_items):
    for item in order_items:
        product = item.product
        if product.stock_quantity < item.quantity:
            raise ValidationError(
                f"Not enough stock for product '{product.name}'. Available stock: {product.stock_quantity}."
            )

def update_stock_after_order(order_items):
    for item in order_items:
        product = item.product
        product.stock_quantity -= item.quantity
        product.save()

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WishlistListCreateView(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        order = serializer.save(user=user)  # Save the order first
        
        # Get the order items and perform stock validation
        order_items = order.items.all()
        validate_stock_for_order(order_items)

        # Update the stock quantities after validation
        update_stock_after_order(order_items)



# Get an instance of a logger
logger = logging.getLogger(__name__)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            # Ensure only valid status changes are allowed (e.g., prevent changing to invalid statuses)
            status = request.data.get("status")
            if status and status not in dict(Order.STATUS_CHOICES):
                return Response({"detail": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)

            return self.update(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error during PATCH for Order ID {kwargs['pk']}: {str(e)}")
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            # Optionally, check if the order is in a state that allows deletion (e.g., not completed or canceled)
            if order.status in [Order.COMPLETED, Order.CANCELLED]:
                return Response(
                    {"detail": "Cannot delete completed or canceled orders."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return self.destroy(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error during DELETE for Order ID {kwargs['pk']}: {str(e)}")
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
