from rest_framework import serializers
from .models import Product, Category, Wishlist

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # Add the category name as a read-only field
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'category', 'category_name',
            'stock_quantity', 'image_url', 'created_date'
        ]

class WishlistSerializer(serializers.ModelSerializer):
    # Add additional fields to show product details in the wishlist
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.DecimalField(
        source="product.price", read_only=True, max_digits=10, decimal_places=2
    )

    class Meta:
        model = Wishlist
        fields = [
            'id', 'user', 'product', 'product_name', 'product_price', 'added_date'
        ]
