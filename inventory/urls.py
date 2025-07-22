from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    # Product API
    path('api/products/', views.ProductListCreateAPIView.as_view(), name='api-products-list-create'),
    path('api/products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='api-products-detail'),
    # Order API
    path('api/orders/', views.OrderListCreateAPIView.as_view(), name='api-orders-list-create'),
    path('api/orders/<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view(), name='api-orders-detail'),
]
