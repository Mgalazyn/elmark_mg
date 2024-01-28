from django.db import models
import uuid
from django.core.validators import MinValueValidator
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)
    parent_name = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Location(models.Model):
    room = models.CharField(max_length=50, blank=False)
    bookcase = models.CharField(max_length=50,blank=False)
    shelf = models.CharField(max_length=50, blank=False)
    cuvette = models.CharField(max_length=50, blank=False)
    column = models.CharField(max_length=50, blank=False)
    row = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return f"Room: {self.room} Bookcase: {self.bookcase}, shelf: {self.shelf}, cuvette: {self.cuvette}, column: {self.column}, row: {self.row}"


class Parts(models.Model):
    serial_number = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=False)
    quantity = models.IntegerField(blank=False, null=False,
                        validators=[MinValueValidator(1)])     #validation for min quantity of 1
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False,
                                validators=[MinValueValidator(0)])  #validation for only + prices, I allow 0 values bc maybe someone want to put part which is free.
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=False)

    def __str__(self):
        return self.name