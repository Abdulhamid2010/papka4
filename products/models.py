from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.PositiveIntegerField()      
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.IntegerField(default=5)  

    def __str__(self):
        return self.name