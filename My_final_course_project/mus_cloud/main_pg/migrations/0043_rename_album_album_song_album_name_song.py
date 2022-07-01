# Generated by Django 4.0.3 on 2022-06-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0042_rename_song_album_album_remove_album_name_song'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album',
            new_name='song',
        ),
        migrations.AddField(
            model_name='album',
            name='name_song',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
