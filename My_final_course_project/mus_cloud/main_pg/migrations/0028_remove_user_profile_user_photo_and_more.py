# Generated by Django 4.0.3 on 2022-05-21 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0027_alter_user_profile_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='user_photo',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='user_posts',
            field=models.TextField(default='', null=True),
        ),
    ]
