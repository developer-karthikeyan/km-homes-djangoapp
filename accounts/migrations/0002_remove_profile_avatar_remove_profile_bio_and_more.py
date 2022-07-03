# Generated by Django 4.0.5 on 2022-06-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pic'),
        ),
    ]
