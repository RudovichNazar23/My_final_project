# Generated by Django 4.0.3 on 2022-04-10 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0013_alter_song_song_editor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_editor',
            new_name='user',
        ),
    ]
