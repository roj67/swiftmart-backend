from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from .models import Cart, Product, WishList
from .serializer import CartSerializer, WishListSerializer


class CartListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.filter(user = request.user)
        serializer = CartSerializer(cart, many = True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=CartSerializer)
    def post(self, request):
        serailizer = CartSerializer(data=request.data)
        if serailizer.is_valid():
            try:
                product = Product.objects.get(id = int(serailizer.data['product']))
                Cart.objects.create(
                    user = request.user,
                    product = product,
                    stock = int(serailizer.data['stock'])
                )
                return Response(serailizer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": serailizer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            cart_item : Cart = Cart.objects.get(id = id)
            cart_item.delete()
            return Response({"message": "Cart Item Deleted!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class WishListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.method)
        wishlist = WishList.objects.filter(user = request.user)
        serializer = WishListSerializer(wishlist, many = True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=WishListSerializer)
    def post(self, request):
        serailizer = WishListSerializer(data=request.data)
        if serailizer.is_valid():
            try:
                product = Product.objects.get(id = int(serailizer.data['product']))
                WishList.objects.create(
                    user = request.user,
                    product = product,
                )
                return Response(serailizer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": serailizer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class WishListDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            wishlist_item : WishList = WishList.objects.get(id = id)
            wishlist_item.delete()
            return Response({"message": "WishList Item Deleted!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)