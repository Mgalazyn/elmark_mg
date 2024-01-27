from django.db import models
import uuid
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)
    parent_name = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Location(models.Model):
    room = models.CharField(max_length=50)
    bookcase = models.CharField(max_length=50)
    shelf = models.CharField(max_length=50)
    cuvette = models.CharField(max_length=50)
    column = models.CharField(max_length=50)
    row = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Room: {self.room} Bookcase: {self.bookcase}, shelf: {self.shelf}, cuvette: {self.cuvette}, column: {self.column}, row: {self.row}"


class Parts(models.Model):
    serial_number = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.name