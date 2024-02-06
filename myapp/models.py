from django.db import models

# Create your models here.


class Product(models.Model):
    Product_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    def __str__(self):
        return self.product_name


class Product_sub_cat(models.Model):
    subcategory_id = models.IntegerField()
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cprice = models.IntegerField()
    cimage = models.FileField(upload_to='images/')
    cname = models.CharField(max_length=200)

    def __str__(self):
        return self.cname