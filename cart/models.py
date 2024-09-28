from django.db import models
from product.models import Product
from authentication.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
    

class WishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product.name
    

class CheckOut(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    street = models.CharField(max_length=250)
    extrafield = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    number = models.BigIntegerField()
    email = models.EmailField()
    save_info = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname + self.lastname
