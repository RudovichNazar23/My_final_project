# Generated by Django 4.0.3 on 2022-04-08 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_editor',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]