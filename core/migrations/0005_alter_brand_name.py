# Generated by Django 4.0.1 on 2022-01-27 06:05

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(blank=True, default=core.models.default_brand, max_length=20),
        ),
    ]