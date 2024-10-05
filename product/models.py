import os
import uuid
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    
    def __str__(self):
        return self.name

class ProductSize(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name + " : " + self.value

class ProductColor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name + " : " + self.value

class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True, default=0)
    reviews = models.FloatField(blank=True, null=True)
    reviewer_count = models.IntegerField(blank=True, null=True)
    sizes = models.ManyToManyField(ProductSize, blank=True)
    colors = models.ManyToManyField(ProductColor, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
def get_guid_filename(instance, filename):
    guid = str(uuid.uuid4())
    ext = filename.split('.')[-1]
    return f"{guid}.{ext}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(null=True, default="", upload_to=get_guid_filename)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


    def __str__(self):
        return f"Image for {self.product.name}"
    
class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_image")
    image = models.ImageField(null=True, default="", upload_to=get_guid_filename)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.category.name}"
    

   


