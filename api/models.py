from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)
    parent_name = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Parts(models.Model):
    serial_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.JSONField()

    def __str__(self):
        return self.name