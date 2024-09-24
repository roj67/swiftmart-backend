from django.urls import path
from . import views

urlpatterns=[
    path("get-products/", views.get_products, name="get-products")
]