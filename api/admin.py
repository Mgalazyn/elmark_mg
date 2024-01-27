from django.contrib import admin
from .models import Parts, Categories, Location

# Register your models here.

admin.site.register(Parts)
admin.site.register(Location)
admin.site.register(Categories)