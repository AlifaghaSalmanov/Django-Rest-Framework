from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True, blank=True, default="Baku")

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="products"
    )
    price = models.FloatField(max_length=255)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images/")
