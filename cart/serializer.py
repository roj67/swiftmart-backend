from rest_framework.serializers import ModelSerializer
from .models import Cart, WishList

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'stock']

class WishListSerializer(ModelSerializer):
    class Meta:
        model = WishList
        fields = ['id', 'product']