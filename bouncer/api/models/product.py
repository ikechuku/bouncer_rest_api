from django.db import models
from .category import Category
from .vendor import Vendor


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
