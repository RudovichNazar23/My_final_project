# Generated by Django 4.0.3 on 2022-04-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pg', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song',
            field=models.FileField(default=None, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name_song',
            field=models.CharField(default='', max_length=100),
        ),
    ]
