# Generated by Django 4.0.3 on 2022-05-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0023_rename_instagram_link_user_profile_first_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='first_link',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='second_link',
            field=models.URLField(max_length=1000),
        ),
    ]