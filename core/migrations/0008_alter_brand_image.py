# Generated by Django 4.0.1 on 2022-01-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_brand_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]
