from django.contrib import admin

# Register your models here.
from app1.models import Car, Address

admin.site.register(Car)
admin.site.register(Address)