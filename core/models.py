from django.core.exceptions import ValidationError
from django.core import validators
from django.db import models


# Create your models here.

def default_brand():
    import random
    return random.choice(['akbar', 'asqar', 'reza'])


def brand_validator(value: str):
    if not value.istitle():
        raise ValidationError("The brand name should start with an uppercase letter!")


class Brand(models.Model):
    name = models.CharField(max_length=20, null=False, blank=True, default=default_brand,
                            help_text="The brand's name", verbose_name='Brand name',
                            validators=[brand_validator, validators.MaxLengthValidator(10, "Shorten your brand name!")])
    country = models.CharField(max_length=20)
    image = models.FileField(null=True, default=None)

    def __str__(self):
        return f"Brand {self.name} from {self.country}"
