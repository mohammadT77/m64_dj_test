# Generated by Django 4.0.1 on 2022-01-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(blank=True, db_column='bname', max_length=20),
        ),
    ]