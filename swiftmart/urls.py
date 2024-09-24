from django.contrib import admin
from django.urls import path, include

api_url = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),

    path(api_url, include('authentication.urls')),
    path(api_url, include('product.urls')),
]
