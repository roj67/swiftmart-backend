from rest_framework.serializers import ModelSerializer
from .models import Product, ProductImage

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'price', 'stock', 'reviews', 'reviewer_count', 'sizes', 'colors']

class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']
