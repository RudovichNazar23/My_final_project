# Generated by Django 4.0.3 on 2022-04-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0008_alter_song_song_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name_song',
            field=models.CharField(default='', max_length=100),
        ),
    ]
