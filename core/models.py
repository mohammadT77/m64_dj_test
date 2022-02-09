from django.contrib.auth.models import User
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


class BaseManager(models.Manager):

    def full_archive(self):
        return super().get_queryset()

    def get_queryset(self):
        return super().get_queryset().exclude(is_delete=True)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = BaseManager()

    is_delete = models.BooleanField(default=False, editable=False, db_index=True)

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save(using=using)
        # return super().delete(using, keep_parents)

    def restore(self):
        self.is_delete = False
        self.save()


class Brand(BaseModel):
    name = models.CharField(max_length=20, null=False, blank=True, default=default_brand,
                            help_text="The brand's name", verbose_name='Brand name',
                            validators=[brand_validator, validators.MaxLengthValidator(10, "Shorten your brand name!")])
    country = models.CharField(max_length=20)
    image = models.FileField(null=True, default=None, upload_to='brand/', blank=True)

    def __str__(self):
        return f"Brand #{self.id}: {self.name} from {self.country}"
