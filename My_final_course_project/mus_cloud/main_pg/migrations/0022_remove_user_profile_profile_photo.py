# Generated by Django 4.0.3 on 2022-05-08 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0021_user_profile_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='profile_photo',
        ),
    ]
