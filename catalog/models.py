from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name
