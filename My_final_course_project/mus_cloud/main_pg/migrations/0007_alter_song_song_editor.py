# Generated by Django 4.0.3 on 2022-04-10 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_pg', '0006_alter_song_song_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_editor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
