from rest_framework import generics, permissions
from django.views.generic import TemplateView
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly

class ProductListView(TemplateView):
    template_name = 'inventory/products.html'

class OrderListView(TemplateView):
    template_name = 'inventory/orders.html'

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()
        product = order.product
        product.stock = max(product.stock - order.quantity, 0)
        product.save()

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            from rest_framework.response import Response
            from rest_framework import status
            return Response({'detail': 'Only admin can delete orders.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
