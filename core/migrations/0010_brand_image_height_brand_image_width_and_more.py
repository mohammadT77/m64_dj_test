# Generated by Django 4.0.1 on 2022-01-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_brand_is_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image_height',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='image_width',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, default=None, height_field='image_height', null=True, upload_to='brand/', width_field='image_width'),
        ),
    ]