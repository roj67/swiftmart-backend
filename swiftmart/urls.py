from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static

api_url = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),

    path(api_url, include('authentication.urls')),
    path(api_url + 'products/', include('product.urls')),
    path(api_url + 'carts/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

schema_view = get_schema_view(
    openapi.Info(
      title="Swiftmart API",
      default_version='v1',
      description="API for swiftmart",
      terms_of_service="https://www.google.com/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="swiftmark license"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

