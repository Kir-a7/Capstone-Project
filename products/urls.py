from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('wishlist/', views.WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]
