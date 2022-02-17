# Generated by Django 4.0.2 on 2022-02-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('value', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('price', 'Price'), ('percent', 'Percent')], max_length=10)),
                ('max_price', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
