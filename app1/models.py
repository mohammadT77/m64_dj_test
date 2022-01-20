from django.db import models
from core.models import Brand


# Create your models here.

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
    color = models.CharField(max_length=3, choices=[
        ('BLK', 'Black'),
        ('GRE', 'Green'),
        ('BLU', 'Blue'),
        ('RED', 'Red'),
    ], null=True, default=None)
    acceleration = models.IntegerField()

    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Car {self.id} {self.brand}"