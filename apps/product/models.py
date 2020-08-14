from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    stock = models.IntegerField(null= True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name