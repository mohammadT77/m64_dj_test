from django.db import models

# Create your models here.
from core.models import BaseModel


class User(BaseModel):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Patient(User):
    blood_type = models.CharField(max_length=3)
    phone = models.CharField(max_length=13)


class Nurse(User):
    email = models.EmailField()
    birthday = models.DateTimeField(null=True, default=None)


class Doctor(User):
    email = models.EmailField()
    postal_code = models.CharField(max_length=10)
    degree = models.CharField(max_length=10)


class DoctorAssistant(Doctor):

    class Meta:
        proxy = True

    def analyze_data(self):
        ...

    def help_to_manage_reports(self):
        ...
