from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    path('auth/google/url/', views.google_login_url, name='google_login_url'),
    path('auth/google/callback/', views.google_callback, name='google_callback'),

    path('users/register-user/', views.RegisterView.as_view(), name='register-user')
]