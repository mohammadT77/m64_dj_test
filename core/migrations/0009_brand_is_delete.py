# Generated by Django 4.0.1 on 2022-01-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]