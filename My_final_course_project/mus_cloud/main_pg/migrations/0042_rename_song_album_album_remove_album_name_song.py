# Generated by Django 4.0.3 on 2022-06-30 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0041_alter_album_name_song'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='song',
            new_name='album',
        ),
        migrations.RemoveField(
            model_name='album',
            name='name_song',
        ),
    ]
