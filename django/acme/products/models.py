from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, db_column='id_category')
    name = models.CharField(max_length=50)
    ref = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='img', default='img/product_0_big.jpg')

    def __str__(self):
        return self.name