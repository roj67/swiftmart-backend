from django.urls import path
from . import views

urlpatterns=[
    path("", views.ProductView.as_view(), name="product-list"),
    path("<str:id>/", views.ProductDetailView.as_view(), name="product-detail"),
]