from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.ProductColor)
admin.site.register(models.ProductSize)
admin.site.register(models.ProductImage)
