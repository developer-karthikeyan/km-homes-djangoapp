# Generated by Django 4.0.5 on 2022-06-11 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_bedrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
        ),
    ]
