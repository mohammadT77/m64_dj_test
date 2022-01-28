from django.db import models
from core.models import Brand, BaseModel


# Create your models here.

class Car(BaseModel):

    class Meta:
        ordering = ['brand', '-acceleration']
        db_tablespace = 'test'

    brand = models.ForeignKey(Brand, on_delete=models.SET(1))
    color = models.CharField(max_length=3, choices=[
        ('BLK', 'Black'),
        ('GRE', 'Green'),
        ('BLU', 'Blue'),
        ('RED', 'Red'),
    ], null=True, default=None)
    acceleration = models.IntegerField()

    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Car {self.id}#: acc: {self.acceleration}, color: {self.color} ({self.brand})"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)


