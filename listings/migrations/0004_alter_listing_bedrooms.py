# Generated by Django 4.0.5 on 2022-06-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listing_bedrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(choices=[(1, 'one'), (2, 'two')]),
        ),
    ]