# Generated by Django 4.0.3 on 2022-06-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0040_rename_album_album_song_album_name_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name_song',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]