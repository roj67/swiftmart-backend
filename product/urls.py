from django.urls import path
from . import views

urlpatterns=[
    path("", views.ProductView.as_view(), name="product-list"),
    path("images/", views.ProductImageView.as_view(), name="image-add"),
    path("images/<str:id>", views.ProductImageDetailView.as_view(), name="image-detail"),
    path("<str:id>/", views.ProductDetailView.as_view(), name="product-detail"),
]