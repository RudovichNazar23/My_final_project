# Generated by Django 4.0.3 on 2022-04-03 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_song', models.CharField(max_length=100)),
                ('song_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_album', models.CharField(max_length=100)),
                ('album_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.artist')),
            ],
        ),
    ]
