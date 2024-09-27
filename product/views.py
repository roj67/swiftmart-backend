from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from drf_yasg.utils import swagger_auto_schema
from .models import Product
from .serializers import ProductSerializer


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

class ProductView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsStaff()]
        return [AllowAny()]

    def get(self, request):
        products = Product.objects.all()
        serialize = ProductSerializer(products, many=True)
        return Response(serialize.data)
    
    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": serializer.data}, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsStaff()]

    def get(self, request, id):
        product = Product.objects.get(id=id)
        serialize = ProductSerializer(product)
        return Response(serialize.data)
    
    @swagger_auto_schema(request_body=ProductSerializer)
    def patch(self, request, id):
        try:
            product = Product.objects.get(id = id)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"message": "Product Does Not Exist!"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ProductSerializer)
    def put(self, request, id):
        return self.patch(request=request, id=id)
    
    def delete(self, request, id):
        try:
            product : Product = Product.objects.get(id=id)
            product.delete()
            return Response({"message": "Product Deleted!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Product Couldn't Be Deleted!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
