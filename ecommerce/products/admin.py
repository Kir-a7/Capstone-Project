from django.contrib import admin
from .models import Category, Product, Wishlist, Order

# Register the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Only 'name' is available in the Category model
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

# Register the Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'created_date', 'image_url')
    list_filter = ('category',)
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)

# Register the Wishlist model
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_date')
    list_filter = ('user', 'added_date')
    search_fields = ('user__username', 'product__name')
    ordering = ('-added_date',)

admin.site.register(Wishlist, WishlistAdmin)
# Register the Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_date')
    list_filter = ('status', 'user', 'created_date')
    search_fields = ('user__username',)
    ordering = ('-created_date',)

admin.site.register(Order, OrderAdmin)
