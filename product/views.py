from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_products(request):
    product = [
        {
            'id': '1',
            'name': 'Shirt',
            'category': 'Cloths',
        },
        {
            'id': '2',
            'name': 'Pant',
            'category': 'Cloths',
        },
        {
            'id': '3',
            'name': 'Phone',
            'category': 'Electronics',
        }
    ]
    return Response(product)
