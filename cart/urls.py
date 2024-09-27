from django.urls import path
from . import views


urlpatterns = [
    path("wishlist/", view=views.WishListView.as_view(), name="wishlist-list"),
    path("wishlist/<str:id>", view=views.WishListDetail.as_view(), name="wishlist-detail"),
    
    path("", view=views.CartListView.as_view(), name="cart-list"),
    path("<str:id>/", view=views.CartDetailView.as_view(), name="cart-detail"),
]