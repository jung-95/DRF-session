# Generated by Django 4.0.4 on 2022-07-25 03:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
