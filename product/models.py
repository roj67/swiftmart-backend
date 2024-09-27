from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

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
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=True, default="")

    def __str__(self):
        return f"Image for {self.product.name}"


